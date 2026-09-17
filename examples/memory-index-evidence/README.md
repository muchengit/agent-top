# Memory And Index Evidence Exercise

This exercise uses fictional memory, vector, and search evidence. No API key, vector database, search engine, inference server, or external connector is needed.

Goal: decide whether memory, index, and deployment evidence is complete enough to support retrieval, rollback, deletion, or release.

## Files

- [`index-events.jsonl`](index-events.jsonl): fictional memory, vector, search, and deployment evidence.

## Steps

1. Read each evidence event.
2. Decide whether it is enough for safe retrieval or release.
3. Identify the owner: `memory`, `index`, `search`, `serving`, `runtime`, or `release`.
4. Choose the next action: `use`, `block`, `delete`, `rollback`, `schema_fix`, or `postmortem`.
5. For each blocked event, name one missing evidence field.

## Answer Key

| Finding | Owner | Next action |
| --- | --- | --- |
| Memory lacks owner or scope | memory | block |
| Vector collection crosses tenant boundary | index | delete + schema_fix |
| Search result lacks source doc id | search | block |
| Serving revision id differs from intended deployment | serving | rollback |

## Learning Outcomes

- Memory is context, not authority.
- Vector collections need tenant/purpose/schema/deletion boundaries.
- Retrieval evidence needs query, filter, index version, source id, freshness, and ranking.
- Serving deployment evidence belongs in cost, latency, rollback, and postmortem workflows.

## Related Reading

- [`../../docs/en/concepts/long-term-memory.md`](../../docs/en/concepts/long-term-memory.md)
- [`../../docs/en/concepts/rag-memory-mcp-flow.md`](../../docs/en/concepts/rag-memory-mcp-flow.md)
- [`../../docs/en/production/cost-stability-operations.md`](../../docs/en/production/cost-stability-operations.md)
- [`../../docs/en/production/evals-playbook.md`](../../docs/en/production/evals-playbook.md)
