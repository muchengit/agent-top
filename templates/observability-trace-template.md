---
title: Observability Trace Template
validated_date: 2026-09-17
tested_against: "JSONL + local docs review"
---

# Observability Trace Template

## Trace Summary

- Trace ID:
- Session ID:
- Tenant / workspace:
- Date:
- Prompt version:
- Model:
- Status: `ok` / `blocked` / `error` / `escalated`

## Request

- User request:
- Normalized intent:
- Required evidence:

## Evidence

| Source ID | Type | Freshness | Permission state | Used in answer |
| --- | --- | --- | --- | --- |

## Tool Calls

| Tool | Risk | Parameters | Result | Approval / audit |
| --- | --- | --- | --- | --- |

## Guardrails

| Check | Verdict | Policy | Remediation |
| --- | --- | --- | --- |

## Memory

- Memory read:
- Memory written:
- Memory deleted:
- Owner and purpose:

## Answer

- Final answer:
- Citations:
- Refusal reason, if any:
- Confidence / limitations:

## Runtime

- Latency:
- Tokens:
- Cost:
- Retry count:

## Incident Follow-Up

- Root cause:
- Owner:
- Rollback:
- New eval / guardrail / trace field:
- Due date:
