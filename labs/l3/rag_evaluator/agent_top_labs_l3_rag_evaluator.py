"""L3 deterministic RAG evaluation helper."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievalCase:
    query: str
    required_source: str
    retrieved_sources: tuple[str, ...]
    allowed_when_missing: bool


def evaluate_retrieval(case: RetrievalCase) -> dict[str, object]:
    retrieved = set(case.retrieved_sources)
    has_required = case.required_source in retrieved
    if has_required:
        return {"status": "pass", "source": case.required_source}
    if case.allowed_when_missing:
        return {"status": "refuse_ok", "reason": "required source missing"}
    return {"status": "fail", "missing_source": case.required_source}
