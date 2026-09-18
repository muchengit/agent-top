"""L4 deterministic deployment hygiene assessment.

Combines observability completeness, cost budget, and release gate checks
into one deploy/no-deploy decision with explicit reasons. No network or
API keys are required.
"""

from __future__ import annotations

from dataclasses import dataclass

DECISION_DEPLOY = "deploy"
DECISION_BLOCK = "block"
DECISION_DEFER = "defer"


@dataclass(frozen=True)
class ObservabilitySnapshot:
    """Completeness of production observability before a deploy."""

    trace_coverage: float
    missing_critical_fields: int
    alert_channels_configured: bool


@dataclass(frozen=True)
class CostSnapshot:
    """Budget health for the upcoming release."""

    cost_ratio: float
    budget_ratio: float
    has_rollback_budget: bool


@dataclass(frozen=True)
class ReleaseGateResult:
    """Outcome of the release gate checks."""

    safety_passed: bool
    rollback_plan_present: bool
    regression_diff_approved: bool


@dataclass(frozen=True)
class DeploymentAssessment:
    decision: str
    reasons: tuple[str, ...]


def assess_deployment(
    observability: ObservabilitySnapshot,
    cost: CostSnapshot,
    gate: ReleaseGateResult,
) -> DeploymentAssessment:
    """Combine the three hygiene dimensions into one decision.

    Rules:
    - Missing critical trace fields or unconfigured alerts block the deploy.
    - Cost over budget without a rollback budget defers the deploy.
    - Safety failure, missing rollback plan, or unapproved regression diff
      blocks the deploy.
    - Otherwise the deploy is allowed.
    """
    reasons: list[str] = []

    if not gate.safety_passed:
        reasons.append("safety_failure")
    if not gate.rollback_plan_present:
        reasons.append("missing_rollback_plan")
    if not gate.regression_diff_approved:
        reasons.append("unapproved_regression_diff")
    if observability.missing_critical_fields > 0:
        reasons.append("missing_critical_trace_fields")
    if not observability.alert_channels_configured:
        reasons.append("alerts_not_configured")

    if reasons:
        return DeploymentAssessment(DECISION_BLOCK, tuple(reasons))

    if cost.cost_ratio > cost.budget_ratio and not cost.has_rollback_budget:
        return DeploymentAssessment(
            DECISION_DEFER,
            ("cost_over_budget_without_rollback_budget",),
        )

    if observability.trace_coverage < 1.0:
        reasons.append("partial_trace_coverage")
        return DeploymentAssessment(DECISION_DEFER, tuple(reasons))

    return DeploymentAssessment(DECISION_DEPLOY, ())
