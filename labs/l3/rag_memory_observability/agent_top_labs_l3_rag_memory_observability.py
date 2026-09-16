"""L3 local skeleton for RAG, memory, generation, and observability."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Trace:
    event: str
    data: dict[str, str]


class InMemoryStore:
    def __init__(self, documents: list[str]) -> None:
        self.documents = documents

    def retrieve(self, query: str, top_k: int = 2) -> list[str]:
        return [doc for doc in self.documents if query.lower() in doc.lower()][:top_k]


class SessionMemory:
    def __init__(self) -> None:
        self.turns: list[str] = []

    def remember(self, message: str) -> None:
        self.turns.append(message)

    def recent(self, limit: int = 3) -> list[str]:
        return self.turns[-limit:]


def answer_with_trace(
    query: str,
    store: InMemoryStore,
    memory: SessionMemory,
) -> tuple[str, list[Trace]]:
    memory.remember(query)
    retrieved = store.retrieve(query)
    traces = [
        Trace("retrieve", {"query": query, "hits": str(len(retrieved))}),
        Trace("memory", {"recent_turns": str(len(memory.recent()))}),
    ]
    answer = " | ".join(retrieved) if retrieved else "No retrieved context."
    return answer, traces
