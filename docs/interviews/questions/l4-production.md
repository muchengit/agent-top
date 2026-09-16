---
title: L4 Production Questions
validated_date: 2026-09-16
---

# L4 Production Questions

## 1. What do you do before shipping an Agent feature?

Expected answer:

- Auth and permissions are defined.
- Rate limits and cost guardrails exist.
- Eval set is green.
- Observability traces prompt, tool, answer, latency, and cost.
- Rollback plan is documented.

Listen for:

- Concrete checklist thinking.
- Operational ownership.

## 2. A customer reports the Agent made the wrong account change.

Expected answer:

- Stop the unsafe action path.
- Inspect traces and prompts.
- Identify root cause in data, tool schema, or policy.
- Add regression eval and prevention controls.
- Document postmortem.

Listen for:

- Incident response discipline.
- Root cause over blame.
