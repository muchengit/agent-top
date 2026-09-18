from __future__ import annotations

import unittest

from .agent_top_labs_l1_minimal_react_agent import add_tool, run_react_agent


class MinimalReactAgentTest(unittest.TestCase):
    def test_add_tool(self) -> None:
        self.assertEqual(add_tool("2+3"), "2+3=5")

    def test_react_agent_answers_with_observation(self) -> None:
        result = run_react_agent("5", {"call_tool": add_tool})
        self.assertEqual(result.observations, ["2+3=5"])
        self.assertEqual(result.steps[-1], "ANSWER: Result: 2+3=5")

    def test_non_numeric_goal_does_not_loop(self) -> None:
        result = run_react_agent("hello", {"call_tool": add_tool})
        self.assertEqual(result.steps, ["ANSWER: I need a numeric goal, but got: hello"])

    def test_empty_goal_is_not_numeric(self) -> None:
        result = run_react_agent("", {"call_tool": add_tool})
        self.assertEqual(result.steps, ["ANSWER: I need a numeric goal, but got: "])

    def test_missing_tool_stops_without_looping(self) -> None:
        result = run_react_agent("5", {})
        self.assertEqual(result.steps, ["STOP: missing tool call_tool"])

    def test_max_steps_zero_stops_immediately(self) -> None:
        result = run_react_agent("5", {"call_tool": add_tool}, max_steps=0)
        self.assertEqual(result.steps, ["STOP: max_steps exceeded"])
        self.assertEqual(result.observations, [])

    def test_observations_accumulate_across_steps(self) -> None:
        def echo_tool(goal: str) -> str:
            return f"obs:{goal}"

        result = run_react_agent("5", {"call_tool": echo_tool}, max_steps=1)
        self.assertEqual(result.observations, ["obs:5"])

    def test_unicode_goal_is_not_numeric(self) -> None:
        result = run_react_agent("五", {"call_tool": add_tool})
        self.assertEqual(result.steps, ["ANSWER: I need a numeric goal, but got: 五"])
