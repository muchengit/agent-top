---
title: 可观测性 Trace 模板
validated_date: 2026-09-17
tested_against: "JSONL + 本地文档审查"
---

# 可观测性 Trace 模板

## Trace 摘要

- Trace ID:
- Session ID:
- Tenant / workspace:
- 日期:
- Prompt 版本:
- Model:
- 状态: `ok` / `blocked` / `error` / `escalated`

## 请求

- 用户请求:
- 规范化意图:
- 需要的证据:

## 证据

## 发布证据与门禁

| Evidence | Source | Result | Owner | 发布决策 |
| --- | --- | --- | --- | --- |

## CI-first 证据

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
- Owner 与 purpose:

## 答案

- 最终答案:
- Citations:
- Refusal reason（如有）:
- Confidence / limitations:

## Runtime

- Latency:
- Tokens:
- Cost:
- Retry count:

## 事故后续

- Root cause:
- Owner:
- Rollback:
- 新增 eval / guardrail / trace field:
- Due date:
