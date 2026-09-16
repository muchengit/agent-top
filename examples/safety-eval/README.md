# Safety Eval Evidence Exercise

This exercise uses fictional safety tests. No API key, model provider, or security scanner is needed.

Goal: decide whether a safety failure should block release, route to an owner, or become a new guardrail.

## Files

- [`safety-tests.jsonl`](safety-tests.jsonl): fictional safety eval cases.

## Steps

1. Read each safety test event.
2. Decide whether the result blocks release.
3. Identify the owner: `prompt`, `tool`, `retrieval`, `memory`, `guardrail`, or `runtime`.
4. Choose the next action: `guardrail`, `eval_case`, `trace_field`, `rollback`, or `postmortem`.
5. For each blocked case, write one guardrail evidence field that was missing.

## Answer Key

| Finding | Owner | Next action |
| --- | --- | --- |
| Retrieved doc instructs tool call | retrieval | guardrail + eval_case |
| Output includes API key fragment | guardrail | trace_field + rollback |
| Memory conflict not surfaced | memory | guardrail + eval_case |
| Hallucinated citation lacks source id | prompt | eval_case + trace_field |

## Learning Outcomes

- Safety evals should test injection, leakage, refusal, harm, and hallucination separately.
- A guardrail pass is evidence, not an opinion.
- Fail-closed decisions should be explicit when evidence is missing.
- Production traces can become reviewable eval cases after redaction.

## Related Reading

- [`../../docs/en/production/safety-checklist.md`](../../docs/en/production/safety-checklist.md)
- [`../../docs/en/production/evals-playbook.md`](../../docs/en/production/evals-playbook.md)
- [`../../docs/en/tutorials/open-source-pattern-matrix.md`](../../docs/en/tutorials/open-source-pattern-matrix.md)
