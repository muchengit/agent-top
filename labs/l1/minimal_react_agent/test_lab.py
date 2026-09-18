from __future__ import annotations

import unittest

from .agent_top_labs_l1_minimal_react_agent import add_tool, is_numeric_goal, run_react_agent


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

    def test_negative_number_is_numeric(self) -> None:
        result = run_react_agent("-7", {"call_tool": add_tool})
        self.assertIn("OBSERVE: 2+3=5", result.steps)

    def test_decimal_number_is_numeric(self) -> None:
        result = run_react_agent("3.14", {"call_tool": add_tool})
        self.assertIn("OBSERVE: 2+3=5", result.steps)

    def test_leading_plus_is_numeric(self) -> None:
        result = run_react_agent("+9", {"call_tool": add_tool})
        self.assertIn("OBSERVE: 2+3=5", result.steps)

    def test_multi_step_loop_continues_until_answer(self) -> None:
        def first_tool(goal: str) -> str:
            return "step-one"

        result = run_react_agent("1", {"call_tool": first_tool})
        self.assertIn("OBSERVE: step-one", result.steps)
        self.assertEqual(result.steps[-1], "ANSWER: Result: step-one")

    def test_observation_echoes_goal_with_multiple_tools(self) -> None:
        def echo_a(goal: str) -> str:
            return f"a:{goal}"

        result = run_react_agent("2", {"call_tool": echo_a, "other": echo_a})
        self.assertEqual(result.observations, ["a:2"])

    def test_plan_next_action_none_goal_empty(self) -> None:
        from .agent_top_labs_l1_minimal_react_agent import plan_next_action

        action = plan_next_action("", ["obs"])
        self.assertIsNotNone(action)
        self.assertEqual(action[0], "answer")

    def test_single_observation_fed_to_answer(self) -> None:
        class ChainedTool:
            def __init__(self) -> None:
                self.calls = 0

            def __call__(self, goal: str) -> str:
                self.calls += 1
                return f"chained-{self.calls}"

        tool = ChainedTool()
        result = run_react_agent("5", {"call_tool": tool}, max_steps=3)
        self.assertEqual(result.observations, ["chained-1"])
        self.assertTrue(result.steps[-1].startswith("ANSWER:"))

    def test_plan_next_action_returns_answer_with_latest_observation(self) -> None:
        from .agent_top_labs_l1_minimal_react_agent import plan_next_action

        action = plan_next_action("5", ["obs"])
        self.assertIsNotNone(action)
        self.assertEqual(action, ("answer", "Result: obs"))

    def test_is_numeric_goal_rejects_whitespace(self) -> None:
        self.assertFalse(is_numeric_goal("   "))

    def test_is_numeric_goal_rejects_nan_and_infinity(self) -> None:
        self.assertFalse(is_numeric_goal("nan"))
        self.assertFalse(is_numeric_goal("inf"))
        self.assertFalse(is_numeric_goal("-inf"))

    def test_is_numeric_goal_accepts_finite_decimals(self) -> None:
        self.assertTrue(is_numeric_goal("0.5"))
        self.assertTrue(is_numeric_goal("-1e3"))
