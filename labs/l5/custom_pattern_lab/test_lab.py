from __future__ import annotations

import unittest

from .agent_top_labs_l5_custom_pattern_lab import PlanStep, VerifiableActionPattern


class CustomPatternLabTest(unittest.TestCase):
    def test_safe_request_gets_three_step_plan(self) -> None:
        result = VerifiableActionPattern(("delete_all",)).plan("update profile")
        self.assertEqual(result.stop_reason, "ready_for_execution")
        self.assertEqual([step.intent for step in result.steps], ["clarify", "execute", "verify"])

    def test_plan_steps_have_tool_and_rollback_hint(self) -> None:
        result = VerifiableActionPattern(("delete_all",)).plan("update profile")
        self.assertEqual(
            [step.tool for step in result.steps],
            ["validator", "tool_gateway", "eval_probe"],
        )
        self.assertEqual(
            [step.rollback_hint for step in result.steps],
            ["remove unclear fields", "restore previous state", "disable path"],
        )

    def test_blocked_plan_has_no_steps_and_no_verification(self) -> None:
        result = VerifiableActionPattern(("delete_all",)).plan("delete_all")
        self.assertEqual(result.stop_reason, "blocked_by_safety_rule")
        self.assertEqual(result.steps, ())
        self.assertFalse(any(step.intent == "verify" for step in result.steps))

    def test_multiple_safety_rules_any_match_blocks(self) -> None:
        pattern = VerifiableActionPattern(("delete_all", "drop_database", "purge"))
        for request in ("delete_all", "drop_database", "purge"):
            result = pattern.plan(request)
            self.assertEqual(result.stop_reason, "blocked_by_safety_rule")
            self.assertEqual(result.steps, ())

    def test_safety_rule_matching_substring_of_word_blocks(self) -> None:
        pattern = VerifiableActionPattern(("delete_all",))
        result = pattern.plan("undo delete_all entries")
        self.assertEqual(result.stop_reason, "blocked_by_safety_rule")

    def test_safety_rule_matches_chinese_translation(self) -> None:
        pattern = VerifiableActionPattern(("删除全部",))
        result = pattern.plan("执行 删除全部命令")
        self.assertEqual(result.stop_reason, "blocked_by_safety_rule")
        self.assertEqual(result.steps, ())

    def test_unicode_text_that_avoids_rule_stays_ready(self) -> None:
        pattern = VerifiableActionPattern(("删除全部", "delete_all"))
        result = pattern.plan("更新用户资料")
        self.assertEqual(result.stop_reason, "ready_for_execution")
        self.assertEqual([step.intent for step in result.steps], ["clarify", "execute", "verify"])

    def test_empty_request_is_allowed_and_returns_empty_plan_steps(self) -> None:
        result = VerifiableActionPattern(("delete_all",)).plan("")
        self.assertEqual(result.stop_reason, "ready_for_execution")
        self.assertEqual([step.intent for step in result.steps], ["clarify", "execute", "verify"])

    def test_empty_safety_rules_never_block(self) -> None:
        result = VerifiableActionPattern(()).plan("delete_all")
        self.assertEqual(result.stop_reason, "ready_for_execution")
        self.assertEqual([step.intent for step in result.steps], ["clarify", "execute", "verify"])

    def test_newline_and_whitespace_surrounding_rule_still_blocks(self) -> None:
        pattern = VerifiableActionPattern(("delete_all",))
        self.assertEqual(
            pattern.plan("please run:\n  delete_all\nnow").stop_reason,
            "blocked_by_safety_rule",
        )

    def test_case_sensitive_rule_is_not_triggered_by_case_variant(self) -> None:
        result = VerifiableActionPattern(("delete_all",)).plan("DELETE_ALL")
        self.assertEqual(result.stop_reason, "ready_for_execution")
        self.assertEqual([step.intent for step in result.steps], ["clarify", "execute", "verify"])

    def test_clarify_step_carries_rollback_note_for_unclear_fields(self) -> None:
        result = VerifiableActionPattern(("delete_all",)).plan("update profile")
        self.assertEqual(result.steps[0], PlanStep("clarify", "validator", "remove unclear fields"))

    def test_execute_and_verify_steps_carry_rollback_notes(self) -> None:
        pattern = VerifiableActionPattern(("delete_all",))
        steps = pattern.plan("update profile").steps
        self.assertEqual(steps[1], PlanStep("execute", "tool_gateway", "restore previous state"))
        self.assertEqual(steps[2], PlanStep("verify", "eval_probe", "disable path"))

    def test_plan_is_deterministic_for_same_request(self) -> None:
        pattern = VerifiableActionPattern(("purge",))
        first = pattern.plan("update profile")
        second = pattern.plan("update profile")
        self.assertEqual(first, second)

    def test_mixed_payload_mentioning_rule_still_blocks(self) -> None:
        pattern = VerifiableActionPattern(("purge",))
        mixed = pattern.plan("safe update but mentions unlock-purge in docs")
        self.assertEqual(mixed.stop_reason, "blocked_by_safety_rule")
        self.assertEqual(mixed.steps, ())

    def test_result_is_frozen_given_frozen_plan_steps(self) -> None:
        result = VerifiableActionPattern(("delete_all",)).plan("update profile")
        steps = result.steps
        with self.assertRaises(Exception):
            steps[0].intent = "execute"  # type: ignore[misc]
        with self.assertRaises(Exception):
            result.steps = ()  # type: ignore[misc]


if __name__ == "__main__":
    unittest.main()
