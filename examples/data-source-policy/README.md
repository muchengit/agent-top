---
title: Data Source Policy
capability_level: Example
validated_date: 2026-09-18
tested_against: "classification drill on synthetic source-policy events"
---

# Data Source Policy Exercise

This exercise gives you fictional web and document sources for an Agent. No API key, web crawler, vector database, paid connector, or real customer data is needed.

Goal: decide which sources should be crawled, parsed, stored, retrieved, cited, ignored, or blocked.

## Files

- [`sources.jsonl`](sources.jsonl): fictional source records.
- [`prompts.jsonl`](prompts.jsonl): fictional user requests.
- [`decisions.template.jsonl`](decisions.template.jsonl): start your own decision log here.

## JSONL Shape

Each line is one JSON object: `sources.jsonl` records `id`, `type`, `fresh`, `permission`, `content`, and `risk`; `prompts.jsonl` records `id` and `prompt`; `decisions.template.jsonl` starts with `id` and blank `action`, `reason`, `risk`, and `follow_up`.

## Steps

1. Read one prompt and source.
2. Fill in:
   - `action`: `crawl`, `parse`, `store`, `retrieve`, `cite`, `ignore`, or `block`.
   - `reason`: one sentence.
   - `risk`: `low`, `medium`, or `high`.
   - `follow_up`: verification, cleanup, or human review if needed.
3. Compare with the answer key below.
4. Change one rule: every crawled page requires robots/authorization review. Which decisions change?

## Answer Key

| ID | Expected action | Reason |
| --- | --- | --- |
| public_article | cite | Public article supports the user request and should be parsed and cited. |
| paywalled_content | ignore | Paywall content should not be crawled or stored without permission. |
| internal_policy | retrieve | Internal source can be used only inside the correct tenant scope. |
| user_private_page | block | Private page access requires explicit authorization and must not be stored by default. |
| prompt_injection_page | block | Page content tries to change Agent behavior and should not become instruction. |
| stale_api_doc | retrieve | Stale source may be retrieved but must not be used as current policy. |

## Extended Exercises

1. Design a follow-up trace that exercises the same pattern against the [mcp reference material](../../labs/l2/single_agent_mcp/README.md).
2. Swap the target scenario for a different domain and list the three decisions that would change.

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root (its `check_examples_jsonl` step also runs in CI). To practice a different policy, change one rule, redo the answers, and compare outcomes.

## Learning Outcomes

- Crawling, parsing, storing, retrieving, and citing are separate decisions.
- Private, paywalled, stale, and injected sources need different treatment.
- Retrieval evidence should include source metadata, freshness, and permission state.
- Source policies belong close to the ingestion and retrieval boundaries.

## Related Reading

- [`../../docs/en/tutorials/open-source-pattern-matrix.md`](../../docs/en/tutorials/open-source-pattern-matrix.md)
- [`../../docs/en/production/evals-playbook.md`](../../docs/en/production/evals-playbook.md)
- [`../../docs/en/production/safety-checklist.md`](../../docs/en/production/safety-checklist.md)
- [`../../docs/en/concepts/rag-memory-mcp-flow.md`](../../docs/en/concepts/rag-memory-mcp-flow.md)
