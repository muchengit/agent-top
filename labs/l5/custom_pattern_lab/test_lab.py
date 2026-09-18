from __future__ import annotations

import unittest

from .agent_top_labs_l5_custom_pattern_lab import VerifiableActionPattern


class CustomPatternLabTest(unittest.TestCase):
    def test_safe_request_gets_three_step_plan(self) -> None:
        result = VerifiableActionPattern(("delete_all",)).plan("update profile")
        self.assertEqual(result.stop_reason, "ready_for_execution")
        self.assertEqual([step.intent for step in result.steps], ["clarify", "execute", "verify"])

    def test_safety_rule_stops_before_execution(self) -> None:
        result = VerifiableActionPattern(("delete_all",)).plan("delete_all")
        self.assertEqual(result.stop_reason, "blocked_by_safety_rule")
        self.assertEqual(result.steps, ())
