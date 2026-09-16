# Agent Design Review Example: Customer Refund Assistant

## Scope

- Agent name: Customer Refund Assistant
- Author: Product engineering team
- Review date: 2026-09-17
- Primary user: Support agent
- Business goal: Draft and validate refund actions for approved support cases.
- Success metric: 95% of eligible refunds are drafted correctly; 0 unauthorized refunds execute.
- Non-goals: Replace policy judgment; process fraud investigation.
- Denied actions: Delete account, waive policy without manager approval, refund above threshold without approval.

## Architecture Choice

- System shape: Tool-using Agent with deterministic verifier.
- Why this shape: Needs policy lookup, order lookup, refund eligibility, and audit trail.
- Why not simpler: A single LLM call cannot safely inspect order state and policy evidence.
- Why not larger: A multi-agent team is not needed until independent verification or handoff improves measurable reliability.

## Tool Risk Table

| Tool | Purpose | Risk | Permission | Confirmation | Audit Fields | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| order.read | Fetch order status | Read | Customer scope | No | actor, order_id, timestamp | Allow |
| policy.read | Fetch refund policy | Read | Policy version scope | No | policy_id, version | Allow |
| refund.quote | Create non-mutating quote | Read | Support agent | No | quote_id, amount | Allow |
| refund.execute | Apply refund | Destructive | Manager approval | Yes | request_id, approver, idempotency_key | Block until approved |

## Evidence and Memory Rules

| Fact Type | Source | Freshness Rule | Citation Required | Conflict Rule |
| --- | --- | --- | --- | --- |
| Order state | order.read | Live read before quote | Yes | Live order beats cached order |
| Refund policy | policy.read | Current approved policy version | Yes | Policy beats memory |
| Agent notes | Memory | Last 30 days | No | Notes never override policy |

## Evaluation Gates

| Gate | Passing Condition | Owner |
| --- | --- | --- |
| Correctness | 20/20 eligible refund drafts cite order and policy | Support lead |
| Safety | 0 unauthorized `refund.execute` calls in eval | Security reviewer |
| Tool use | All `refund.execute` attempts require approval token | Tool owner |
| Retrieval / memory | Policy conflicts resolved by current policy | Knowledge owner |
| Cost / latency | p95 under 8 seconds with max 6 tool calls | Platform owner |
| Rollback | Prompt/tool/config rollback documented | Release manager |

## Review Result

- Verdict: Approve with conditions
- Required changes: add approval token for `refund.execute`; add regression eval for policy conflict; add idempotency key to refund quote trace.
- Owners and due dates: Support lead by day 2; Security reviewer by day 3; Platform owner by day 5.
- Follow-up issues: create eval fixtures for stale policy and duplicate refund attempts.
