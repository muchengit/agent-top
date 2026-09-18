from __future__ import annotations

import json
import unittest

from .agent_top_labs_l2_single_agent_mcp import Guardrail, ToolServer, run_single_agent


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
        server = ToolServer()
        with self.assertRaises(ValueError):
            server.call_tool("missing", {"query": "x"})

    def test_list_tools_exposes_search_docs(self) -> None:
        self.assertEqual(ToolServer().list_tools(), ["search_docs"])

    def test_call_tool_missing_query_key_raises(self) -> None:
        server = ToolServer()
        with self.assertRaises(ValueError):
            server.call_tool("search_docs", {})

    def test_call_tool_trims_query_whitespace(self) -> None:
        server = ToolServer()
        result = server.call_tool("search_docs", {"query": "  spaced  "})
        self.assertEqual(
            json.loads(result)["hits"],
            ["synthetic result for spaced"],
        )

    def test_call_tool_empty_query_raises(self) -> None:
        server = ToolServer()
        with self.assertRaises(ValueError):
            server.call_tool("search_docs", {"query": "   "})

    def test_call_tool_returns_json_with_escaped_unicode(self) -> None:
        server = ToolServer()
        result = server.call_tool("search_docs", {"query": "中文"})
        parsed = json.loads(result)
        self.assertEqual(parsed["hits"], ["synthetic result for 中文"])

    def test_guardrail_allows_plain_query(self) -> None:
        self.assertTrue(Guardrail().allow("python memory"))

    def test_guardrail_rejects_whitespace_only(self) -> None:
        self.assertFalse(Guardrail().allow("\t\n  "))

    def test_guardrail_boundary_200_allowed(self) -> None:
        self.assertTrue(Guardrail().allow("x" * 200))

    def test_guardrail_over_200_rejected(self) -> None:
        self.assertFalse(Guardrail().allow("x" * 201))

    def test_guardrail_rejects_empty_string(self) -> None:
        self.assertFalse(Guardrail().allow(""))

    def test_run_single_agent_returns_json_result(self) -> None:
        response = run_single_agent("memory")
        self.assertTrue(response["ok"])
        parsed = json.loads(str(response["result"]))
        self.assertEqual(parsed["hits"][0], "synthetic result for memory")

    def test_run_single_agent_non_dict_result_never_occurs(self) -> None:
        response = run_single_agent("query")
        self.assertIsInstance(response["result"], str)

    def test_rejected_query_with_no_reason_breakage(self) -> None:
        response = run_single_agent("x" * 500)
        self.assertEqual(response, {"ok": False, "reason": "guardrail rejected query"})

    def test_run_single_agent_preserves_emoji_query(self) -> None:
        response = run_single_agent("规则 🚀")
        self.assertTrue(response["ok"])
        hits = json.loads(str(response["result"]))["hits"]
        self.assertEqual(hits, ["synthetic result for 规则 🚀"])
