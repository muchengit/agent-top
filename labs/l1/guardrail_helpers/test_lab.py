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

    def test_write_role_with_confirmation_required_and_confirmed(self) -> None:
        policy = ToolPolicy(
            "update_profile",
            RiskLevel.WRITE,
            ("agent",),
            requires_confirmation=True,
        )
        request = ToolRequest("update_profile", "agent", user_confirmed=True)
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.ALLOWED)

    def test_unauthorized_role_cannot_bypass_with_confirmation(self) -> None:
        policy = ToolPolicy("delete_ticket", RiskLevel.DESTRUCTIVE, ("agent",))
        request = ToolRequest("delete_ticket", "visitor", user_confirmed=True)
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.BLOCKED)

    def test_tool_name_mismatch_takes_priority_over_confirmation(self) -> None:
        policy = ToolPolicy("delete_ticket", RiskLevel.DESTRUCTIVE, ("agent",))
        request = ToolRequest("delete_other", "agent", user_confirmed=True)
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.BLOCKED)

    def test_destructive_with_confirmation_flag_needs_single_confirmation(self) -> None:
        policy = ToolPolicy(
            "purge_data",
            RiskLevel.DESTRUCTIVE,
            ("admin",),
            requires_confirmation=True,
        )
        request = ToolRequest("purge_data", "admin")
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.CONFIRMATION_REQUIRED)
        confirmed = ToolRequest("purge_data", "admin", user_confirmed=True)
        self.assertEqual(evaluate_tool_request(policy, confirmed), ToolOutcome.ALLOWED)

    def test_case_sensitive_role_matching(self) -> None:
        policy = ToolPolicy("search_docs", RiskLevel.READ_ONLY, ("Agent",))
        request = ToolRequest("search_docs", "agent")
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.BLOCKED)

    def test_allowed_roles_any_position_in_tuple(self) -> None:
        policy = ToolPolicy("search_docs", RiskLevel.READ_ONLY, ("human", "agent", "reviewer"))
        request = ToolRequest("search_docs", "reviewer")
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.ALLOWED)

    def test_read_only_never_requires_confirmation(self) -> None:
        policy = ToolPolicy("read_audit", RiskLevel.READ_ONLY, ("auditor",))
        request = ToolRequest("read_audit", "auditor")
        self.assertEqual(evaluate_tool_request(policy, request), ToolOutcome.ALLOWED)
