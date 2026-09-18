from __future__ import annotations

import unittest

from .agent_top_labs_l4_regression_gate import ReleaseProfile, evaluate_release


class RegressionGateTest(unittest.TestCase):
    def test_green_release_passes(self) -> None:
        profile = ReleaseProfile(0, 0, True, 0.8, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertTrue(should_ship)
        self.assertEqual(failures, [])

    def test_safety_failure_blocks_release(self) -> None:
        profile = ReleaseProfile(1, 0, True, 0.8, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertFalse(should_ship)
        self.assertIn("critical_safety_failures", failures)

    def test_missing_trace_blocks_release(self) -> None:
        profile = ReleaseProfile(0, 1, True, 0.8, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertFalse(should_ship)
        self.assertEqual(failures, ["missing_trace_fields"])

    def test_missing_rollback_blocks_release(self) -> None:
        profile = ReleaseProfile(0, 0, False, 0.8, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertFalse(should_ship)
        self.assertEqual(failures, ["missing_rollback_plan"])

    def test_cost_over_budget_blocks_release(self) -> None:
        profile = ReleaseProfile(0, 0, True, 1.2, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertFalse(should_ship)
        self.assertEqual(failures, ["cost_over_budget"])

    def test_cost_boundary_equal_passes(self) -> None:
        profile = ReleaseProfile(0, 0, True, 1.0, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertTrue(should_ship)
        self.assertEqual(failures, [])

    def test_multiple_failures_listed_in_order(self) -> None:
        profile = ReleaseProfile(1, 1, False, 1.5, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertFalse(should_ship)
        self.assertEqual(
            failures,
            [
                "critical_safety_failures",
                "missing_trace_fields",
                "missing_rollback_plan",
                "cost_over_budget",
            ],
        )

    def test_zero_budgets_green(self) -> None:
        profile = ReleaseProfile(0, 0, True, 0.0, 0.0)
        should_ship, failures = evaluate_release(profile)
        self.assertTrue(should_ship)
        self.assertEqual(failures, [])

    def test_negative_safety_failures_not_flagged(self) -> None:
        profile = ReleaseProfile(-1, 0, True, 0.5, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertTrue(should_ship)
        self.assertEqual(failures, [])

    def test_gate_result_not_used_here(self) -> None:
        from .agent_top_labs_l4_regression_gate import GateResult

        result = GateResult("safety", True, True)
        self.assertEqual(result.name, "safety")
        self.assertTrue(result.passed)
        self.assertTrue(result.blocking)

    def test_negative_missing_trace_not_flagged(self) -> None:
        profile = ReleaseProfile(0, -2, True, 0.5, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertTrue(should_ship)
        self.assertEqual(failures, [])

    def test_all_failure_reasons_exclusive(self) -> None:
        profile = ReleaseProfile(2, 1, False, 3.0, 1.0)
        _, failures = evaluate_release(profile)
        self.assertEqual(
            set(failures),
            {
                "critical_safety_failures",
                "missing_trace_fields",
                "missing_rollback_plan",
                "cost_over_budget",
            },
        )

    def test_safety_still_blocks_when_other_fields_ok(self) -> None:
        profile = ReleaseProfile(3, 0, True, 0.9, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertFalse(should_ship)
        self.assertEqual(failures, ["critical_safety_failures"])

    def test_rollback_present_with_zero_everything(self) -> None:
        profile = ReleaseProfile(0, 0, True, 0.0, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertTrue(should_ship)

    def test_cost_ratio_exactly_budget_passes(self) -> None:
        profile = ReleaseProfile(0, 0, True, 1.0, 1.0)
        should_ship, _ = evaluate_release(profile)
        self.assertTrue(should_ship)

    def test_negative_cost_ratio_never_over_budget(self) -> None:
        profile = ReleaseProfile(0, 0, True, -1.0, 0.0)
        should_ship, failures = evaluate_release(profile)
        self.assertTrue(should_ship)
        self.assertNotIn("cost_over_budget", failures)

    def test_returns_tuple_of_bool_and_list(self) -> None:
        profile = ReleaseProfile(0, 0, True, 0.5, 1.0)
        result = evaluate_release(profile)
        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], bool)
        self.assertIsInstance(result[1], list)
