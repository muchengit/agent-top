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

    def test_needs_summary_true_when_exceeding_limit(self) -> None:
        state = MultiTurnState(summary_limit=2)
        state.add(TurnMessage("user", "a"))
        state.add(TurnMessage("assistant", "b"))
        state.add(TurnMessage("user", "c"))
        self.assertTrue(state.needs_summary())

    def test_build_prompt_context_with_no_messages(self) -> None:
        state = MultiTurnState(summary_limit=2)
        self.assertEqual(state.build_prompt_context(), [])

    def test_empty_content_preserved(self) -> None:
        state = MultiTurnState(summary_limit=1)
        state.add(TurnMessage("assistant", ""))
        self.assertEqual(state.build_prompt_context(), ["assistant: "])

    def test_large_summary_limit_never_summarizes(self) -> None:
        state = MultiTurnState(summary_limit=100)
        for index in range(5):
            state.add(TurnMessage("user", f"m{index}"))
        self.assertFalse(state.needs_summary())
        context = state.build_prompt_context()
        self.assertEqual(len(context), 5)

    def test_summary_count_scales_with_excess(self) -> None:
        state = MultiTurnState(summary_limit=1)
        for index in range(4):
            state.add(TurnMessage("user", f"m{index}"))
        context = state.build_prompt_context()
        self.assertEqual(context[0], "summary_of_3_older_messages")

    def test_mixed_roles_in_recent_context(self) -> None:
        state = MultiTurnState(summary_limit=3)
        state.add(TurnMessage("user", "u1"))
        state.add(TurnMessage("assistant", "a1"))
        state.add(TurnMessage("tool", "t1"))
        state.add(TurnMessage("user", "u2"))
        context = state.build_prompt_context()
        self.assertEqual(context, ["summary_of_1_older_messages", "assistant: a1", "tool: t1", "user: u2"])

    def test_unicode_content_preserved(self) -> None:
        state = MultiTurnState(summary_limit=1)
        state.add(TurnMessage("user", "🚀 你好 Agent"))
        self.assertEqual(state.build_prompt_context(), ["user: 🚀 你好 Agent"])

    def test_add_appends_in_order(self) -> None:
        state = MultiTurnState()
        state.add(TurnMessage("user", "first"))
        state.add(TurnMessage("assistant", "second"))
        self.assertEqual(state.messages[0].content, "first")
        self.assertEqual(state.messages[1].content, "second")

    def test_recent_messages_negative_count_returns_last_slice(self) -> None:
        state = MultiTurnState()
        state.add(TurnMessage("user", "a"))
        state.add(TurnMessage("user", "b"))
        self.assertEqual(
            state.recent_messages(-1),
            [TurnMessage("user", "b")],
        )
