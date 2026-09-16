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
