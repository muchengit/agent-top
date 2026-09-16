---
title: L3 RAG Memory Observability
validated_date: 2026-09-16
tested_against: "python 3.10+"
i18n-key: l3-rag-memory-observability
last-synced: 2026-09-16
---

# L3 RAG Memory Observability

## Goal

Compose RAG, memory, generation, and observability into a traceable skeleton.

## Prerequisites

- L0 through L2 completed
- Basic understanding of retrieval and context assembly

## Core Data Flow

1. User query enters.
2. RAG retrieves scoped context.
3. Memory adds durable context.
4. The agent plans and calls tools.
5. Observability records prompts, retrievals, tool calls, latency, and cost.

## Related Lab

See [`../../labs/l3/rag_memory_observability/README.md`](../../labs/l3/rag_memory_observability/README.md).
