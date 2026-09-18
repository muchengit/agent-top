"""Deterministic tests for the L4 deployment hygiene lab."""

from __future__ import annotations

import unittest

from .agent_top_labs_l4_deployment_hygiene import (
    DECISION_BLOCK,
    DECISION_DEFER,
    DECISION_DEPLOY,
    CostSnapshot,
    ObservabilitySnapshot,
    ReleaseGateResult,
    assess_deployment,
)

HEALTHY_OBS = ObservabilitySnapshot(
    trace_coverage=1.0,
    missing_critical_fields=0,
    alert_channels_configured=True,
)
HEALTHY_COST = CostSnapshot(cost_ratio=0.8, budget_ratio=1.0, has_rollback_budget=True)
HEALTHY_GATE = ReleaseGateResult(
    safety_passed=True,
    rollback_plan_present=True,
    regression_diff_approved=True,
)


class DeploymentHygieneTest(unittest.TestCase):
    def test_healthy_deployment_deploys(self) -> None:
        result = assess_deployment(HEALTHY_OBS, HEALTHY_COST, HEALTHY_GATE)
        self.assertEqual(result.decision, DECISION_DEPLOY)
        self.assertEqual(result.reasons, ())

    def test_safety_failure_blocks(self) -> None:
        gate = ReleaseGateResult(
            safety_passed=False,
            rollback_plan_present=True,
            regression_diff_approved=True,
        )
        result = assess_deployment(HEALTHY_OBS, HEALTHY_COST, gate)
        self.assertEqual(result.decision, DECISION_BLOCK)
        self.assertIn("safety_failure", result.reasons)

    def test_missing_critical_trace_field_blocks(self) -> None:
        obs = ObservabilitySnapshot(
            trace_coverage=0.9,
            missing_critical_fields=2,
            alert_channels_configured=True,
        )
        result = assess_deployment(obs, HEALTHY_COST, HEALTHY_GATE)
        self.assertEqual(result.decision, DECISION_BLOCK)
        self.assertIn("missing_critical_trace_fields", result.reasons)

    def test_cost_over_budget_without_rollback_budget_defers(self) -> None:
        cost = CostSnapshot(cost_ratio=1.2, budget_ratio=1.0, has_rollback_budget=False)
        result = assess_deployment(HEALTHY_OBS, cost, HEALTHY_GATE)
        self.assertEqual(result.decision, DECISION_DEFER)
        self.assertIn("cost_over_budget_without_rollback_budget", result.reasons)

    def test_cost_over_budget_with_rollback_budget_does_not_block(self) -> None:
        cost = CostSnapshot(cost_ratio=1.2, budget_ratio=1.0, has_rollback_budget=True)
        result = assess_deployment(HEALTHY_OBS, cost, HEALTHY_GATE)
        self.assertEqual(result.decision, DECISION_DEPLOY)

    def test_partial_trace_coverage_defers(self) -> None:
        obs = ObservabilitySnapshot(
            trace_coverage=0.7,
            missing_critical_fields=0,
            alert_channels_configured=True,
        )
        result = assess_deployment(obs, HEALTHY_COST, HEALTHY_GATE)
        self.assertEqual(result.decision, DECISION_DEFER)
        self.assertIn("partial_trace_coverage", result.reasons)

    def test_unconfigured_alerts_block(self) -> None:
        obs = ObservabilitySnapshot(
            trace_coverage=1.0,
            missing_critical_fields=0,
            alert_channels_configured=False,
        )
        result = assess_deployment(obs, HEALTHY_COST, HEALTHY_GATE)
        self.assertEqual(result.decision, DECISION_BLOCK)
        self.assertIn("alerts_not_configured", result.reasons)
