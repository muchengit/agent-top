---
title: 可回放 Eval 和 Trace 模板
validated_date: 2026-09-17
---

# 可回放 Eval 和 Trace 模板

当 eval 或 trace 结果在发布、事故复盘、或 L5 证据包中需要被重放时，使用这个模板。

## 运行上下文

- Run date:
- Operator:
- Repository branch:
- Commit SHA:
- Model / prompt version:
- Tool versions:
- Fixture / dataset version:
- Time window:

## 必交产物

- Request / input fixture:
- Expected output or rubric:
- Trace schema or trace file:
- Eval config:
- Guardrail policy:
- Rollback 或 mitigation note:

## 回放步骤

| Step | Command or action | Required result | Owner | Backup |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |
| 2 |  |  |  |  |

## 退出条件

- [ ] 回放使用同一 fixture，或明确批准了替代 fixture。
- [ ] 回放记录 commit SHA、tool versions、dataset version。
- [ ] 回放输出包含 expected answer、blocked case、或 refusal case。
- [ ] 回放输出包含 trace 字段：request、evidence、tool calls、guardrails、memory、cost、latency。
- [ ] 回放标明残余风险和 owner。

## 证据输出

- Raw output:
- Trace artifact path:
- Eval artifact path:
- Screenshot or log path, if any:
- Reviewer notes:
