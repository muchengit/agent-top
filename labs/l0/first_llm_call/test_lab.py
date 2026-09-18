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

    def test_default_arguments_work(self) -> None:
        response = first_llm_call()
        self.assertIn("[You are helpful.]", response)
        self.assertIn("Explain agents simply.", response)

    def test_empty_system_prompt_still_formats(self) -> None:
        response = first_llm_call(system_prompt="", prompt="hi")
        self.assertTrue(response.startswith("[] I received"))
        self.assertIn("hi", response)

    def test_multiline_prompt_counts_lines_as_words(self) -> None:
        response = first_llm_call(prompt="one\ntwo\nthree")
        self.assertIn("3 prompt tokens", response)

    def test_punctuation_and_emoji_preserved(self) -> None:
        response = first_llm_call(prompt="hello, world! 🎉")
        self.assertIn("hello, world! 🎉", response)

    def test_numeric_prompt_counts_words(self) -> None:
        response = first_llm_call(prompt="42 100")
        self.assertIn("2 prompt tokens", response)

    def test_mixed_language_word_count(self) -> None:
        response = first_llm_call(prompt="Agent 框架 1 2")
        self.assertIn("4 prompt tokens", response)

    def test_response_has_system_prompt_prefix(self) -> None:
        response = first_llm_call(system_prompt="You are terse.", prompt="go")
        self.assertTrue(response.startswith("[You are terse.]"))

    def test_deterministic_same_input_same_output(self) -> None:
        first = first_llm_call(system_prompt="You are kind.", prompt="hello agent")
        second = first_llm_call(system_prompt="You are kind.", prompt="hello agent")
        self.assertEqual(first, second)

    def test_prompt_with_tabs_counts_words(self) -> None:
        response = first_llm_call(prompt="a\tb\tc")
        self.assertIn("3 prompt tokens", response)

    def test_long_prompt_preserved_fully(self) -> None:
        prompt = "word " * 50
        response = first_llm_call(prompt=prompt)
        self.assertIn(prompt.rstrip(), response)
        self.assertIn("50 prompt tokens", response)
