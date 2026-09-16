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
