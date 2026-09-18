from __future__ import annotations

import unittest

from .agent_top_labs_l0_first_llm_call import first_llm_call


class FirstLlmCallTest(unittest.TestCase):
    def test_first_call_returns_prompt_and_role(self) -> None:
        response = first_llm_call(prompt="hello world")
        self.assertIn("You are helpful.", response)
        self.assertIn("2 prompt tokens", response)

    def test_empty_prompt_is_handled(self) -> None:
        self.assertEqual(first_llm_call(prompt=""), "No user prompt provided.")

    def test_custom_system_prompt_appears_in_response(self) -> None:
        response = first_llm_call(system_prompt="You are strict.", prompt="hello")
        self.assertIn("[You are strict.]", response)

    def test_token_count_is_word_based(self) -> None:
        response = first_llm_call(prompt="one two three")
        self.assertIn("3 prompt tokens", response)

    def test_whitespace_only_prompt_counts_as_tokens(self) -> None:
        response = first_llm_call(prompt="   ")
        self.assertIn("0 prompt tokens", response)

    def test_chinese_prompt_is_preserved(self) -> None:
        response = first_llm_call(prompt="解释一下 Agent")
        self.assertIn("解释一下 Agent", response)
