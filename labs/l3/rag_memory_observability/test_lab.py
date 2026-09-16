import unittest

from .agent_top_labs_l3_rag_memory_observability import InMemoryStore, SessionMemory, answer_with_trace


class RagMemoryObservabilityTest(unittest.TestCase):
    def test_retrieval_memory_and_trace(self) -> None:
        store = InMemoryStore(["RAG retrieves context", "MCP exposes tools"])
        memory = SessionMemory()
        answer, traces = answer_with_trace("RAG", store, memory)
        self.assertIn("RAG retrieves context", answer)
        self.assertEqual([trace.event for trace in traces], ["retrieve", "memory"])
