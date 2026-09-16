# Agent 设计审查范例：客服退款助手

## 范围

- Agent 名称：Customer Refund Assistant
- 作者：Product engineering team
- 审查日期：2026-09-17
- 主要用户：Support agent
- 业务目标：为已批准的支持工单起草并校验退款动作。
- 成功指标：95% 的合格退款被正确起草；0 次未授权退款执行。
- Non-goals：替代政策判断；处理欺诈调查。
- 禁止动作：删除账号、无经理审批豁免政策、超过阈值直接退款。

## 架构选择

- System shape: Tool-using Agent + deterministic verifier
- 为什么这样选：需要 policy lookup、order lookup、eligibility 和 audit trail。
- 为什么不选更简单方案：Single LLM call 无法安全检查订单状态和政策证据。
- 为什么不选更复杂方案：在验证或 handoff 能可衡量提升可靠性前，不需要 multi-agent。

## 工具风险表

| Tool | 用途 | Risk | 权限 | 确认 | 审计字段 | 决策 |
| --- | --- | --- | --- | --- | --- | --- |
| order.read | 获取订单状态 | Read | Customer scope | 否 | actor, order_id, timestamp | Allow |
| policy.read | 获取退款政策 | Read | Policy version scope | 否 | policy_id, version | Allow |
| refund.quote | 创建非 mutation quote | Read | Support agent | 否 | quote_id, amount | Allow |
| refund.execute | 执行退款 | Destructive | Manager approval | 是 | request_id, approver, idempotency_key | 审批前 Block |

## 证据和记忆规则

| 事实类型 | 来源 | Freshness 规则 | 是否 citation | 冲突规则 |
| --- | --- | --- | --- | --- |
| 订单状态 | order.read | Quote 前 live read | 是 | Live order 优先于 cached order |
| 退款政策 | policy.read | 当前 approved policy version | 是 | Policy 优先于 memory |
| Agent notes | Memory | 最近 30 天 | 否 | Notes 不能覆盖 policy |

## 评估门禁

| Gate | 通过条件 | Owner |
| --- | --- | --- |
| Correctness | 20/20 合格退款草稿引用 order 和 policy | Support lead |
| Safety | Eval 中 0 次未授权 `refund.execute` | Security reviewer |
| Tool use | 所有 `refund.execute` 都需要 approval token | Tool owner |
| Retrieval / memory | Policy conflicts 由 current policy 解决 | Knowledge owner |
| Cost / latency | p95 低于 8 秒，最多 6 次 tool calls | Platform owner |
| Rollback | Prompt/tool/config rollback 文档化 | Release manager |

## 审查结果

- Verdict: Approve with conditions
- 必须修改：为 `refund.execute` 添加 approval token；为 policy conflict 添加 regression eval；为 refund quote trace 添加 idempotency key。
- Owner 和 due date：Support lead 第 2 天；Security reviewer 第 3 天；Platform owner 第 5 天。
- Follow-up issues：创建 stale policy 和 duplicate refund attempts 的 eval fixtures。
