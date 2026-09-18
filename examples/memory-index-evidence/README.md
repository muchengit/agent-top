# Memory And Index Evidence Exercise

This exercise uses fictional memory, vector, and search evidence. No API key, vector database, search engine, inference server, or external connector is needed.

Goal: decide whether memory, index, and deployment evidence is complete enough to support retrieval, rollback, deletion, or release.

## Files

- [`index-events.jsonl`](index-events.jsonl): fictional memory, vector, search, and deployment evidence.

## JSONL Shape

Each line is one JSON object with a stable `event` and `trace_id`. Event-specific fields: `memory.lifecycle.checked` uses `record_id`, `source`, `confidence`, `scope`, `owner`, `conflict`, `action`, and `last_verified`; `vector.collection.checked` uses `collection`, `tenant`, `schema_version`, `embedding_model`, `deletion_propagated`, and `index_metadata`; `search.evidence.checked` uses `query`, `filter`, `index_version`, `source_doc_id`, `freshness`, and `ranking`; `serving.deployment.checked` uses `endpoint`, `model_revision`, `revision_id`, `health`, `resource_limits`, `timeout_policy`, `capacity`, and `rollback_action`. All events end with `decision`.

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

## Extended Exercises

1. Design a follow-up trace that exercises the same pattern against the [flow reference material](../../docs/en/concepts/rag-memory-mcp-flow.md).
2. Swap the target scenario for a different domain and list the three decisions that would change.

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root (its `check_examples_jsonl` step also runs in CI). To practice a different policy, change one rule, redo the answers, and compare outcomes.

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
