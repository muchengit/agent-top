from __future__ import annotations

import unittest

from .agent_top_labs_l3_multi_round_research_discussion import (
    CandidateSource,
    DiscussionStatus,
    ResearchState,
    evaluate_discussion,
    select_sources,
)


class MultiRoundResearchDiscussionTest(unittest.TestCase):
    def test_selects_evidence_sources_with_highest_priority(self) -> None:
        sources = [
            CandidateSource("stale-doc", 0.9, 0.2, 0.9, True),
            CandidateSource("fresh-doc", 0.8, 0.9, 0.9, True),
            CandidateSource("irrelevant", 0.9, 0.9, 0.9, False),
        ]
        selected = select_sources(sources, max_sources=2)
        self.assertEqual([source.name for source in selected], ["fresh-doc", "stale-doc"])

    def test_ready_to_answer_when_evidence_is_fresh(self) -> None:
        state = ResearchState("how do agents route tools?", ("fresh-doc",), 2, True)
        selected = [CandidateSource("fresh-doc", 0.8, 0.9, 0.9, True)]
        self.assertEqual(evaluate_discussion(state, selected), DiscussionStatus.READY_TO_ANSWER)

    def test_needs_more_evidence_when_selected_sources_are_stale(self) -> None:
        state = ResearchState("how do agents route tools?", ("stale-doc",), 2, True)
        selected = [CandidateSource("stale-doc", 0.9, 0.4, 0.9, True)]
        self.assertEqual(evaluate_discussion(state, selected), DiscussionStatus.NEEDS_MORE_EVIDENCE)

    def test_asks_user_when_question_is_empty(self) -> None:
        state = ResearchState("   ", (), 0, False)
        self.assertEqual(evaluate_discussion(state, []), DiscussionStatus.SHOULD_ASK_USER)
