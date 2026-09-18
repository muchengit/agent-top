from __future__ import annotations

import unittest

from .agent_top_labs_l1_guardrail_helpers import (
    RiskLevel,
    ToolOutcome,
    ToolPolicy,
    ToolRequest,
    evaluate_tool_request,
)


class GuardrailHelpersTest(unittest.TestCase):
    def test_read_only_tool_is_allowed_for_authorized_role(self) -> None:
        policy = ToolPolicy("search_docs", RiskLevel.READ_ONLY, ("agent",))
        request = ToolRequest("search_docs", "agent")
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.ALLOWED)

    def test_unauthorized_role_is_blocked(self) -> None:
        policy = ToolPolicy("search_docs", RiskLevel.READ_ONLY, ("agent",))
        request = ToolRequest("search_docs", "visitor")
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.BLOCKED)

    def test_destructive_tool_requires_confirmation(self) -> None:
        policy = ToolPolicy("delete_ticket", RiskLevel.DESTRUCTIVE, ("agent",))
        request = ToolRequest("delete_ticket", "agent")
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.CONFIRMATION_REQUIRED)

    def test_destructive_tool_allowed_after_confirmation(self) -> None:
        policy = ToolPolicy("delete_ticket", RiskLevel.DESTRUCTIVE, ("agent",))
        request = ToolRequest("delete_ticket", "agent", user_confirmed=True)
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.ALLOWED)

    def test_write_tool_without_confirmation_flag_is_allowed(self) -> None:
        policy = ToolPolicy("save_note", RiskLevel.WRITE, ("agent",))
        request = ToolRequest("save_note", "agent")
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.ALLOWED)

    def test_requires_confirmation_policy_blocks_without_user_ok(self) -> None:
        policy = ToolPolicy(
            "update_profile",
            RiskLevel.WRITE,
            ("agent",),
            requires_confirmation=True,
        )
        request = ToolRequest("update_profile", "agent")
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.CONFIRMATION_REQUIRED)

    def test_tool_name_mismatch_is_blocked(self) -> None:
        policy = ToolPolicy("search_docs", RiskLevel.READ_ONLY, ("agent",))
        request = ToolRequest("delete_ticket", "agent", user_confirmed=True)
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.BLOCKED)

    def test_empty_allowed_roles_blocks_everyone(self) -> None:
        policy = ToolPolicy("search_docs", RiskLevel.READ_ONLY, ())
        request = ToolRequest("search_docs", "agent", user_confirmed=True)
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.BLOCKED)

    def test_multi_role_allowlist(self) -> None:
        policy = ToolPolicy("search_docs", RiskLevel.READ_ONLY, ("agent", "human"))
        request = ToolRequest("search_docs", "human")
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.ALLOWED)
