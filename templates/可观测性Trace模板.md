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


## 运行时证据

| Source | Tool | Tool version | Artifact / SHA | Release SHA | Finding | Decision | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `lint` / `profile` / `lockfile` / `workflow` / `error-group` / `ci` |  |  |  |  |  | `release` / `block` / `warn` / `route` |  |

运行时证据应说明：发布是否能在同一工具链下复现，成本或延迟热点是否能绑定到 commit，相似事故是否能聚合到同一 owner。

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
