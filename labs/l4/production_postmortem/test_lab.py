from __future__ import annotations

import unittest
from datetime import date

from .agent_top_labs_l4_production_postmortem import (
    ActionItem,
    ActionType,
    PostmortemDraft,
    Severity,
    highest_severity,
    required_coverage,
    unresolved_actions,
)


class ProductionPostmortemTest(unittest.TestCase):
    def test_required_coverage_flags_missing_sections(self) -> None:
        draft = PostmortemDraft(
            summary="Tool calls failed for one user.",
            root_causes=("Missing input validation",),
            action_items=(),
            rollback_plan="Roll back prompt changes.",
            evaluation_plan="Add regression eval for rejected inputs.",
            safety_controls=("Input validation",),
        )
        self.assertEqual(required_coverage(draft), ["action items"])

    def test_unresolved_actions_include_missing_owner(self) -> None:
        item = ActionItem("Add rate limit", "", date(2026, 9, 30), ActionType.SAFETY_GUARDRAIL)
        draft = PostmortemDraft("summary", ("cause",), (item,), "rollback", "eval", ("safety",))
        self.assertEqual(unresolved_actions(draft), [item])

    def test_overdue_guardrail_becomes_highest_severity(self) -> None:
        today = date(2026, 9, 20)
        overdue = ActionItem(
            "Restore auth boundary",
            "team",
            date(2026, 9, 19),
            ActionType.SAFETY_GUARDRAIL,
        )
        draft = PostmortemDraft("summary", ("cause",), (overdue,), "rollback", "eval", ("safety",))
        self.assertEqual(highest_severity(unresolved_actions(draft), today), Severity.SEV1)

    def test_required_coverage_empty_draft_lists_all(self) -> None:
        draft = PostmortemDraft("", (), (), "", "", ())
        self.assertEqual(
            required_coverage(draft),
            [
                "summary",
                "root causes",
                "rollback plan",
                "evaluation plan",
                "safety controls",
                "action items",
            ],
        )

    def test_required_coverage_whitespace_summary(self) -> None:
        item = ActionItem(
            "t",
            "o",
            date(2026, 9, 30),
            ActionType.PROCESS_CHANGE,
        )
        draft = PostmortemDraft(
            "   ",
            ("cause",),
            (item,),
            "rollback",
            "eval",
            ("safety",),
        )
        self.assertIn("summary", required_coverage(draft))

    def test_complete_draft_has_no_missing_sections(self) -> None:
        item = ActionItem(
            "Add rate limit",
            "owner",
            date(2026, 9, 30),
            ActionType.SAFETY_GUARDRAIL,
            done=True,
        )
        draft = PostmortemDraft("summary", ("cause",), (item,), "rollback", "eval", ("safety",))
        self.assertEqual(required_coverage(draft), [])

    def test_unresolved_includes_in_progress_item(self) -> None:
        item = ActionItem("Add rate limit", "owner", date(2026, 9, 30), ActionType.SAFETY_GUARDRAIL)
        draft = PostmortemDraft("summary", ("cause",), (item,), "rollback", "eval", ("safety",))
        self.assertEqual(unresolved_actions(draft), [item])

    def test_done_item_with_empty_owner_is_unresolved(self) -> None:
        item = ActionItem(
            "Add rate limit",
            "",
            date(2026, 9, 30),
            ActionType.SAFETY_GUARDRAIL,
            done=True,
        )
        draft = PostmortemDraft("summary", ("cause",), (item,), "rollback", "eval", ("safety",))
        self.assertEqual(unresolved_actions(draft), [item])

    def test_is_overdue_boundary_due_today_not_overdue(self) -> None:
        today = date(2026, 9, 20)
        item = ActionItem("Fix bug", "owner", today, ActionType.IMMEDIATE_FIX)
        self.assertFalse(item.is_overdue(today))

    def test_is_overdue_past_date_is_overdue(self) -> None:
        today = date(2026, 9, 20)
        item = ActionItem("Fix bug", "owner", date(2026, 9, 19), ActionType.IMMEDIATE_FIX)
        self.assertTrue(item.is_overdue(today))

    def test_done_past_item_not_overdue(self) -> None:
        today = date(2026, 9, 20)
        item = ActionItem(
            "Fix bug",
            "owner",
            date(2026, 9, 19),
            ActionType.IMMEDIATE_FIX,
            done=True,
        )
        self.assertFalse(item.is_overdue(today))

    def test_has_required_fields_empty_title(self) -> None:
        item = ActionItem("", "owner", date(2026, 9, 30), ActionType.PROCESS_CHANGE)
        self.assertFalse(item.has_required_fields())

    def test_highest_severity_none_when_all_done(self) -> None:
        today = date(2026, 9, 20)
        item = ActionItem(
            "Done",
            "owner",
            date(2026, 9, 19),
            ActionType.SAFETY_GUARDRAIL,
            done=True,
        )
        self.assertIsNone(highest_severity([item], today))

    def test_highest_severity_active_not_overdue_is_sev2(self) -> None:
        today = date(2026, 9, 20)
        item = ActionItem("Open", "owner", date(2026, 9, 30), ActionType.PROCESS_CHANGE)
        self.assertEqual(highest_severity([item], today), Severity.SEV2)

    def test_urgent_type_not_overdue_but_active_is_sev2(self) -> None:
        today = date(2026, 9, 20)
        item = ActionItem("Urgent", "owner", date(2026, 9, 30), ActionType.IMMEDIATE_FIX)
        self.assertEqual(highest_severity([item], today), Severity.SEV2)

    def test_chinese_fields_are_valid(self) -> None:
        item = ActionItem("增加限流", "负责人", date(2026, 9, 30), ActionType.SAFETY_GUARDRAIL)
        self.assertTrue(item.has_required_fields())
