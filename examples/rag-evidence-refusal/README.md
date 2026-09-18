# RAG Evidence Refusal Exercise

This exercise gives you fictional retrieved passages. No API key, search service, vector database, or paid connector is needed.

Goal: decide whether an Agent can answer, must cite, or must refuse because evidence is missing, stale, or conflicting.

## Files

- [`sources.jsonl`](sources.jsonl): fictional retrieved passages.
- [`prompts.jsonl`](prompts.jsonl): fictional user questions.
- [`answers.template.jsonl`](answers.template.jsonl): start your own answer log here.

## Steps

1. Read one prompt.
2. Select only evidence that can support the prompt.
3. Fill in:
   - `decision`: `answer`, `answer_with_citation`, or `refuse`.
   - `source_ids`: comma-separated source IDs.
   - `reason`: one sentence.
   - `follow_up`: what to ask or verify before answering.
4. Compare with the answer key below.
5. Change one rule: require citations for every factual claim. Which answers change?

## Answer Key

| Prompt ID | Expected decision | Reason |
| --- | --- | --- |
| shipping_policy_current | answer_with_citation | Current policy source directly supports the answer. |
| old_refund_deadline | refuse | Source is stale; current policy must be checked. |
| contradictory_discount | refuse | Sources conflict; needs policy owner or fresher source. |
| unsupported_security_claim | refuse | No retrieved source supports the claim. |
| supported_return_window | answer_with_citation | Two fresh sources agree. |

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root (its `check_examples_jsonl` step also runs in CI). To practice a different policy, change one rule, redo the answers, and compare outcomes.

## Learning Outcomes

- Evidence sufficiency.
- Citation discipline.
- Refusal without inventing facts.
- Stale-source handling.
- Conflict resolution before answering.

## Related Reading

- [`../../docs/en/tutorials/quick-navigation.md`](../../docs/en/tutorials/quick-navigation.md)
- [`../../docs/en/concepts/model-hallucination.md`](../../docs/en/concepts/model-hallucination.md)
- [`../../docs/en/concepts/long-term-memory.md`](../../docs/en/concepts/long-term-memory.md)
- [`../../docs/en/l3-rag-memory-observability.md`](../../docs/en/l3-rag-memory-observability.md)
