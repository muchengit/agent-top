---
title: Community Experiment Log
validated_date: 2026-09-18
i18n-key: community-experiment-log
last-synced: 2026-09-18
---

# Community Experiment Log

This log tracks experiment proposals for Agent-Top content. One experiment per quarter: propose, prototype, then promote or archive. Each entry records the candidate, the decision, and where the result landed.

## Goals

- Keep experiment output reviewable.
- Give every experiment an explicit promote or archive decision.
- Compare repetition to a stable baseline before calling a pattern reusable.

## Entry Format

| Field | Meaning |
| --- | --- |
| ID | Unique experiment number (`EX-001`-style). |
| Status | `proposed`, `in-progress`, `promoted`, `archived`. |
| Baseline | Existing behavior or metric before the experiment. |
| Prototype | File or Lab where the prototype lives. |
| Decision | Promote to content or archive with reason. |

## Current Experiments

| ID | Status | Baseline | Prototype | Decision |
| --- | --- | --- | --- | --- |
| EX-001 | promoted | No repeatable "pattern repetition" check | `labs/l5/pattern_eval_gate/` | Promote: gate now covers repetition scoring |
| EX-002 | promoted | Single-language pattern demos only | `labs/l5/multilingual_pattern_lab/` | Promote: five-language parity verified by smoke |
| EX-003 | promoted | Supervision documented, not executable | `labs/l5/supervision_incident_response/` | Promote: deterministic incident response tests now executable |
| EX-004 | promoted | Vibe Coding was guidance only, not testable | `labs/l5/vibe_coding_spec/` | Promote: prompt-readiness check is now a deterministic Lab |

## Repeating Protocol

When a community experiment validates a pattern, record its repetition count and evidence. A pattern is considered reusable only after the same behavior is reproduced across at least two independent traces or implementations, with a deterministic test in the repository.

## Policy

- Every quarter at least one experiment moves to `promoted` or `archived`.
- Promote only when the prototype passes repository checks and a deterministic test exists.
- Archive with a one-line reason; do not silently delete the prototype.
