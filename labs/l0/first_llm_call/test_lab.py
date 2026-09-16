import unittest

from .agent_top_labs_l0_first_llm_call import first_llm_call


class FirstLlmCallTest(unittest.TestCase):
    def test_first_call_returns_prompt_and_role(self) -> None:
        response = first_llm_call(prompt="hello world")
        self.assertIn("You are helpful.", response)
        self.assertIn("2 prompt tokens", response)

    def test_empty_prompt_is_handled(self) -> None:
        self.assertEqual(first_llm_call(prompt=""), "No user prompt provided.")
