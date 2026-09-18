# Compliance Review Exercise

This exercise uses fictional compliance-approval decisions. No API key, legal database, or external audit service is needed.

Goal: decide whether an evidence-gated approval can proceed, must request more evidence, or must be blocked with an audit trail.

## Files

- [`approval-decisions.jsonl`](approval-decisions.jsonl): evidence-gated approval decisions with policy checks.
- [`audit-events.jsonl`](audit-events.jsonl): audit log events recording who approved, what evidence was seen, and when.

## JSONL Shape

Each line is one JSON object with a stable `event`, `trace_id`, `request_id`, `policy`, `evidence_complete`, `evidence_types`, `approver_role`, `decision`, and `next_action`. Optional fields such as `missing_evidence` and `audit_ref` appear only when relevant.

## Steps

1. Read each approval decision.
2. Identify whether the evidence set satisfies the policy and whether the approver role is allowed.
3. Decide the next action: `approve`, `request_more_evidence`, `block`, or `escalate`.
4. For audit events, check that every approval has a matching audit record with approver, evidence, and timestamp.
5. Add one missing field for each blocked event.

## Answer Key

| Finding | Owner | Next action |
| --- | --- | --- |
| Evidence incomplete for policy | policy | request_more_evidence |
| Approver role not permitted | policy | block + escalate |
| Approval without audit record | audit | block + backfill audit |
| Evidence seen does not match decision | audit | block + postmortem |

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root. To practice a different policy, change one approval rule, redo the answers, and compare outcomes.

## Learning Outcomes

- Compliance approvals are release decisions gated by evidence and role, not by intent.
- Every approval must have a replayable audit trail: who, what evidence, and when.
- Missing evidence and wrong approver role are blocking conditions, not warnings.
