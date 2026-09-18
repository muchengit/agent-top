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
