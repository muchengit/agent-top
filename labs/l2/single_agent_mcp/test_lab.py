from __future__ import annotations

import json
import unittest

from .agent_top_labs_l2_single_agent_mcp import run_single_agent


class SingleAgentMcpTest(unittest.TestCase):
    def test_tool_boundary_returns_result(self) -> None:
        response = run_single_agent("agent memory")
        self.assertTrue(response["ok"])
        hits = json.loads(str(response["result"]))["hits"]
        self.assertEqual(hits, ["synthetic result for agent memory"])

    def test_guardrail_rejects_empty_query(self) -> None:
        response = run_single_agent("   ")
        self.assertFalse(response["ok"])

    def test_guardrail_rejects_overlong_query(self) -> None:
        response = run_single_agent("x" * 201)
        self.assertFalse(response["ok"])
        self.assertEqual(response["reason"], "guardrail rejected query")

    def test_guardrail_allows_200_char_query(self) -> None:
        response = run_single_agent("x" * 200)
        self.assertTrue(response["ok"])

    def test_query_is_trimmed_before_call(self) -> None:
        response = run_single_agent("  agent memory  ")
        self.assertTrue(response["ok"])
        self.assertIn("synthetic result for agent memory", str(response["result"]))

    def test_chinese_query_is_supported(self) -> None:
        response = run_single_agent("检索 记忆")
        self.assertTrue(response["ok"])
        hits = json.loads(str(response["result"]))["hits"]
        self.assertEqual(hits, ["synthetic result for 检索 记忆"])

    def test_unknown_tool_raises_value_error(self) -> None:
        from .agent_top_labs_l2_single_agent_mcp import ToolServer

        server = ToolServer()
        with self.assertRaises(ValueError):
            server.call_tool("missing", {"query": "x"})
