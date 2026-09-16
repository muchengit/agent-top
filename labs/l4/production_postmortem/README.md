---
title: Production Postmortem Template Lab
capability_level: L4
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L4 Lab: Production Postmortem Template

## Goal

Turn a production failure into a structured postmortem with root causes, measurable action items, evaluation coverage, safety controls, and rollback planning.

## Prerequisites

- L0 through L3 completed.
- Basic understanding of evaluation, observability, and rollback.
- Python 3.10+.

## Run

```bash
python -m unittest labs.l4.production_postmortem.test_lab
```

## Production Checklist

- Auth and permissions.
- Rate limits.
- Cost guardrails.
- Evaluation set.
- Observability traces.
- Rollback plan.

## What This Lab Teaches

- A postmortem must name root causes, not just summarize symptoms.
- Action items need owners, due dates, and type labels.
- Rollback, evaluation, and safety controls are part of production readiness.
- Missing coverage should be surfaced explicitly.

## Reference Template

See [`../../../templates/postmortem-template.md`](../../../templates/postmortem-template.md).

## Common Pitfalls

- Writing only a summary without root causes.
- Creating action items without owners or due dates.
- Skipping rollback, evaluation, or safety-control follow-up.

## Self-Check

1. What makes a postmortem actionable?
2. What coverage is missing if action items have no owner?
3. Why are rollback and evaluation plans part of production readiness?
