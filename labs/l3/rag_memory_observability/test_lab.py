from __future__ import annotations

import unittest

from .agent_top_labs_l3_rag_memory_observability import (
    InMemoryStore,
    SessionMemory,
    answer_with_trace,
)


class RagMemoryObservabilityTest(unittest.TestCase):
    def test_retrieval_memory_and_trace(self) -> None:
        store = InMemoryStore(["RAG retrieves context", "MCP exposes tools"])
        memory = SessionMemory()
        answer, traces = answer_with_trace("RAG", store, memory)
        self.assertIn("RAG retrieves context", answer)
        self.assertEqual([trace.event for trace in traces], ["retrieve", "memory"])

    def test_retrieval_is_case_insensitive(self) -> None:
        store = InMemoryStore(["RAG retrieves context", "MCP exposes tools"])
        self.assertEqual(store.retrieve("rag"), ["RAG retrieves context"])

    def test_no_match_returns_empty_and_answer_falls_back(self) -> None:
        store = InMemoryStore(["RAG retrieves context"])
        memory = SessionMemory()
        answer, traces = answer_with_trace("missing topic", store, memory)
        self.assertEqual(answer, "No retrieved context.")
        trace_data = dict(traces[0].data)
        self.assertEqual(trace_data["hits"], "0")

    def test_top_k_limits_results(self) -> None:
        store = InMemoryStore(["doc one", "doc two", "doc three"])
        self.assertEqual(store.retrieve("doc", top_k=2), ["doc one", "doc two"])
        self.assertEqual(store.retrieve("doc", top_k=0), [])

    def test_top_k_zero_returns_empty(self) -> None:
        store = InMemoryStore(["doc one"])
        self.assertEqual(store.retrieve("doc", top_k=0), [])

    def test_empty_query_matches_everything(self) -> None:
        store = InMemoryStore(["doc one", "doc two"])
        self.assertEqual(store.retrieve("", top_k=10), ["doc one", "doc two"])

    def test_memory_remembers_query_and_recent_orders(self) -> None:
        memory = SessionMemory()
        memory.remember("first")
        memory.remember("second")
        memory.remember("third")
        self.assertEqual(memory.recent(2), ["second", "third"])
        self.assertEqual(memory.recent(), ["first", "second", "third"])

    def test_memory_recent_limit_larger_than_history(self) -> None:
        memory = SessionMemory()
        memory.remember("only")
        self.assertEqual(memory.recent(10), ["only"])

    def test_trace_data_records_query_and_hits(self) -> None:
        store = InMemoryStore(["RAG retrieves context", "RAG memory"])
        memory = SessionMemory()
        _, traces = answer_with_trace("RAG", store, memory)
        retrieve_trace = traces[0]
        self.assertEqual(retrieve_trace.event, "retrieve")
        self.assertEqual(dict(retrieve_trace.data)["query"], "RAG")
        self.assertEqual(dict(retrieve_trace.data)["hits"], "2")

    def test_chinese_retrieval(self) -> None:
        store = InMemoryStore(["检索系统返回中文上下文", "MCP exposes tools"])
        self.assertEqual(store.retrieve("中文"), ["检索系统返回中文上下文"])
