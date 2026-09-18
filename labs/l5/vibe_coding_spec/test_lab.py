from __future__ import annotations

import unittest

from .agent_top_labs_l5_vibe_coding_spec import (
    acceptance_command_present,
    check_spec,
    ready_to_prompt,
)


class VibeCodingSpecTest(unittest.TestCase):
    def test_complete_spec_is_ready(self) -> None:
        spec = check_spec(
            goal="Add a search endpoint",
            interface="GET /search?q=... returns 10 results",
            acceptance="pytest tests/api/test_search.py passes",
        )
        self.assertTrue(ready_to_prompt(spec))
        self.assertEqual(spec.missing, ())

    def test_missing_acceptance_is_not_ready(self) -> None:
        spec = check_spec(
            goal="Improve the agent",
            interface="",
            acceptance="",
        )
        self.assertFalse(ready_to_prompt(spec))
        self.assertIn("interface", spec.missing)
        self.assertIn("acceptance", spec.missing)

    def test_blank_spec_fails_closed(self) -> None:
        spec = check_spec(goal="", interface="", acceptance="")
        self.assertFalse(ready_to_prompt(spec))
        self.assertEqual(len(spec.missing), 3)

    def test_one_sentence_joins_three_fields(self) -> None:
        spec = check_spec(
            goal="Add search.",
            interface="Returns 10 results.",
            acceptance="pytest passes.",
        )
        sentence = spec.one_sentence()
        self.assertIn("Add search.", sentence)
        self.assertIn("pytest passes.", sentence)

    def test_acceptance_command_detected(self) -> None:
        spec = check_spec(
            goal="Add search endpoint",
            interface="GET /search",
            acceptance="Run: python3 -m unittest labs.l5.vibe_coding_spec.test_lab",
        )
        self.assertTrue(
            acceptance_command_present(spec, ("python3 -m unittest", "pytest"))
        )
        self.assertFalse(
            acceptance_command_present(spec, ("go test", "npm test"))
        )

    def test_whitespace_only_fields_fail_closed(self) -> None:
        spec = check_spec(goal="   ", interface="\t\n", acceptance=" ")
        self.assertFalse(ready_to_prompt(spec))
        self.assertEqual(len(spec.missing), 3)

    def test_only_goal_set_is_not_ready(self) -> None:
        spec = check_spec(goal="Add a search endpoint", interface="", acceptance="")
        self.assertFalse(ready_to_prompt(spec))
        self.assertEqual(spec.missing, ("interface", "acceptance"))
        self.assertEqual(spec.one_sentence(), "Add a search endpoint")

    def test_goal_and_interface_without_acceptance(self) -> None:
        spec = check_spec(
            goal="Add a search endpoint",
            interface="GET /search?q=... returns 10 results",
            acceptance="",
        )
        self.assertFalse(ready_to_prompt(spec))
        self.assertEqual(spec.missing, ("acceptance",))
        sentence = spec.one_sentence()
        self.assertIn("Add a search endpoint", sentence)
        self.assertIn("GET /search?q=... returns 10 results", sentence)

    def test_vague_acceptance_is_not_a_command(self) -> None:
        spec = check_spec(
            goal="Add a search endpoint",
            interface="GET /search",
            acceptance="it should work",
        )
        self.assertTrue(ready_to_prompt(spec))
        self.assertFalse(
            acceptance_command_present(spec, ("python3 -m unittest", "pytest", "npm test"))
        )

    def test_minimal_valid_spec_is_ready(self) -> None:
        spec = check_spec(
            goal="Add search",
            interface="GET /search",
            acceptance="pytest passes",
        )
        self.assertTrue(ready_to_prompt(spec))
        self.assertEqual(spec.missing, ())
        self.assertTrue(
            acceptance_command_present(spec, ("pytest",))
        )

    def test_chinese_fields_are_handled(self) -> None:
        spec = check_spec(
            goal="添加搜索接口",
            interface="GET /search 返回最多 10 条结果",
            acceptance="运行 pytest 通过",
        )
        self.assertTrue(ready_to_prompt(spec))
        self.assertEqual(spec.missing, ())
        self.assertTrue(spec.one_sentence().startswith("添加搜索接口"))
        self.assertTrue(
            acceptance_command_present(spec, ("pytest", "python3 -m unittest"))
        )

    def test_one_sentence_normalizes_whitespace(self) -> None:
        spec = check_spec(
            goal="  Add search. ",
            interface="\tGET /search.\n",
            acceptance="  pytest passes.  ",
        )
        self.assertEqual(spec.one_sentence(), "Add search. GET /search. pytest passes.")


if __name__ == "__main__":
    unittest.main()
