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

    def test_partial_match_is_not_retrieved(self) -> None:
        store = InMemoryStore(["machine learning", "machine shop"])
        self.assertEqual(store.retrieve("machine learn"), ["machine learning"])

    def test_multiple_matches_respect_order(self) -> None:
        store = InMemoryStore(["first doc", "second doc", "third doc"])
        self.assertEqual(store.retrieve("doc", top_k=10), ["first doc", "second doc", "third doc"])

    def test_retrieve_top_k_negative_returns_empty(self) -> None:
        store = InMemoryStore(["doc one"])
        self.assertEqual(store.retrieve("doc", top_k=-1), [])

    def test_memory_recent_zero_returns_all(self) -> None:
        memory = SessionMemory()
        memory.remember("hello")
        self.assertEqual(memory.recent(0), ["hello"])

    def test_memory_recent_negative_returns_empty(self) -> None:
        memory = SessionMemory()
        memory.remember("hello")
        self.assertEqual(memory.recent(-3), [])

    def test_answer_with_trace_multiple_hits(self) -> None:
        store = InMemoryStore(["RAG a", "RAG b"])
        memory = SessionMemory()
        answer, _ = answer_with_trace("RAG", store, memory)
        self.assertEqual(answer, "RAG a | RAG b")

    def test_trace_memory_records_recent_turn_count(self) -> None:
        store = InMemoryStore([])
        memory = SessionMemory()
        memory.remember("previous")
        _, traces = answer_with_trace("current", store, memory)
        memory_trace = dict(traces[1].data)
        self.assertEqual(memory_trace["recent_turns"], "2")

    def test_memory_remembers_every_query(self) -> None:
        store = InMemoryStore([])
        memory = SessionMemory()
        answer_with_trace("q1", store, memory)
        answer_with_trace("q2", store, memory)
        self.assertEqual(memory.turns, ["q1", "q2"])

    def test_trace_is_mutable_dataclass(self) -> None:
        store = InMemoryStore([])
        memory = SessionMemory()
        _, traces = answer_with_trace("q", store, memory)
        traces[0].event = "changed"
        self.assertEqual(traces[0].event, "changed")

    def test_store_documents_accessible_directly(self) -> None:
        store = InMemoryStore(["a", "b"])
        self.assertEqual(store.documents, ["a", "b"])

    def test_retrieve_case_insensitive_chinese(self) -> None:
        store = InMemoryStore(["RAG 检索", "AGENT 编排"])
        self.assertEqual(store.retrieve("rag"), ["RAG 检索"])
