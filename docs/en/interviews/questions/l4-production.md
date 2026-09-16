---
title: L4 Production Questions
validated_date: 2026-09-16
i18n-key: interviews-questions-l4-production
last-synced: 2026-09-16
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

Follow-up:

- Which item would block release by itself?

## 2. A customer reports the Agent made the wrong account change.

Expected answer:

- Stop the unsafe action path.
- Inspect traces and prompts.
- Identify root cause in data, tool schema, policy, or permission boundary.
- Add regression eval and prevention controls.
- Document postmortem with owner, due date, and rollback plan.

Listen for:

- Incident response discipline.
- Root cause over blame.
- Follow-up ownership.

Follow-up:

- How do you prevent the same failure in a different tenant?

## 3. How do you handle a model version change?

Expected answer:

- Treat it as a release.
- Run golden and safety evals.
- Compare latency, cost, refusal behavior, and tool-call behavior.
- Shadow or canary before full rollout.
- Keep rollback to the prior model or prompt path.

Listen for:

- Model change as operational risk.
- Regression awareness.
- Canary and rollback thinking.

Follow-up:

- What eval would block a new model version?

## 4. How do you design an incident severity model for Agent systems?

Expected answer:

- SEV1: user harm, data integrity, safety bypass, or broad outage.
- SEV2: degraded quality, wrong answer at meaningful scale, or tool failure with workaround.
- SEV3: localized defect with small blast radius.
- SEV4: cosmetic or low-risk regression.

Listen for:

- Safety and data integrity first.
- Blast radius reasoning.
- Clear response paths.

Follow-up:

- What should happen if a SEV1 action item becomes overdue?

## 5. How do you balance cost and quality?

Expected answer:

- Profile cost by route, tool, model, and prompt length.
- Use simpler models or deterministic paths where safe.
- Cache stable retrieval or template outputs.
- Escalate expensive reasoning only when needed.
- Track quality regressions alongside cost.

Listen for:

- Cost treated as a metric, not afterthought.
- Guardrails before optimization.
- Clear rollout control.

Follow-up:

- What optimization would you avoid before a safety incident?
