"""Deterministic tests for the MCP tool selection lab."""

from __future__ import annotations

import unittest

from .agent_top_labs_l2_mcp_tool_selection import (
    ArgSpec,
    RiskLevel,
    ToolSpec,
    select_tool,
)


def _example_tools() -> list[ToolSpec]:
    return [
        ToolSpec(
            name="get_weather",
            description="Return current weather for a city.",
            args=(ArgSpec("city"),),
            keywords=("weather", "temperature", "forecast"),
        ),
        ToolSpec(
            name="search_docs",
            description="Search internal documentation.",
            args=(
                ArgSpec("query", required=True),
                ArgSpec("max_results", kind="integer"),
            ),
            keywords=("docs", "documentation", "search"),
        ),
        ToolSpec(
            name="send_email",
            description="Send an email to a recipient.",
            args=(ArgSpec("to", required=True), ArgSpec("subject", required=True)),
            risk=RiskLevel.MEDIUM,
            keywords=("email", "send mail", "message"),
        ),
        ToolSpec(
            name="delete_account",
            description="Permanently delete a user account.",
            risk=RiskLevel.HIGH,
            keywords=("delete account", "remove account"),
        ),
    ]


class SelectToolTest(unittest.TestCase):
    def test_selects_correct_tool(self) -> None:
        result = select_tool("What is the weather in Shanghai?", _example_tools())
        self.assertTrue(result.ok)
        self.assertIsNotNone(result.tool)
        self.assertEqual(result.tool.name, "get_weather")  # type: ignore[union-attr]

    def test_no_matching_tool(self) -> None:
        result = select_tool("Please book a flight to Tokyo.", _example_tools())
        self.assertFalse(result.ok)
        self.assertEqual(result.reason, "no matching tool")

    def test_missing_required_argument_is_rejected(self) -> None:
        result = select_tool(
            "send_email(to=, subject=hello)", _example_tools()
        )
        self.assertFalse(result.ok)
        self.assertEqual(result.tool.name, "send_email")  # type: ignore[union-attr]
        self.assertIn("missing required argument", result.reason)

    def test_medium_risk_requires_confirmation(self) -> None:
        result = select_tool("Please send an email to Alice.", _example_tools())
        self.assertFalse(result.ok)
        self.assertTrue(result.needs_confirmation)
        self.assertEqual(result.reason, "requires confirmation")

    def test_high_risk_is_blocked(self) -> None:
        result = select_tool("Please delete account for alice.", _example_tools())
        self.assertFalse(result.ok)
        self.assertEqual(result.reason, "blocked by safety policy")

    def test_ambiguous_intent_is_rejected(self) -> None:
        tools = [
            ToolSpec(
                name="get_weather",
                description="Current weather.",
                keywords=("weather",),
            ),
            ToolSpec(
                name="weather_alerts",
                description="Weather alerts.",
                keywords=("weather",),
            ),
        ]
        result = select_tool("Tell me about the weather.", tools)
        self.assertFalse(result.ok)
        self.assertEqual(result.reason, "ambiguous intent: get_weather, weather_alerts")

    def test_explicit_confirmation_allows_medium_risk(self) -> None:
        result = select_tool(
            "send_email(to=alice@example.com, subject=hi)", _example_tools()
        )
        self.assertTrue(result.ok)
        self.assertEqual(result.tool.name, "send_email")  # type: ignore[union-attr]
        self.assertEqual(result.args["to"], "alice@example.com")
        self.assertEqual(result.args["subject"], "hi")

    def test_unknown_argument_is_rejected(self) -> None:
        result = select_tool(
            "get_weather(city=beijing, unit=celsius)", _example_tools()
        )
        self.assertFalse(result.ok)
        self.assertIn("unknown arguments", result.reason)

    def test_non_integer_argument_is_rejected(self) -> None:
        result = select_tool(
            "search_docs(query=agents, max_results=abc)", _example_tools()
        )
        self.assertFalse(result.ok)
        self.assertIn("must be an integer", result.reason)

    def test_empty_request_is_rejected(self) -> None:
        result = select_tool("   ", _example_tools())
        self.assertFalse(result.ok)
        self.assertEqual(result.reason, "empty request")


if __name__ == "__main__":
    unittest.main()
