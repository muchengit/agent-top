"""Deterministic tests for the L3 hybrid retrieval lab."""

from __future__ import annotations

import unittest

from .agent_top_labs_l3_rag_hybrid_search import (
    Document,
    FusionMethod,
    HybridSearch,
    Retriever,
    Score,
)


def make_search() -> HybridSearch:
    """Build the lab's fixed in-memory document set and hybrid search."""
    documents = [
        Document("doc-1", "The quick brown fox jumps over the lazy dog"),
        Document("doc-2", "Data pipelines move large volumes of data quickly"),
        Document("doc-3", "RAG systems combine retrieval with generation"),
        Document("doc-4", "Vector databases store embeddings for semantic search"),
        Document("doc-5", "The search engine returns ranked results"),
        Document("doc-6", "Real time analytics ingest streaming events"),
    ]
    return HybridSearch(Retriever(documents))


class HybridSearchTest(unittest.TestCase):
    def test_keyword_hit(self) -> None:
        search = make_search()
        results = search.search("retrieval generation")
        self.assertEqual(results[0].doc_id, "doc-3")
        self.assertGreater(results[0].lexical, 0.0)

    def test_semantic_synonym_hit(self) -> None:
        search = make_search()
        results = search.search("embedding vectors")
        self.assertEqual(results[0].doc_id, "doc-4")
        self.assertGreater(results[0].vector, 0.0)

    def test_fusion_beats_single_retrieval(self) -> None:
        search = make_search()
        fused = search.search("semantic retrieval", top_k=1)
        lexical_only = HybridSearch(
            search.retriever, lexical_weight=1.0, vector_weight=0.0
        ).search("semantic retrieval", top_k=1)
        vector_only = HybridSearch(
            search.retriever, lexical_weight=0.0, vector_weight=1.0
        ).search("semantic retrieval", top_k=1)
        top = fused[0]
        self.assertGreater(top.lexical, 0.0)
        self.assertGreater(top.vector, 0.0)
        self.assertAlmostEqual(
            top.fused,
            search.lexical_weight * top.lexical + search.vector_weight * top.vector,
            places=6,
        )
        self.assertIn(lexical_only[0].doc_id, {s.doc_id for s in fused[:3]})
        self.assertIn(vector_only[0].doc_id, {s.doc_id for s in fused[:3]})

    def test_top_k_truncation(self) -> None:
        search = make_search()
        results = search.search("search", top_k=2)
        self.assertEqual(len(results), 2)
        self.assertLessEqual(len(results), 2)

    def test_empty_query(self) -> None:
        search = make_search()
        results = search.search("")
        self.assertEqual(len(results), 3)
        self.assertEqual([score.fused for score in results], [0.0, 0.0, 0.0])

    def test_no_hit(self) -> None:
        search = make_search()
        results = search.search("zzzzzzzz")
        self.assertEqual(len(results), 3)
        self.assertEqual([score.lexical for score in results], [0.0, 0.0, 0.0])
        self.assertEqual([score.fused for score in results], [0.0, 0.0, 0.0])

    def test_score_monotonicity(self) -> None:
        search = make_search()
        results = search.search("data")
        fused_scores = [score.fused for score in results]
        self.assertEqual(fused_scores, sorted(fused_scores, reverse=True))

    def test_rrf_matches_expected_formula(self) -> None:
        search = make_search()
        results = search.search("data", top_k=6, method=FusionMethod.RRF)
        self.assertEqual(len(results), 6)
        self.assertGreater(results[0].fused, results[-1].fused)

    def test_frozen_dataclasses(self) -> None:
        doc = Document("id-1", "text")
        with self.assertRaises(AttributeError):
            doc.id = "id-2"  # type: ignore[misc]
        score = Score("id-1", 1.0, 2.0, 3.0)
        with self.assertRaises(AttributeError):
            score.doc_id = "id-2"  # type: ignore[misc]
