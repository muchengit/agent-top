from __future__ import annotations

import unittest

from .agent_top_labs_l3_rag_evaluator import RetrievalCase, evaluate_retrieval


class RagEvaluatorTest(unittest.TestCase):
    def test_passes_when_required_source_present(self) -> None:
        case = RetrievalCase("pricing", "pricing-v2", ("intro", "pricing-v2"), False)
        self.assertEqual(evaluate_retrieval(case), {"status": "pass", "source": "pricing-v2"})

    def test_refuses_when_required_source_missing_but_refusal_allowed(self) -> None:
        case = RetrievalCase("pricing", "pricing-v2", ("intro",), True)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "refuse_ok", "reason": "required source missing"},
        )

    def test_fails_when_required_source_missing(self) -> None:
        case = RetrievalCase("pricing", "pricing-v2", ("intro",), False)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "fail", "missing_source": "pricing-v2"},
        )

    def test_fails_when_retrieved_set_is_empty(self) -> None:
        case = RetrievalCase("pricing", "pricing-v2", (), False)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "fail", "missing_source": "pricing-v2"},
        )

    def test_refuses_when_retrieved_set_is_empty_and_allowed(self) -> None:
        case = RetrievalCase("pricing", "pricing-v2", (), True)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "refuse_ok", "reason": "required source missing"},
        )

    def test_required_source_must_match_exactly_not_substring(self) -> None:
        case = RetrievalCase("pricing", "pricing", ("pricing-v2",), False)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "fail", "missing_source": "pricing"},
        )

    def test_pass_takes_precedence_when_refusal_allowed(self) -> None:
        case = RetrievalCase("pricing", "pricing-v2", ("pricing-v2",), True)
        self.assertEqual(evaluate_retrieval(case), {"status": "pass", "source": "pricing-v2"})

    def test_duplicate_sources_still_pass(self) -> None:
        case = RetrievalCase("pricing", "pricing-v2", ("pricing-v2", "pricing-v2"), False)
        self.assertEqual(evaluate_retrieval(case), {"status": "pass", "source": "pricing-v2"})

    def test_chinese_sources(self) -> None:
        case = RetrievalCase("定价如何", "定价说明", ("简介", "定价说明"), False)
        self.assertEqual(evaluate_retrieval(case), {"status": "pass", "source": "定价说明"})

    def test_chinese_required_missing(self) -> None:
        case = RetrievalCase("定价如何", "定价说明", ("简介",), False)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "fail", "missing_source": "定价说明"},
        )

    def test_frozen_case_rejects_mutation(self) -> None:
        case = RetrievalCase("pricing", "pricing-v2", (), False)
        with self.assertRaises(Exception):
            case.query = "other"  # type: ignore[misc]

    def test_status_values(self) -> None:
        self.assertEqual(
            evaluate_retrieval(
                RetrievalCase("q", "src", ("src",), False)
            )["status"],
            "pass",
        )
        self.assertEqual(
            evaluate_retrieval(
                RetrievalCase("q", "src", (), True)
            )["status"],
            "refuse_ok",
        )
        self.assertEqual(
            evaluate_retrieval(
                RetrievalCase("q", "src", (), False)
            )["status"],
            "fail",
        )

    def test_case_sensitive_source_match(self) -> None:
        case = RetrievalCase("q", "Docs", ("docs",), False)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "fail", "missing_source": "Docs"},
        )

    def test_all_retrieved_sources_ignored_except_required(self) -> None:
        case = RetrievalCase("q", "target", ("other-a", "other-b"), False)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "fail", "missing_source": "target"},
        )

    def test_required_source_among_many_passes(self) -> None:
        case = RetrievalCase("q", "target", ("a", "target", "b", "c"), True)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "pass", "source": "target"},
        )

    def test_query_irrelevant_to_result(self) -> None:
        case = RetrievalCase("anything", "target", ("target",), False)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "pass", "source": "target"},
        )

    def test_required_source_is_empty_string(self) -> None:
        case = RetrievalCase("q", "", ("a",), False)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "fail", "missing_source": ""},
        )

    def test_retrieved_sources_tuple_duplicates(self) -> None:
        case = RetrievalCase("q", "src", ("src", "src", "src"), False)
        self.assertEqual(
            evaluate_retrieval(case),
            {"status": "pass", "source": "src"},
        )
