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

## Release Gate Evidence

| Evidence | Source | Result | Owner | Release decision |
| --- | --- | --- | --- | --- |


## Runtime Evidence

| Source | Tool | Tool version | Artifact / SHA | Release SHA | Finding | Decision | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `lint` / `profile` / `lockfile` / `workflow` / `error-group` / `ci` |  |  |  |  |  | `release` / `block` / `warn` / `route` |  |

Runtime evidence should answer whether the release can be replayed with the same tools, whether cost or latency hotspots can be tied to a commit, and whether similar incidents can be grouped into one route.

## CI First Evidence

- CI commit SHA:
- Required checks status:
- Dataset / fixture version:
- Regression diff reviewed:
- Owner approval:
- Rollback plan:
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
