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

    def test_select_sources_filters_non_answer_sources(self) -> None:
        sources = [
            CandidateSource("good", 0.8, 0.9, 0.9, True),
            CandidateSource("bad", 0.9, 0.9, 0.9, False),
        ]
        selected = select_sources(sources, max_sources=3)
        self.assertEqual([s.name for s in selected], ["good", "bad"])
        self.assertEqual([s.name for s in selected if s.contains_answer], ["good"])

    def test_candidate_priority_weights_relevance_highest(self) -> None:
        high_relevance = CandidateSource("a", 1.0, 0.0, 0.0, True)
        low_relevance = CandidateSource("b", 0.0, 1.0, 0.0, True)
        self.assertGreater(
            candidate_priority(high_relevance),
            candidate_priority(low_relevance),
        )

    def test_candidate_priority_zero_scores(self) -> None:
        source = CandidateSource("doc", 0.0, 0.0, 0.0, True)
        self.assertEqual(candidate_priority(source), 0.0)

    def test_evaluate_discussion_no_clarification_needed_but_question_blank(self) -> None:
        state = ResearchState("", (), 0, False)
        selected = [CandidateSource("doc", 0.8, 0.9, 0.9, True)]
        self.assertEqual(
            evaluate_discussion(state, selected),
            DiscussionStatus.SHOULD_ASK_USER,
        )

    def test_question_whitespace_asks_user(self) -> None:
        state = ResearchState(" \t", (), 0, False)
        self.assertEqual(
            evaluate_discussion(state, []),
            DiscussionStatus.SHOULD_ASK_USER,
        )

    def test_refuse_when_evidence_sources_missing_even_with_other_sources(self) -> None:
        state = ResearchState("q", ("other",), 2, True)
        selected = [
            CandidateSource("other", 0.9, 0.9, 0.9, False),
        ]
        self.assertEqual(
            evaluate_discussion(state, selected),
            DiscussionStatus.SHOULD_REFUSE,
        )

    def test_empty_selected_sources_refuses(self) -> None:
        state = ResearchState("q", (), 2, True)
        self.assertEqual(
            evaluate_discussion(state, []),
            DiscussionStatus.SHOULD_REFUSE,
        )

    def test_freshness_low_on_some_evidence_blocks(self) -> None:
        state = ResearchState("q", ("a", "b"), 2, True)
        selected = [
            CandidateSource("a", 0.8, 0.4, 0.9, True),
            CandidateSource("b", 0.8, 0.9, 0.9, True),
        ]
        self.assertEqual(
            evaluate_discussion(state, selected),
            DiscussionStatus.NEEDS_MORE_EVIDENCE,
        )

    def test_state_rounds_used_does_not_affect_status(self) -> None:
        state = ResearchState("q", ("doc",), 0, True)
        selected = [CandidateSource("doc", 0.8, 0.9, 0.9, True)]
        self.assertEqual(
            evaluate_discussion(state, selected),
            DiscussionStatus.READY_TO_ANSWER,
        )

    def test_enum_values(self) -> None:
        self.assertEqual(DiscussionStatus.READY_TO_ANSWER.value, "ready_to_answer")
        self.assertEqual(DiscussionStatus.NEEDS_MORE_EVIDENCE.value, "needs_more_evidence")
        self.assertEqual(DiscussionStatus.SHOULD_ASK_USER.value, "should_ask_user")
        self.assertEqual(DiscussionStatus.SHOULD_REFUSE.value, "should_refuse")

    def test_frozen_state_rejects_mutation(self) -> None:
        state = ResearchState("q", ("doc",), 1, True)
        with self.assertRaises(Exception):
            state.question = "changed"  # type: ignore[misc]
