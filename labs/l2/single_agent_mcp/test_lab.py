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
