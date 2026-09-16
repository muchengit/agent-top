---
title: Agent Safety Checklist
validated_date: 2026-09-16
i18n-key: production-safety-checklist
last-synced: 2026-09-16
---

# Agent Safety Checklist

Safety controls should protect users, data, and the Agent's ability to operate predictably.

## Required Controls

### Auth and Permissions

- Identify the user or tenant.
- Check authorization before retrieval.
- Check authorization before tool execution.
- Never rely only on the prompt for access control.

### Tool Safety

- Maintain a tool allowlist.
- Classify tools as read-only, write, or destructive.
- Require approval for destructive actions.
- Validate tool arguments before execution.
- Emit audit logs for tool calls.

### Input Validation

- Reject malformed inputs.
- Detect obvious prompt injection.
- Limit input size.
- Strip or ignore hidden control instructions when possible.

### Output Validation

- Reject unsupported claims when evidence is required.
- Block sensitive data leakage.
- Block final answers for missing critical evidence.
- Require citation or source references when configured.

### Memory Safety

- Scope memory by user, tenant, and purpose.
- Avoid storing secrets, credentials, or prohibited personal data.
- Make stale or conflicting memory visible.
- Support deletion or forgetting.

### Rate and Cost Limits

- Limit request rate by user and tenant.
- Limit tool-call count per request.
- Limit token spend per task.
- Stop escalation loops.

### Observability

- Log request id, prompt version, model version, tool calls, and final answer status.
- Redact secrets.
- Preserve enough trace to reproduce incidents.


## Guardrail Evidence

Safety checks should not only say “passed”. Each guardrail decision should record replayable evidence:

- `validator`: rule or model check name.
- `verdict`: `pass`, `fail`, `repair`, or `block`.
- `repair_attempt`: whether output repair was attempted and the repair budget.
- `matched_policy`: policy name matched, without secrets.
- `fail_closed`: whether uncertainty caused a fail-closed decision.
- `owner`: prompt, tool, retrieval, memory, runtime, or release owner.

Use these fields to answer: why did the system allow or block this action, and how will we prove similar issues are intercepted next time?

## Risk Classification

| Risk | Example | Required Control |
| --- | --- | --- |
| Low | Read-only lookup | Auth, trace, timeout |
| Medium | Ticket comment, preference write | Validation, rollback, audit |
| High | Billing, permission, deletion | Approval, idempotency, postmortem path |
| Critical | Data deletion, payment, credentials | Explicit human approval and full audit |

## Guardrails

- Block irreversible actions without confirmation.
- Reject malformed tool arguments.
- Redact sensitive data where possible.
- Log denied actions for auditability.
- Stop when a tool schema or permission result is ambiguous.
- Escalate when memory and retrieval conflict.

## Incident Controls

When safety is suspected:

1. Disable the risky action path.
2. Freeze writes if data integrity is in doubt.
3. Inspect traces and tool logs.
4. Add regression eval.
5. Write postmortem with owner and due date.
6. Roll back or patch with monitoring.
