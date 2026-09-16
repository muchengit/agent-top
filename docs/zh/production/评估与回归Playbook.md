---
title: 评估与回归 Playbook
validated_date: 2026-09-17
i18n-key: production-evals-playbook
last-synced: 2026-09-17
---

# 评估与回归 Playbook

用这个 Playbook 把一个变更转成可测量的发布决策。

## 什么时候使用

在修改 prompt、model、tool、retrieval、memory、routing、guardrail 或生产发布逻辑前使用。

## 1. 定义变更面

列出改动和可能破坏的地方。

| Change | Risk Area | Eval Needed | Owner |
| --- | --- | --- | --- |
| Prompt | answer quality、refusal、citations | golden prompts + safety |  |
| Model | format drift、latency、cost | golden prompts + latency/cost |  |
| Tool schema | invalid args、denied tools | tool usage |  |
| Retrieval | missing/stale sources | citation 和 refusal |  |
| Memory | stale preferences | conflict 和 expiry |  |
| Router | wrong specialist | route decision |  |
| Guardrail | false block/miss | safety 和 usability |  |

## 2. 最小 Eval Matrix

每个 Agent 变更至少覆盖这些行：

| Eval Class | Example Case | Expected Result | Blocking? |
| --- | --- | --- | --- |
| Golden path | 核心用户任务 | 用必要证据回答 | Yes |
| Missing evidence | 未检索到来源 | 拒绝或澄清 | Yes |
| Stale source | 旧政策来源 | 不从 stale source 回答 | Yes |
| Tool failure | tool timeout/error | 安全 fallback 或 escalation | Yes |
| Destructive action | delete/refund/request | 执行前需要 approval | Yes |
| Prompt injection | 检索文档试图改 policy | 忽略注入指令 | Yes |
| Ambiguous request | 缺用户身份或意图 | 澄清 | No |
| Cost/latency | 长 tool loop | 遵守预算或降级 | 超 gate 时 Yes |

## 3. 编写用例

每个 eval case 应包含：

- `id`：稳定名称。
- `input`：用户请求。
- `context`：来源、记忆、工具可用性。
- `expected_action`：answer、clarify、refuse、tool、escalate。
- `expected_evidence`：source IDs、tool result 或 trace fields。
- `blocking`：失败是否阻断发布。

## 4. 运行并记录

用 L4 regression gate Lab 作为确定性基线：

```bash
python -m unittest labs.l4.regression_gate.test_lab
```

记录：

- 总 case 数。
- 各类 pass/fail。
- Blocking failures。
- Cost 和 latency budget 状态。
- Rollback 是否可用。
- Trace 是否完整。

## 5. 发布决策

只有所有 blocking gates 通过才发布。

| Decision | 使用场景 |
| --- | --- |
| Ship | 无 blocking failures；预算通过；rollback ready |
| Canary | 有非阻断问题但风险可控 |
| Block | 有 critical safety、destructive action、missing trace 或 missing rollback |
| Rollback | 生产证据显示不可接受 regression |

## 6. 失败处理

每个 failure 必须变成以下之一：

- 新 eval case。
- Guardrail 修改。
- Trace field。
- Rollback note。
- Product decision。
- Postmortem action item。

## 7. 报告模板

可复制模板见 [`../../../templates/eval-report-template.md`](../../../templates/eval-report-template.md)。结构示例：

```markdown
# Eval Report

- Change:
- Date:
- Owner:
- Eval matrix version:

## Results
- Cases passed:
- Cases failed:
- Blocking failures:
- Safety failures:
- Tool failures:
- Retrieval failures:
- Cost status:
- Latency status:
- Trace completeness:
- Rollback ready:

## Decision
Ship / canary / block / rollback

## Follow-Up
- Owner:
- Due date:
- Regression case added:
```

## 相关页面

- 评估清单：[`评估清单.md`](评估清单.md)
- 生产清单：[`../quick-reference/生产清单.md`](../quick-reference/生产清单.md)
- 回归门禁 Lab：[`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md)
