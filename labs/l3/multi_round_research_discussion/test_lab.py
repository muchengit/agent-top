from __future__ import annotations

import unittest

from .agent_top_labs_l3_multi_round_research_discussion import (
    CandidateSource,
    DiscussionStatus,
    ResearchState,
    candidate_priority,
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

    def test_asks_user_when_clarification_needed_and_not_confirmed(self) -> None:
        state = ResearchState("how do agents route tools?", (), 1, False)
        self.assertEqual(
            evaluate_discussion(state, [], requires_clarification=True),
            DiscussionStatus.SHOULD_ASK_USER,
        )

    def test_proceeds_when_clarified(self) -> None:
        state = ResearchState("how do agents route tools?", ("fresh-doc",), 1, True)
        selected = [CandidateSource("fresh-doc", 0.8, 0.9, 0.9, True)]
        self.assertEqual(
            evaluate_discussion(state, selected, requires_clarification=True),
            DiscussionStatus.READY_TO_ANSWER,
        )

    def test_refuses_when_no_evidence(self) -> None:
        state = ResearchState("how do agents route tools?", (), 2, True)
        selected = [CandidateSource("irrelevant", 0.9, 0.9, 0.9, False)]
        self.assertEqual(evaluate_discussion(state, selected), DiscussionStatus.SHOULD_REFUSE)

    def test_freshness_boundary_exactly_half_is_ready(self) -> None:
        state = ResearchState("how do agents route tools?", ("boundary",), 1, True)
        selected = [CandidateSource("boundary", 0.8, 0.5, 0.9, True)]
        self.assertEqual(evaluate_discussion(state, selected), DiscussionStatus.READY_TO_ANSWER)

    def test_mixed_fresh_and_stale_blocks_answer(self) -> None:
        state = ResearchState("how do agents route tools?", ("fresh-doc", "stale-doc"), 2, True)
        selected = [
            CandidateSource("fresh-doc", 0.8, 0.9, 0.9, True),
            CandidateSource("stale-doc", 0.9, 0.4, 0.9, True),
        ]
        self.assertEqual(
            evaluate_discussion(state, selected),
            DiscussionStatus.NEEDS_MORE_EVIDENCE,
        )

    def test_chinese_question_with_evidence_is_ready(self) -> None:
        state = ResearchState("Agent 如何路由工具？", ("doc",), 1, True)
        selected = [CandidateSource("doc", 0.8, 0.9, 0.9, True)]
        self.assertEqual(evaluate_discussion(state, selected), DiscussionStatus.READY_TO_ANSWER)

    def test_non_answer_source_gets_negative_priority(self) -> None:
        source = CandidateSource("irrelevant", 0.9, 0.9, 0.9, False)
        self.assertEqual(candidate_priority(source), -1.0)

    def test_candidate_priority_weights(self) -> None:
        source = CandidateSource("doc", 0.8, 0.9, 0.9, True)
        self.assertAlmostEqual(candidate_priority(source), 0.4 + 0.27 + 0.18)

    def test_select_sources_empty_and_zero(self) -> None:
        self.assertEqual(select_sources([]), [])
        sources = [CandidateSource("doc", 0.8, 0.9, 0.9, True)]
        self.assertEqual(select_sources(sources, max_sources=0), [])

    def test_select_sources_ties_broken_by_name_descending(self) -> None:
        sources = [
            CandidateSource("a-doc", 0.5, 0.5, 0.5, True),
            CandidateSource("b-doc", 0.5, 0.5, 0.5, True),
        ]
        selected = select_sources(sources, max_sources=1)
        self.assertEqual([source.name for source in selected], ["b-doc"])
