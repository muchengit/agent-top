"""L3 deterministic hybrid retrieval: BM25-style keywords plus simple vector scores.

This module implements a small, fully deterministic hybrid search pipeline:

1. A BM25-style lexical scorer built on term frequencies and inverse document
   frequency, with no external dependencies.
2. A simple character/word overlap scorer that stands in for a dense embedding
   ("fake vector") score.
3. A fusion step that combines both scores into a final ranking using weighted
   sum fusion or reciprocal-rank fusion (RRF).

The pipeline runs offline, needs no API keys, and produces reproducible output.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum

_TOKEN_PATTERN = re.compile(r"[a-z0-9]+")
_BIGRAM_PATTERN = re.compile(r"[a-z0-9]{2}")


def tokenize(text: str) -> list[str]:
    """Lowercase the text and split it into alphanumeric tokens."""
    return _TOKEN_PATTERN.findall(text.lower())


def _character_bigrams(text: str) -> set[str]:
    """Return the set of lowercase alphanumeric character bigrams in text."""
    return set(_BIGRAM_PATTERN.findall(text.lower()))


@dataclass(frozen=True)
class Document:
    """A single indexable document with a stable id and raw text."""

    id: str
    text: str


@dataclass(frozen=True)
class Score:
    """A retrieval result with its lexical, fake-vector, and fused scores."""

    doc_id: str
    lexical: float
    vector: float
    fused: float


class FusionMethod(Enum):
    """Supported deterministic fusion strategies."""

    WEIGHTED_SUM = "weighted_sum"
    RRF = "rrf"


@dataclass
class Retriever:
    """BM25-style lexical retriever over a fixed, in-memory document set."""

    documents: list[Document]

    def __post_init__(self) -> None:
        """Precompute per-document term statistics and inverse document frequency."""
        self._term_freqs: dict[str, Counter[str]] = {}
        self._doc_lengths: dict[str, int] = {}
        doc_count = len(self.documents)
        term_doc_freq: Counter[str] = Counter()
        for doc in self.documents:
            tokens = tokenize(doc.text)
            self._doc_lengths[doc.id] = len(tokens)
            self._term_freqs[doc.id] = Counter(tokens)
            term_doc_freq.update(self._term_freqs[doc.id].keys())
        self._idf: dict[str, float] = {}
        for term, df in term_doc_freq.items():
            self._idf[term] = math.log(1.0 + (doc_count - df + 0.5) / (df + 0.5))
        total_length = sum(self._doc_lengths.values())
        self._avg_doc_len = total_length / doc_count if doc_count else 0.0

    def lexical_score(self, query: str) -> dict[str, float]:
        """Return a BM25-style score per document id for the given query."""
        query_terms = set(tokenize(query))
        if not query_terms:
            return {doc.id: 0.0 for doc in self.documents}
        avg_doc_len = self._avg_doc_len or 1.0
        scores: dict[str, float] = {}
        for doc in self.documents:
            doc_id = doc.id
            total = 0.0
            for term in query_terms:
                tf = self._term_freqs[doc_id].get(term, 0)
                if tf == 0:
                    continue
                doc_len_ratio = self._doc_lengths[doc_id] / avg_doc_len
                total += self._idf.get(term, 0.0) * (tf * 2.2) / (tf + 1.5 * doc_len_ratio)
            scores[doc_id] = total
        return scores


@dataclass(frozen=True)
class HybridSearch:
    """Hybrid retriever that fuses lexical retrieval with a fake-vector scorer."""

    retriever: Retriever
    lexical_weight: float = 0.5
    vector_weight: float = 0.5
    rrf_k: int = 60

    def vector_score(self, query: str) -> dict[str, float]:
        """Return overlapping character-bigram ratios acting as dense-vector scores."""
        query_bigrams = _character_bigrams(query)
        if not query_bigrams:
            return {doc.id: 0.0 for doc in self.retriever.documents}
        scores: dict[str, float] = {}
        for doc in self.retriever.documents:
            doc_bigrams = _character_bigrams(doc.text)
            scores[doc.id] = len(query_bigrams & doc_bigrams) / len(query_bigrams)
        return scores

    def search(
        self,
        query: str,
        top_k: int = 3,
        method: FusionMethod = FusionMethod.WEIGHTED_SUM,
    ) -> list[Score]:
        """Rank documents for a query and return the top-k fused results."""
        lexical_scores = self.retriever.lexical_score(query)
        vector_scores = self.vector_score(query)
        doc_ids = [doc.id for doc in self.retriever.documents]
        lexical_rank = {
            doc_id: rank for rank, doc_id in enumerate(self._rank_ids(lexical_scores, doc_ids))
        }
        vector_rank = {
            doc_id: rank for rank, doc_id in enumerate(self._rank_ids(vector_scores, doc_ids))
        }
        fused: dict[str, float] = {}
        for doc_id in doc_ids:
            fused[doc_id] = self._fuse(
                lexical_scores[doc_id],
                vector_scores[doc_id],
                lexical_rank[doc_id],
                vector_rank[doc_id],
                method,
            )
        ordered_ids = self._rank_ids(fused, doc_ids)
        return [
            Score(doc_id, lexical_scores[doc_id], vector_scores[doc_id], fused[doc_id])
            for doc_id in ordered_ids[:top_k]
        ]

    def _fuse(
        self,
        lexical_score: float,
        vector_score: float,
        lexical_rank: int,
        vector_rank: int,
        method: FusionMethod,
    ) -> float:
        """Fuse lexical and vector signals using the selected strategy."""
        if method is FusionMethod.WEIGHTED_SUM:
            return self.lexical_weight * lexical_score + self.vector_weight * vector_score
        return 1.0 / (self.rrf_k + 1 + lexical_rank) + 1.0 / (self.rrf_k + 1 + vector_rank)

    @staticmethod
    def _rank_ids(scores: dict[str, float], doc_ids: Sequence[str]) -> list[str]:
        """Return document ids sorted by descending score, breaking ties by id."""
        return sorted(doc_ids, key=lambda doc_id: (-scores[doc_id], doc_id))
