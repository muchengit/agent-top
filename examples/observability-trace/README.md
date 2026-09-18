---
title: Observability Trace
capability_level: Example
validated_date: 2026-09-18
tested_against: "trace-completeness review on synthetic runtime evidence"
---

# Observability Trace Exercise

This exercise gives you a fictional Agent trace. No API key, observability service, model call, or external dashboard is needed.

Goal: complete the trace, identify missing evidence, route the failure to an owner, and decide whether the incident should become an eval, guardrail, trace field, or rollback rule.

## Files

- [`trace-events.jsonl`](trace-events.jsonl): a partial trace.
- [`release-gates.jsonl`](release-gates.jsonl): CI-first release evidence and gate decisions.
- [`runtime-evidence.jsonl`](runtime-evidence.jsonl): lint, profiling, dependency lock, workflow provenance, and error-group evidence.
- [`trace-template.jsonl`](trace-template.jsonl): start your trace-completion log here.

## JSONL Shape

Each line is one JSON object with a stable `finding` field plus the blank fields you fill in: `status`, `missing_fields`, `owner`, and `next_action`.

## Steps

1. Read the trace events.
2. Fill in:
   - `status`: `ok`, `blocked`, `error`, or `escalated`.
   - `missing_fields`: fields needed before release.
   - `owner`: `prompt`, `tool`, `retrieval`, `memory`, `guardrail`, or `runtime`.
   - `next_action`: `eval`, `guardrail`, `trace_field`, `rollback`, or `postmortem`.
3. Compare with the answer key below.
4. Add a `release.gate.checked` event for one gate. Decide whether it blocks release.
5. Change one rule: traces must redact private data before storage. Which fields must change?
6. Read `runtime-evidence.jsonl` and decide which evidence blocks release and which should route to runtime, release, or tooling ownership.

## Answer Key

| Finding | Owner | Next action |
| --- | --- | --- |
| Final answer has no citations | retrieval | trace_field + eval |
| Tool call lacks approval evidence | guardrail | guardrail + rollback rule |
| Cost spike not captured per request | runtime | trace_field |
| Release evidence lacks CI SHA | runtime | release gate + trace_field |
| Error group lacks fingerprint | runtime | trace_field + incident routing |
| Profile hotspot lacks release SHA | runtime | trace_field + cost owner |
| Lockfile lacks tool version | release | trace_field + rollback rule |

## Extended Exercises

1. Design a follow-up trace that exercises the same pattern against the [trace reference material](../../labs/l4/production_trace_integrity/README.md).
2. Swap the target scenario for a different domain and list the three decisions that would change.

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root (its `check_examples_jsonl` step also runs in CI). To practice a different policy, change one rule, redo the answers, and compare outcomes.

## Learning Outcomes

- A trace is a contract, not a console log.
- Missing fields are release blockers when they prevent diagnosis.
- Good traces route incidents to owners instead of debating who was right.
- CI evidence should point to the exact commit being evaluated, not just a branch name.
- Runtime evidence should explain whether a release can be replayed with the same tools and whether an incident can be grouped with similar traces.

## Related Reading

- [`../../docs/en/production/observability-trace-contract.md`](../../docs/en/production/observability-trace-contract.md)
- [`../../docs/en/production/evals-playbook.md`](../../docs/en/production/evals-playbook.md)
- [`../../templates/observability-trace-template.md`](../../templates/observability-trace-template.md)
