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
