from __future__ import annotations

import unittest

from .agent_top_labs_l1_multi_turn_state import MultiTurnState, TurnMessage


class MultiTurnStateTest(unittest.TestCase):
    def test_recent_messages_without_summary(self) -> None:
        state = MultiTurnState(summary_limit=2)
        state.add(TurnMessage("user", "hello"))
        state.add(TurnMessage("assistant", "hi"))
        self.assertFalse(state.needs_summary())
        self.assertEqual(state.build_prompt_context(), ["user: hello", "assistant: hi"])

    def test_older_messages_become_summary(self) -> None:
        state = MultiTurnState(summary_limit=1)
        state.add(TurnMessage("user", "first"))
        state.add(TurnMessage("assistant", "second"))
        state.add(TurnMessage("user", "third"))
        self.assertTrue(state.needs_summary())
        self.assertEqual(
            state.build_prompt_context(),
            ["summary_of_2_older_messages", "user: third"],
        )

    def test_zero_count_returns_empty(self) -> None:
        state = MultiTurnState()
        state.add(TurnMessage("user", "hello"))
        self.assertEqual(state.recent_messages(0), state.messages)

    def test_count_larger_than_history_returns_all(self) -> None:
        state = MultiTurnState()
        state.add(TurnMessage("user", "a"))
        state.add(TurnMessage("assistant", "b"))
        self.assertEqual(state.recent_messages(10), state.messages)

    def test_build_prompt_context_orders_recent_first(self) -> None:
        state = MultiTurnState(summary_limit=2)
        state.add(TurnMessage("user", "first"))
        state.add(TurnMessage("user", "second"))
        state.add(TurnMessage("assistant", "third"))
        self.assertEqual(
            state.build_prompt_context(),
            ["summary_of_1_older_messages", "user: second", "assistant: third"],
        )

    def test_chinese_content_preserved_in_context(self) -> None:
        state = MultiTurnState(summary_limit=1)
        state.add(TurnMessage("user", "你好"))
        self.assertEqual(state.build_prompt_context(), ["user: 你好"])

    def test_needs_summary_boundary_exactly_at_limit(self) -> None:
        state = MultiTurnState(summary_limit=2)
        state.add(TurnMessage("user", "a"))
        state.add(TurnMessage("assistant", "b"))
        self.assertFalse(state.needs_summary())
