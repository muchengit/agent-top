"""Deterministic tests for the L3 hybrid retrieval lab."""

from __future__ import annotations

import unittest

from .agent_top_labs_l3_rag_hybrid_search import (
    Document,
    FusionMethod,
    HybridSearch,
    Retriever,
    Score,
    _character_bigrams,
    tokenize,
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

    def test_tokenize_lowercases_and_splits(self) -> None:
        self.assertEqual(tokenize("Hello, World! 123"), ["hello", "world", "123"])

    def test_tokenize_empty_string(self) -> None:
        self.assertEqual(tokenize("   !!! "), [])

    def test_tokenize_chinese_characters_dropped(self) -> None:
        self.assertEqual(tokenize("检索 RAG 记忆"), ["rag"])

    def test_character_bigrams(self) -> None:
        self.assertEqual(_character_bigrams("ab cd"), {"ab", "cd"})

    def test_character_bigrams_short_text(self) -> None:
        self.assertEqual(_character_bigrams("a"), set())

    def test_vector_score_identical_text(self) -> None:
        search = make_search()
        scores = search.vector_score("data pipelines")
        self.assertEqual(scores["doc-2"], 1.0)

    def test_vector_score_no_overlap(self) -> None:
        search = make_search()
        scores = search.vector_score("xyz")
        self.assertAlmostEqual(scores["doc-1"], 0.0, places=6)

    def test_custom_weights_change_fused_order(self) -> None:
        search = make_search()
        lexical_heavy = HybridSearch(
            search.retriever, lexical_weight=0.9, vector_weight=0.1
        )
        results = lexical_heavy.search("data pipelines", top_k=3, method=FusionMethod.WEIGHTED_SUM)
        self.assertEqual(results[0].doc_id, "doc-2")

    def test_rrf_order_differs_from_weighted_sum(self) -> None:
        search = make_search()
        ws = search.search("semantic", top_k=6, method=FusionMethod.WEIGHTED_SUM)
        rrf = search.search("semantic", top_k=6, method=FusionMethod.RRF)
        self.assertNotEqual(ws, rrf)

    def test_retriever_lexical_score_empty_query_zero(self) -> None:
        search = make_search()
        scores = search.retriever.lexical_score("")
        for doc in search.retriever.documents:
            self.assertEqual(scores[doc.id], 0.0)

    def test_search_top_k_exceeds_docs(self) -> None:
        search = make_search()
        results = search.search("data", top_k=100)
        self.assertEqual(len(results), 6)

    def test_search_zero_top_k(self) -> None:
        search = make_search()
        results = search.search("data", top_k=0)
        self.assertEqual(results, [])

    def test_empty_document_set(self) -> None:
        retriever = Retriever([])
        search = HybridSearch(retriever)
        self.assertEqual(search.search("anything"), [])
