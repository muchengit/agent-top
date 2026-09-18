from __future__ import annotations

import unittest

from .agent_top_labs_l5_multilingual_pattern_lab import (
    BLOCKED_REASON,
    READY_REASON,
    SAFETY_RULE,
    assert_blocked_plan,
    assert_ready_plan,
    run_python_pattern,
)


class MultilingualPatternLabTest(unittest.TestCase):
    def test_python_safe_request_gets_three_step_plan(self) -> None:
        stop_reason, steps = run_python_pattern("update profile")
        assert_ready_plan(stop_reason, steps)

    def test_python_plan_steps_carry_tool_and_rollback_hint(self) -> None:
        stop_reason, steps = run_python_pattern("update profile")
        self.assertEqual(stop_reason, READY_REASON)
        self.assertEqual(
            [tool for _, tool, _ in steps],
            ["validator", "tool_gateway", "eval_probe"],
        )
        self.assertEqual(
            [hint for _, _, hint in steps],
            ["remove unclear fields", "restore previous state", "disable path"],
        )

    def test_python_safety_rule_stops_before_execution(self) -> None:
        stop_reason, steps = run_python_pattern("delete_all")
        assert_blocked_plan(stop_reason, steps)

    def test_python_blocked_plan_returns_no_steps(self) -> None:
        stop_reason, steps = run_python_pattern(SAFETY_RULE)
        self.assertEqual(stop_reason, BLOCKED_REASON)
        self.assertEqual(steps, [])

    def test_python_rule_matching_substring_of_word_blocks(self) -> None:
        stop_reason, steps = run_python_pattern("undo delete_all entries")
        self.assertEqual(stop_reason, BLOCKED_REASON)
        self.assertEqual(steps, [])

    def test_python_safety_rule_matches_ascii_rule_in_request(self) -> None:
        stop_reason, steps = run_python_pattern("please run delete_all now")
        self.assertEqual(stop_reason, BLOCKED_REASON)
        self.assertEqual(steps, [])

    def test_python_unicode_text_that_avoids_rule_stays_ready(self) -> None:
        stop_reason, steps = run_python_pattern("更新用户资料")
        assert_ready_plan(stop_reason, steps)

    def test_python_empty_request_stays_ready(self) -> None:
        stop_reason, steps = run_python_pattern("")
        self.assertEqual(stop_reason, READY_REASON)
        self.assertEqual([intent for intent, _, _ in steps], ["clarify", "execute", "verify"])

    def test_python_empty_request_has_no_rule_but_stays_ready(self) -> None:
        stop_reason, steps = run_python_pattern("")
        self.assertEqual(stop_reason, READY_REASON)
        self.assertEqual([intent for intent, _, _ in steps], ["clarify", "execute", "verify"])

    def test_python_newline_and_whitespace_surrounding_rule_still_blocks(self) -> None:
        stop_reason, steps = run_python_pattern("please run:\n  delete_all\nnow")
        self.assertEqual(stop_reason, BLOCKED_REASON)
        self.assertEqual(steps, [])

    def test_python_case_variant_does_not_trigger_rule(self) -> None:
        stop_reason, steps = run_python_pattern("DELETE_ALL")
        self.assertEqual(stop_reason, READY_REASON)
        self.assertEqual([intent for intent, _, _ in steps], ["clarify", "execute", "verify"])

    def test_python_blocked_reason_is_constant(self) -> None:
        self.assertEqual(BLOCKED_REASON, "blocked_by_safety_rule")

    def test_python_ready_reason_is_constant(self) -> None:
        self.assertEqual(READY_REASON, "ready_for_execution")

    def test_python_safety_rule_is_constant(self) -> None:
        self.assertEqual(SAFETY_RULE, "delete_all")

    def test_assert_ready_plan_rejects_blocked_result(self) -> None:
        with self.assertRaises(AssertionError):
            assert_ready_plan(BLOCKED_REASON, [])

    def test_assert_blocked_plan_rejects_ready_result(self) -> None:
        _, steps = run_python_pattern("update profile")
        with self.assertRaises(AssertionError):
            assert_blocked_plan(READY_REASON, steps)

    def test_python_plan_is_deterministic_and_mixed_payload_stays_ready(self) -> None:
        first = run_python_pattern("update profile")
        second = run_python_pattern("update profile")
        self.assertEqual(first, second)
        stop_reason, steps = run_python_pattern("update profile but mention unlock-purge in docs")
        self.assertEqual(stop_reason, READY_REASON)
        self.assertEqual([intent for intent, _, _ in steps], ["clarify", "execute", "verify"])


if __name__ == "__main__":
    unittest.main()
