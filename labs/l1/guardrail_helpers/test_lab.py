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

