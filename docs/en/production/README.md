---
title: Production Guides Index
validated_date: 2026-09-16
i18n-key: production-readme
last-synced: 2026-09-16
---

# Production Guides

Production guides are the readiness layer for Agent systems.

## Guides

- [`evals-checklist.md`](evals-checklist.md)
- [`safety-checklist.md`](safety-checklist.md)
- [`quarterly-maintenance.md`](quarterly-maintenance.md)

## Minimum Production Bar

Before release, confirm:

- Auth and permissions are explicit.
- Tool allowlist and risk classification exist.
- Destructive actions require confirmation or approval.
- Safety evals pass.
- Trace schema includes request, tool, retrieval, and final-answer fields.
- Rollback plan is documented and tested.
- Cost and latency budgets are defined.

## Incident Response Loop

1. Disable the risky action path.
2. Freeze writes if data integrity is uncertain.
3. Inspect traces and tool logs.
4. Identify root cause.
5. Add a regression eval.
6. Document a postmortem with owner, due date, and prevention action.

## Related Case

- [`../cases/production-regression-gate.md`](../cases/production-regression-gate.md)
