"""Deterministic tests for the L5 pattern evaluation gate lab."""

from __future__ import annotations

import dataclasses
import unittest

from .agent_top_labs_l5_pattern_eval_gate import (
    OUTCOME_NEEDS_FIX,
    OUTCOME_PASSED,
    OUTCOME_REJECTED,
    RISK_HIGH,
    RISK_LOW,
    STATUS_FAIL,
    STATUS_PASS,
    VALIDATION_VALIDATED,
    PatternEntry,
    PatternEvalGate,
)

VALID_ENTRY = PatternEntry(
    name="safe-retrieval-augmented-action",
    owner="agent-platform-team",
    domain="retrieval",
    risk_level=RISK_LOW,
    evidence_types=("eval_probe", "unit_test"),
    reproduction_steps=("load catalog", "run eval probe", "inspect audit log"),
    validation_status=VALIDATION_VALIDATED,
)


class PatternEvalGateTest(unittest.TestCase):
    def test_fully_compliant_pattern_passes(self) -> None:
        result = PatternEvalGate().evaluate(VALID_ENTRY)
        self.assertEqual(result.outcome, OUTCOME_PASSED)
        self.assertTrue(all(d.status == STATUS_PASS for d in result.dimensions))

    def test_missing_reproduction_steps_rejects(self) -> None:
        entry = dataclasses.replace(VALID_ENTRY, reproduction_steps=())
        result = PatternEvalGate().evaluate(entry)
        self.assertEqual(result.outcome, OUTCOME_REJECTED)
        self.assertEqual(result.dimensions[0].status, STATUS_FAIL)

    def test_missing_evidence_needs_fix(self) -> None:
        entry = dataclasses.replace(VALID_ENTRY, evidence_types=())
        result = PatternEvalGate().evaluate(entry)
        self.assertEqual(result.outcome, OUTCOME_NEEDS_FIX)
        self.assertEqual(result.dimensions[1].status, STATUS_FAIL)

    def test_unmitigated_high_risk_rejects(self) -> None:
        entry = dataclasses.replace(
            VALID_ENTRY, unresolved_high_risks=("unsandboxed_code_execution",)
        )
        result = PatternEvalGate().evaluate(entry)
        self.assertEqual(result.outcome, OUTCOME_REJECTED)
        self.assertEqual(result.dimensions[2].status, STATUS_FAIL)

    def test_missing_documentation_needs_fix(self) -> None:
        entry = dataclasses.replace(VALID_ENTRY, has_documentation=False)
        result = PatternEvalGate().evaluate(entry)
        self.assertEqual(result.outcome, OUTCOME_NEEDS_FIX)
        self.assertEqual(result.dimensions[3].status, STATUS_FAIL)

    def test_missing_owner_needs_fix(self) -> None:
        entry = dataclasses.replace(VALID_ENTRY, owner="   ")
        result = PatternEvalGate().evaluate(entry)
        self.assertEqual(result.outcome, OUTCOME_NEEDS_FIX)
        self.assertEqual(result.dimensions[4].status, STATUS_FAIL)

    def test_high_risk_with_mitigation_needs_review(self) -> None:
        entry = dataclasses.replace(
            VALID_ENTRY, risk_level=RISK_HIGH, unresolved_high_risks=()
        )
        result = PatternEvalGate().evaluate(entry)
        self.assertEqual(result.outcome, OUTCOME_NEEDS_FIX)
        self.assertEqual(result.dimensions[2].status, "needs_review")

    def test_batch_evaluation_statistics(self) -> None:
        entries = (
            VALID_ENTRY,
            dataclasses.replace(VALID_ENTRY, name="p2", evidence_types=()),
            dataclasses.replace(VALID_ENTRY, name="p3", reproduction_steps=()),
            dataclasses.replace(VALID_ENTRY, name="p4", has_documentation=False),
            dataclasses.replace(
                VALID_ENTRY,
                name="p5",
                unresolved_high_risks=("unchecked_prompt_injection",),
            ),
        )
        report = PatternEvalGate().evaluate_batch(entries)
        self.assertEqual(report.total, 5)
        self.assertEqual(report.passed, 1)
        self.assertEqual(report.needs_fix, 2)
        self.assertEqual(report.rejected, 2)

    def test_empty_pattern_list(self) -> None:
        report = PatternEvalGate().evaluate_batch(())
        self.assertEqual(report.total, 0)
        self.assertEqual(report.passed, 0)
        self.assertEqual(report.needs_fix, 0)
        self.assertEqual(report.rejected, 0)
        self.assertEqual(len(report.per_dimension), 5)
        self.assertTrue(all(d.passed == 0 and d.failed == 0 for d in report.per_dimension))

    def test_dimension_details(self) -> None:
        entry = dataclasses.replace(VALID_ENTRY, evidence_types=())
        result = PatternEvalGate().evaluate(entry)
        self.assertEqual(len(result.dimensions), 5)
        self.assertEqual(
            [d.name for d in result.dimensions],
            ["reproducibility", "evidence", "safety", "documentation", "ownership"],
        )
        self.assertEqual(result.dimensions[1].name, "evidence")
        self.assertIn("evidence", result.dimensions[1].reason)


if __name__ == "__main__":
    unittest.main()
