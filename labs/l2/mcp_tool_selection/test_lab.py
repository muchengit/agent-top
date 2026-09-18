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

    def test_arg_spec_missing_required_raises(self) -> None:
        spec = ArgSpec("city", required=True)
        with self.assertRaises(ValueError):
            spec.validate(None)

    def test_arg_spec_optional_none_is_ok(self) -> None:
        spec = ArgSpec("city")
        spec.validate(None)

    def test_arg_spec_empty_string_raises(self) -> None:
        spec = ArgSpec("query", required=True)
        with self.assertRaises(ValueError):
            spec.validate("   ")

    def test_arg_spec_integer_kind(self) -> None:
        spec = ArgSpec("count", kind="integer")
        spec.validate(3)
        with self.assertRaises(ValueError):
            spec.validate("3")

    def test_arg_spec_integer_rejects_bool(self) -> None:
        spec = ArgSpec("count", kind="integer")
        with self.assertRaises(ValueError):
            spec.validate(True)

    def test_arg_spec_integer_negative_rejected_with_choices(self) -> None:
        spec = ArgSpec("count", kind="integer", choices=("min",))
        with self.assertRaises(ValueError):
            spec.validate(-2)

    def test_arg_spec_enum_validation(self) -> None:
        spec = ArgSpec("mode", kind="enum", choices=("fast", "safe"))
        spec.validate("fast")
        with self.assertRaises(ValueError):
            spec.validate("slow")

    def test_arg_spec_array_kind(self) -> None:
        spec = ArgSpec("ids", kind="array")
        spec.validate(["a", "b"])
        with self.assertRaises(ValueError):
            spec.validate(["a", 1])
        with self.assertRaises(ValueError):
            spec.validate("not-a-list")

    def test_arg_spec_overlong_string_rejected(self) -> None:
        spec = ArgSpec("text")
        with self.assertRaises(ValueError):
            spec.validate("x" * 1001)

    def test_safety_keyword_delete_blocks_even_with_matching_tool(self) -> None:
        result = select_tool("please delete account", _example_tools())
        self.assertEqual(result.reason, "blocked by safety policy")

    def test_safety_keyword_reset_blocks(self) -> None:
        result = select_tool("reset my password please", _example_tools())
        self.assertEqual(result.reason, "blocked by safety policy")

    def test_matches_is_case_insensitive(self) -> None:
        tool = ToolSpec(
            name="get_weather",
            description="Weather.",
            keywords=("weather",),
        )
        self.assertTrue(tool.matches("What is the WEATHER?"))

    def test_matches_partial_keyword_substring(self) -> None:
        tool = ToolSpec(
            name="search_docs",
            description="Search docs.",
            keywords=("docs",),
        )
        self.assertTrue(tool.matches("documentation is in my docs folder"))

    def test_keyword_match_with_missing_required_arg_fails(self) -> None:
        result = select_tool("search docs about agents", _example_tools())
        self.assertFalse(result.ok)
        self.assertEqual(result.tool.name, "search_docs")  # type: ignore[union-attr]
        self.assertIn("missing required argument", result.reason)

    def test_no_keyword_tool_never_matches(self) -> None:
        tool = ToolSpec(
            name="blob",
            description="No keywords.",
        )
        self.assertFalse(tool.matches("anything"))

    def test_needs_confirmation_false_for_low_risk(self) -> None:
        result = select_tool("What is the weather?", _example_tools())
        self.assertTrue(result.ok)
        self.assertFalse(result.needs_confirmation)

    def test_positive_int_string_converted_to_int(self) -> None:
        result = select_tool(
            "search_docs(query=agents, max_results=5)", _example_tools()
        )
        self.assertTrue(result.ok)
        self.assertEqual(result.args["max_results"], 5)
        self.assertIsInstance(result.args["max_results"], int)


if __name__ == "__main__":
    unittest.main()
