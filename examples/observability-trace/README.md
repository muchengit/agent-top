# Observability Trace Exercise

This exercise gives you a fictional Agent trace. No API key, observability service, model call, or external dashboard is needed.

Goal: complete the trace, identify missing evidence, route the failure to an owner, and decide whether the incident should become an eval, guardrail, trace field, or rollback rule.

## Files

- [`trace-events.jsonl`](trace-events.jsonl): a partial trace.
- [`trace-template.jsonl`](trace-template.jsonl): start your completion here.

## Steps

1. Read the trace events.
2. Fill in:
   - `status`: `ok`, `blocked`, `error`, or `escalated`.
   - `missing_fields`: fields needed before release.
   - `owner`: `prompt`, `tool`, `retrieval`, `memory`, `guardrail`, or `runtime`.
   - `next_action`: `eval`, `guardrail`, `trace_field`, `rollback`, or `postmortem`.
3. Compare with the answer key below.
4. Change one rule: traces must redact private data before storage. Which fields must change?

## Answer Key

| Finding | Owner | Next action |
| --- | --- | --- |
| Final answer has no citations | retrieval | trace_field + eval |
| Tool call lacks approval evidence | guardrail | guardrail + rollback rule |
| Cost spike not captured per request | runtime | trace_field |
| User data appears unredacted | privacy | redaction policy + postmortem |

## Learning Outcomes

- A trace is a contract, not a console log.
- Missing fields are release blockers when they prevent diagnosis.
- Good traces route incidents to owners instead of debating who was right.
- Private data needs redaction and retention rules before it becomes evidence.

## Related Reading

- [`../../docs/en/production/observability-trace-contract.md`](../../docs/en/production/observability-trace-contract.md)
- [`../../docs/en/production/evals-playbook.md`](../../docs/en/production/evals-playbook.md)
- [`../../templates/observability-trace-template.md`](../../templates/observability-trace-template.md)
