# Memory Vs Evidence Exercise

This exercise gives you fictional memory records and current evidence. No API key, vector database, memory service, or external connector is needed.

Goal: decide which facts come from memory, live tool results, retrieved sources, or should be ignored.

## Files

- [`memory.jsonl`](memory.jsonl): fictional long-term memory records.
- [`prompts.jsonl`](prompts.jsonl): fictional user questions.
- [`answers.template.jsonl`](answers.template.jsonl): start your decision log here.

## Steps

1. Read one prompt.
2. Compare memory records with live evidence.
3. Fill in:
   - `preferred_source`: `memory`, `tool_result`, `retrieved_source`, or `refuse`.
   - `decision`: one sentence.
   - `reason`: why this source wins.
   - `follow_up`: what to ask or verify.
4. Compare with the answer key below.
5. Change one rule: memory writes require confirmation. Which outcomes change?

## Answer Key

| Prompt ID | Preferred source | Reason |
| --- | --- | --- |
| preferred_editor | memory | Preference is explicit, recent, low-risk, and not contradicted by live data. |
| stale_city | refuse | Memory is stale and no current source is available. |
| conflicting_contact | tool_result | Live contact result beats outdated memory. |
| private_api_key | refuse | Secret must not be answered or written to memory. |
| delete_without_confirmation | refuse | Memory deletion is destructive and needs confirmation. |

## Learning Outcomes

- Memory is not always authoritative.
- Live evidence should beat stale memory.
- Secrets and destructive memory operations need refusal or confirmation.
- Conflicting sources require explicit precedence rules.

## Related Reading

- [`../../docs/en/concepts/long-term-memory.md`](../../docs/en/concepts/long-term-memory.md)
- [`../../docs/en/concepts/implementation-guide.md`](../../docs/en/concepts/implementation-guide.md)
- [`../../docs/en/production/safety-checklist.md`](../../docs/en/production/safety-checklist.md)
