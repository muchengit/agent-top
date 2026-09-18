"""L5 deterministic gate for evaluating patterns before catalog entry."""

from __future__ import annotations

from dataclasses import dataclass

STATUS_PASS = "pass"
STATUS_FAIL = "fail"
STATUS_NEEDS_REVIEW = "needs_review"

OUTCOME_PASSED = "passed"
OUTCOME_NEEDS_FIX = "needs_fix"
OUTCOME_REJECTED = "rejected"

RISK_LOW = "low"
RISK_MEDIUM = "medium"
RISK_HIGH = "high"

VALIDATION_DRAFT = "draft"
VALIDATION_VALIDATED = "validated"


@dataclass(frozen=True)
class PatternEntry:
    """A candidate pattern submitted to the evaluation gate."""

    name: str
    owner: str
    domain: str
    risk_level: str
    evidence_types: tuple[str, ...]
    reproduction_steps: tuple[str, ...]
    validation_status: str
    has_documentation: bool = True
    unresolved_high_risks: tuple[str, ...] = ()


@dataclass(frozen=True)
class GateDimension:
    """One scored evaluation dimension for a single pattern."""

    name: str
    status: str
    reason: str


@dataclass(frozen=True)
class EvaluationResult:
    """Per-pattern gate result with dimension-level detail."""

    name: str
    outcome: str
    dimensions: tuple[GateDimension, ...]


@dataclass(frozen=True)
class DimensionSummary:
    """Aggregated pass/fail/needs-review counts for one dimension."""

    name: str
    passed: int
    failed: int
    needs_review: int


@dataclass(frozen=True)
class GateReport:
    """Aggregated gate report across a batch of patterns."""

    total: int
    passed: int
    needs_fix: int
    rejected: int
    per_dimension: tuple[DimensionSummary, ...]


class PatternEvalGate:
    """Evaluate pattern entries against catalog entry requirements.

    Five dimensions are scored per pattern: reproducibility, evidence,
    safety, documentation, and ownership. Reproducibility and safety
    failures block entry outright; other gaps require fixes.
    """

    BLOCKING_DIMENSIONS: tuple[str, ...] = ("reproducibility", "safety")
    DIMENSIONS: tuple[str, ...] = (
        "reproducibility",
        "evidence",
        "safety",
        "documentation",
        "ownership",
    )

    def evaluate(self, entry: PatternEntry) -> EvaluationResult:
        """Score a single pattern entry and return its gate result."""
        dimensions = (
            self._check_reproducibility(entry),
            self._check_evidence(entry),
            self._check_safety(entry),
            self._check_documentation(entry),
            self._check_ownership(entry),
        )
        return EvaluationResult(entry.name, self._aggregate(dimensions), dimensions)

    def evaluate_batch(self, entries: tuple[PatternEntry, ...]) -> GateReport:
        """Score a batch of patterns and summarize the gate outcome."""
        results = [self.evaluate(entry) for entry in entries]
        passed = sum(1 for result in results if result.outcome == OUTCOME_PASSED)
        needs_fix = sum(1 for result in results if result.outcome == OUTCOME_NEEDS_FIX)
        rejected = sum(1 for result in results if result.outcome == OUTCOME_REJECTED)
        per_dimension = tuple(
            self._summarize_dimension(name, results) for name in self.DIMENSIONS
        )
        return GateReport(len(entries), passed, needs_fix, rejected, per_dimension)

    @staticmethod
    def _check_reproducibility(entry: PatternEntry) -> GateDimension:
        """Require reproduction steps and a validated status."""
        if not entry.reproduction_steps:
            return GateDimension(
                "reproducibility", STATUS_FAIL, "missing reproduction steps"
            )
        if entry.validation_status != VALIDATION_VALIDATED:
            return GateDimension(
                "reproducibility",
                STATUS_NEEDS_REVIEW,
                "reproduction steps present but pattern not validated",
            )
        return GateDimension(
            "reproducibility", STATUS_PASS, "reproduction steps documented and validated"
        )

    @staticmethod
    def _check_evidence(entry: PatternEntry) -> GateDimension:
        """Require at least one eval or test evidence type."""
        if not entry.evidence_types:
            return GateDimension(
                "evidence", STATUS_FAIL, "missing eval/test evidence"
            )
        if entry.validation_status != VALIDATION_VALIDATED:
            return GateDimension(
                "evidence", STATUS_NEEDS_REVIEW, "evidence present but validation pending"
            )
        return GateDimension("evidence", STATUS_PASS, "eval/test evidence present")

    @staticmethod
    def _check_safety(entry: PatternEntry) -> GateDimension:
        """Reject unresolved high-risk items; require review for high-risk patterns."""
        if entry.unresolved_high_risks:
            risks = ", ".join(entry.unresolved_high_risks)
            return GateDimension(
                "safety", STATUS_FAIL, f"unresolved high-risk items: {risks}"
            )
        if entry.risk_level == RISK_HIGH:
            return GateDimension(
                "safety", STATUS_NEEDS_REVIEW, "high-risk pattern requires human sign-off"
            )
        return GateDimension("safety", STATUS_PASS, "no unresolved high-risk items")

    @staticmethod
    def _check_documentation(entry: PatternEntry) -> GateDimension:
        """Require a README or usage description."""
        if not entry.has_documentation:
            return GateDimension(
                "documentation", STATUS_FAIL, "missing README/usage documentation"
            )
        return GateDimension(
            "documentation", STATUS_PASS, "README/usage documentation present"
        )

    @staticmethod
    def _check_ownership(entry: PatternEntry) -> GateDimension:
        """Require a non-empty owner."""
        if not entry.owner.strip():
            return GateDimension("ownership", STATUS_FAIL, "missing owner")
        return GateDimension("ownership", STATUS_PASS, f"owner: {entry.owner}")

    @staticmethod
    def _aggregate(dimensions: tuple[GateDimension, ...]) -> str:
        """Combine dimension scores into a single gate outcome."""
        if any(
            dimension.status == STATUS_FAIL
            and dimension.name in PatternEvalGate.BLOCKING_DIMENSIONS
            for dimension in dimensions
        ):
            return OUTCOME_REJECTED
        if any(dimension.status != STATUS_PASS for dimension in dimensions):
            return OUTCOME_NEEDS_FIX
        return OUTCOME_PASSED

    @staticmethod
    def _summarize_dimension(
        name: str, results: list[EvaluationResult]
    ) -> DimensionSummary:
        """Count pass/fail/needs-review outcomes for one dimension."""
        passed = 0
        failed = 0
        needs_review = 0
        for result in results:
            for dimension in result.dimensions:
                if dimension.name != name:
                    continue
                if dimension.status == STATUS_PASS:
                    passed += 1
                elif dimension.status == STATUS_FAIL:
                    failed += 1
                else:
                    needs_review += 1
        return DimensionSummary(name, passed, failed, needs_review)
