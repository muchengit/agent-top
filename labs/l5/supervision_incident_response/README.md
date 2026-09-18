---
title: L5 Lab: Supervision and Incident Response
capability_level: L5
validated_date: 2026-09-18
i18n-key: l5-supervision-incident-response
last-synced: 2026-09-18
tested_against: "python 3.10+"
---

# L5 Lab: Supervision and Incident Response

## Goal

Build a deterministic production supervisor for a multi-agent fleet: aggregate worker heartbeats and incident reports, decide whether to continue, escalate, pause, or roll back, and produce an action plan with owners and rollback targets.

## Prerequisites

- L4: productionized Agent systems with trace integrity and release gates.
- Python 3.10+
- Familiarity with multi-agent scheduling and observability contracts.

## Run

```bash
python -m unittest labs.l5.supervision_incident_response.test_lab
```

## What This Lab Teaches

- Supervision is a deterministic state machine, not another LLM conversation.
- Incident response needs owners, rollback targets, and explicit decisions.
- Critical incidents and dead workers change the release posture.

## Common Pitfalls

- Treating warnings as informational until they exceed the threshold.
- Rolling back the entire fleet when one trace family is affected.
- Forgetting that resolved incidents should leave the open set.

## Self-Check

1. When does a supervisor choose rollback instead of escalation?
2. Why should action items carry a rollback target?
3. How would you add a human-approval step before rollback?

## Bilingual Notes

The Chinese mirror lives at [`README.zh-CN.md`](README.zh-CN.md) with the same `i18n-key`. Keep both mirrors in sync when changing this lab.
