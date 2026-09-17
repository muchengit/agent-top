---
title: Eval and Trace Replay Template
validated_date: 2026-09-17
---

# Eval and Trace Replay Template

Use this when an eval or trace result must be replayed before release, incident review, or L5 evidence packaging.

## Run Context

- Run date:
- Operator:
- Repository branch:
- Commit SHA:
- Model / prompt version:
- Tool versions:
- Fixture / dataset version:
- Time window:

## Required Artifacts

- Request / input fixture:
- Expected output or rubric:
- Trace schema or trace file:
- Eval config:
- Guardrail policy:
- Rollback or mitigation note:

## Replay Steps

| Step | Command or action | Required result | Owner | Backup |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |
| 2 |  |  |  |  |

## Exit Criteria

- [ ] The replay uses the same fixture or an explicitly approved replacement.
- [ ] The replay records commit SHA, tool versions, and dataset version.
- [ ] The replay output includes expected answer, blocked case, or refusal case.
- [ ] The replay output includes trace fields: request, evidence, tool calls, guardrails, memory, cost, and latency.
- [ ] The replay identifies residual risk and owner.

## Evidence Output

- Raw output:
- Trace artifact path:
- Eval artifact path:
- Screenshot or log path, if any:
- Reviewer notes:
