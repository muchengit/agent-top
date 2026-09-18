---
title: Release Gate Evidence
capability_level: Example
validated_date: 2026-09-18
tested_against: "replay of synthetic workflow and release-gate events"
---

# Release Gate Evidence Exercise

This exercise uses fictional GitHub Actions-style release evidence. No GitHub account, GitHub token, CI runner, API key, or external service is needed.

Goal: decide whether release gate evidence is complete enough to approve, block, or request more evidence.

## Files

- [`gate-events.jsonl`](gate-events.jsonl): fictional workflow-run evidence.

## JSONL Shape

Common fields: `event`, `trace_id`, `commit_sha`, `workflow_run_id`, `action_ref`, `setup_version`, `artifact`, `cache_key`, `decision`, and `owner`. Optional fields may include `artifact_sha`, `rollback`, and `missing_fields`.

## Steps

1. Read each gate event.
2. Decide whether it is ready for release.
3. Identify the owner: `ci`, `runtime`, `release`, `tooling`, or `security`.
4. Choose the next action: `approve`, `block`, `request_evidence`, or `rollback`.
5. For each blocked event, add one missing evidence field.

## Answer Key

| Finding | Owner | Next action |
| --- | --- | --- |
| CI action ref is not pinned | ci | block |
| Artifact decision lacks artifact SHA | release | request_evidence |
| Cache hit lacks cache key | tooling | request_evidence |
| Rollback target is missing | release | rollback |

## Extended Exercises

1. Design a follow-up trace that exercises the same pattern against the [gate2 reference material](../../labs/l4/regression_gate/README.md).
2. Swap the target scenario for a different domain and list the three decisions that would change.

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root (its `check_examples_jsonl` step also runs in CI). To practice a different policy, change one rule, redo the answers, and compare outcomes.

## Learning Outcomes

- Release evidence should point to exact commit and workflow-run evidence, not branch names.
- Pinned action refs and setup versions are part of reproducible release evidence.
- Artifact and cache decisions should record identity, ownership, and replayability.
- Missing CI evidence should block release or trigger a focused evidence request.

## Related Reading

- [`../../docs/en/production/evals-playbook.md`](../../docs/en/production/evals-playbook.md)
- [`../../docs/en/production/safety-checklist.md`](../../docs/en/production/safety-checklist.md)
- [`../../docs/en/tutorials/open-source-pattern-matrix.md`](../../docs/en/tutorials/open-source-pattern-matrix.md)
