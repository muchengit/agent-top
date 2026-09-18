---
title: L3 RAG Memory Observability
validated_date: 2026-09-18
tested_against: "python 3.10+"
i18n-key: l3-rag-memory-observability
last-synced: 2026-09-18
---

# L3 RAG Memory Observability

## Goal

Compose RAG, memory, generation, and observability into a traceable skeleton.

## Prerequisites

- L0 through L2 completed
- Basic understanding of retrieval and context assembly
- No API key required

## Core Data Flow

1. User query enters.
2. RAG retrieves scoped context.
3. Memory adds durable context.
4. The Agent plans and calls tools.
5. Observability records prompts, retrievals, tool calls, latency, and cost.

## Why This Matters

Most production Agent failures are not “the model was wrong” in the abstract. They are usually concrete problems such as:

- retrieval missed the right document;
- memory added stale context;
- the Agent did not log enough to debug;
- the final answer did not show what evidence was used.

This Lab is a traceable skeleton for that kind of system.

## The Lab Design

```python
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
```

## Step-by-Step Walkthrough

### 1. Build a small document set

```bash
python - <<'PY'
from labs.l3.rag_memory_observability.agent_top_labs_l3_rag_memory_observability import InMemoryStore, SessionMemory, answer_with_trace
store = InMemoryStore(["RAG retrieves context", "MCP exposes tools", "Memory persists turns"])
memory = SessionMemory()
answer, traces = answer_with_trace("RAG", store, memory)
print(answer)
for trace in traces:
    print(trace.event, trace.data)
PY
```

Expected output:

```text
RAG retrieves context
retrieve {'query': 'RAG', 'hits': '1'}
memory {'recent_turns': '1'}
```

### 2. Add a second turn

```bash
python - <<'PY'
from labs.l3.rag_memory_observability.agent_top_labs_l3_rag_memory_observability import InMemoryStore, SessionMemory, answer_with_trace
store = InMemoryStore(["RAG retrieves context", "MCP exposes tools", "Memory persists turns"])
memory = SessionMemory()
answer_with_trace("RAG", store, memory)
_, traces = answer_with_trace("MCP", store, memory)
print(traces[1].data)
PY
```

Expected output:

```text
{'recent_turns': '2'}
```

### 3. Run the tests

```bash
python -m unittest labs.l3.rag_memory_observability.test_lab
```

Expected result:

```text
Ran 1 test in 0.00Xs

OK
```

## What Each Part Does

- `InMemoryStore` is a tiny retrieval layer.
- `SessionMemory` is a tiny persistent conversation layer.
- `answer_with_trace()` wires the two together and emits traces.
- `Trace` is the debug surface for what happened.

## Why Traces Matter

A trace gives you a chronological record.

In production you would usually include:

- prompt id;
- retrieved document ids;
- memory keys used;
- tool call id;
- latency;
- token usage;
- cost;
- success or failure reason.

That lets you answer questions like:

- did we retrieve the right context?
- did memory introduce stale data?
- which call took too long?
- which failure mode recurred?

## Common Mistakes

- Retrieving too much context for a query.
- Mixing session memory with durable user memory.
- Producing answers without tracing which context was used.
- Treating memory as always correct.
- Forgetting to log tool call boundaries.

## Self-Check

1. What is the difference between retrieval and memory?
2. Why should a trace include retrieved hits?
3. What is one risk of over-broad retrieval?
4. Why is `recent_turns` useful in a trace?
5. What would you add before sending this to production?

## Related Lab

Read the Lab README: [`../../labs/l3/rag_memory_observability/README.md`](../../labs/l3/rag_memory_observability/README.md).

Run the Lab tests:

```bash
python -m unittest labs.l3.rag_memory_observability.test_lab
```

## Next Step

Continue with [`L4 Production`](l4-production.md) for evals, guardrails, rollback, and postmortem thinking.

## Interview Questions

Reinforce L3 concepts with the system design question bank: [`L3 System Design Questions`](interviews/questions/l3-system-design.md).
