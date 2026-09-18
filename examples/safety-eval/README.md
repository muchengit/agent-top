---
title: Safety Eval Evidence
capability_level: Example
validated_date: 2026-09-18
tested_against: "evaluation battery over synthetic safety scenarios"
---

# Safety Eval Evidence Exercise

This exercise uses fictional safety tests. No API key, model provider, or security scanner is needed.

Goal: decide whether a safety failure should block release, route to an owner, or become a new guardrail.

## Files

- [`safety-tests.jsonl`](safety-tests.jsonl): fictional safety eval cases.

## JSONL Shape

Common fields: `event`, `trace_id`, `case`, `source`, `validator`, `verdict`, `matched_policy`, `fail_closed`, `decision`, `owner`, and `next_action`. Optional fields such as `repair_attempt` appear only when relevant to failure repair.

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

## Extended Exercises

1. Design a follow-up trace that exercises the same pattern against the [gate reference material](../../labs/l5/pattern_eval_gate/README.md).
2. Swap the target scenario for a different domain and list the three decisions that would change.

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root (its `check_examples_jsonl` step also runs in CI). To practice a different policy, change one rule, redo the answers, and compare outcomes.

## Learning Outcomes

- Safety evals should test injection, leakage, refusal, harm, and hallucination separately.
- A guardrail pass is evidence, not an opinion.
- Fail-closed decisions should be explicit when evidence is missing.
- Production traces can become reviewable eval cases after redaction.

## Related Reading

- [`../../docs/en/production/safety-checklist.md`](../../docs/en/production/safety-checklist.md)
- [`../../docs/en/production/evals-playbook.md`](../../docs/en/production/evals-playbook.md)
- [`../../docs/en/tutorials/open-source-pattern-matrix.md`](../../docs/en/tutorials/open-source-pattern-matrix.md)
