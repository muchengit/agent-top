---
title: Agent Design Review Workshop
validated_date: 2026-09-17
i18n-key: concepts-design-review-workshop
last-synced: 2026-09-17
---

# Agent Design Review Workshop

Use this workshop to review one Agent idea in about 45 minutes.

## Roles

- Author: explains the proposed Agent.
- Challenger: asks boundary and failure questions.
- Reviewer: checks evidence, safety, and operations.
- Scribe: writes decisions and owners.

## Inputs

- One-page system goal.
- User and tenant model.
- Tool list with read/write/destructive labels.
- Data sources and freshness rules.
- Known failure examples.
- Current or proposed eval plan.

## 45-Minute Agenda

| Time | Activity | Output |
| --- | --- | --- |
| 5 min | State the task and non-goals | One-sentence success metric |
| 10 min | Map architecture and data flow | Minimal system diagram |
| 10 min | Review tools, MCP, and permissions | Risk table |
| 10 min | Review memory, evidence, and hallucination risks | Source precedence rules |
| 5 min | Review evals and release gates | Pass/fail conditions |
| 5 min | Decide next action | Approve, conditions, rework, or stop |

## Questions That Usually Improve Design

- Can the system say "I do not know" without failing?
- Which action is irreversible?
- What happens if two tools disagree?
- Which claim requires a citation?
- What trace fields would prove the incident path?
- What changes require rollback?
- What would break if model confidence drops?

## Output Template

```markdown
# Review Result

- Verdict: Approve / Approve with conditions / Rework / Stop
- Success metric:
- Architecture choice:
- Tool risk decisions:
- Required evidence:
- Eval gates:
- Rollback path:
- Owners and dates:
```

## Related Pages

- Checklist: [`design-review-checklist.md`](design-review-checklist.md)
- Implementation guide: [`implementation-guide.md`](implementation-guide.md)
- System blueprint: [`agent-system-blueprint.md`](agent-system-blueprint.md)
