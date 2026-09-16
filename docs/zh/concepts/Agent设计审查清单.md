---
title: Agent 设计审查清单
validated_date: 2026-09-16
i18n-key: concepts-design-review-checklist
last-synced: 2026-09-16
---

# Agent 设计审查清单

用这份清单在实现前、代码评审、上线前或面试准备时审查 Agent 设计。

## 0. 审查输出

一次好的设计审查最终应给出四个结论之一：

- **Approve**：可以按常规监控继续构建或发布。
- **Approve with conditions**：补上指定条件、owner 和日期后可发布。
- **Rework**：架构存在未解决的 correctness、safety 或 maintainability 风险。
- **Stop**：任务不需要 Agent，或风险不可接受。

可复制模板见 [`../../../templates/agent-design-template.md`](../../../templates/agent-design-template.md)。

审查模板：

```markdown
# Agent Design Review

## Scope
- User:
- Business goal:
- Non-goals:

## Decision
- Verdict: Approve / Approve with conditions / Rework / Stop
- Required conditions:
- Owners and dates:

## Evidence
- Eval plan:
- Safety controls:
- Observability plan:
- Rollback plan:
- Cost and latency budget:
```

## 1. 需求与非目标

必须问清楚：

- 用户是谁，必须完成什么任务？
- 成功条件能否用一句可衡量标准描述？
- 哪些事情明确不在范围内？
- Agent 不确定时怎么处理？
- 动作不可逆时怎么处理？

红旗：

- 目标只是“做一个 AI”，没有任务级成功指标。
- 系统期望只用 prompt 处理安全、权限或业务规则。
- 没有 refusal path。

## 2. 系统形态

选择能解决问题的最小形态：

| 形态 | 适用场景 | 避免场景 |
| --- | --- | --- |
| Single LLM call | 直接回答，无需外部状态 | 需要证据、工具或 side effects |
| ReAct loop | 需要观察 tool result 后调整 | tool result 不可信且没有 verifier |
| RAG Agent | 答案依赖私有、当前或大规模文档 | 无法衡量检索质量 |
| Tool-using Agent | 需要查询或修改外部系统 | 权限与审计边界不清 |
| Multi-agent system | 专业分工、验证或隔离有明确收益 | 单 Agent + tools 就足够 |

红旗：

- 还没诊断单 Agent 失败，就引入 multi-agent 复杂度。
- Orchestrator 管得太少，无法 stop、verify 或 escalate。
- 多个 Agent 共享 mutable state，但没有 owner。

## 3. 组件边界

每个组件都要写清：

- Owner。
- Inputs。
- Outputs。
- Required permissions。
- Failure modes。
- Observability fields。
- Rollback path。

生产 Agent 最低边界：

- Gateway：auth、rate limits、request size limits。
- Planner：stop conditions、max steps、budget awareness。
- Tool gateway：schema validation、allowlist、audit logs。
- Retriever：scope、freshness、citation contract。
- Memory：extraction、deduplication、expiry、deletion。
- Verifier：evidence checks、output policy、escalation。
- Evaluator：golden prompts、safety evals、regression gates。

## 4. 数据流与 context 归属

给每类事实指定来源：

| Fact type | Preferred source | Do not trust blindly |
| --- | --- | --- |
| Current user instruction | User turn | Old memory |
| Private knowledge | Scoped RAG | Model parametric memory |
| External state | Tool call | Cached prompt context |
| User preference | Memory | Unconfirmed inference |
| Safety decision | Guardrail or approval | Final model text |

审查问题：

- 最终回答能否说明每条事实来自哪里？
- stale memory 能否被检测并排除？
- tool results 是否可能和 retrieved documents 冲突？
- 回答前是否有 conflict-resolution rule？

## 5. Tool 与 MCP 设计

新增工具前定义：

- Tool name 和一句话用途。
- Input schema 和 output schema。
- read-only、write 或 destructive 分类。
- Auth 和 tenant scoping。
- Idempotency behavior。
- Timeout 和 retry policy。
- Audit fields。

红旗：

- 工具只在 prompt 里描述，没有 schema validation。
- destructive action 不需要确认即可调用。
- tool errors 直接变成 user-facing answer，没有解释。

## 6. 安全、权限与滥用案例

至少审查这些风险：

- 通过 retrieved documents 或 tool results 注入 prompt。
- Cross-tenant data retrieval。
- Overprivileged tools。
- write action 的 hidden side effects。
- Memory poisoning。
- Infinite escalation 或 retry loops。
- Sensitive output leakage。

必需控制：

- Retrieval 前做 auth checks。
- Tool execution 前做 auth checks。
- Tool allowlist 和 risk classification。
- destructive actions 需要 explicit approval。
- 需要证据或 citation 时做 output validation。
- 每个 user 和 tenant 有 rate 与 cost limits。

## 7. 实现前评估

先定义 evals，再决定最终 prompt：

- Golden prompts：核心 journey。
- Negative cases：Agent 应拒绝的问题。
- Tool-usage cases：invalid 或 missing parameters。
- Retrieval cases：stale、missing、conflicting sources。
- Safety cases：injection、privilege escalation、destructive action。
- Ambiguous requests：需要澄清的问题。

发布门禁：

- Safety failures block release。
- Missing trace fields block release。
- Missing rollback plan block release。
- Cost 或 latency 超预算必须显式审批。

## 8. Observability Contract

每个请求都应能追踪：

- Request ID 和 user/tenant ID。
- Prompt version 和 model version。
- Planner decisions 和 stop reason。
- Tool calls、arguments、result status、latency。
- Retrieved sources 和 freshness metadata。
- Memory reads 和 writes。
- Guardrail decisions。
- Final answer status。
- Token cost 和 total latency。

事故要求：

- 生产 incident 必须转化为 eval、guardrail、trace field、rollback path 或 postmortem action。

## 9. 成本与延迟预算

先做预算，再优化：

- 每个请求最大 steps。
- 每个请求最大 tool calls。
- p50 和 p95 latency targets。
- 每个 user、task、tenant 的 token budget。
- Retry budget。
- Escalation budget。

红旗：

- Retries 可以无限递归。
- Multi-agent routing 没有 maximum hop count。
- RAG retrieval 不受 relevance 或 token budget 约束。

## 10. Rollback 与变更管理

每类重大变更都要记录：

- 能回滚什么：prompt、model、tool、retrieval index、memory policy、router。
- 回滚期间如何保护用户。
- 如何用 traces 找到受影响请求。
- 谁能批准 release gate exception。

Rollback 应恢复 known-safe behavior，而不只是关闭失败功能。

## 审查评分表

| Area | Passing standard |
| --- | --- |
| Requirements | 用户、任务、成功指标、非目标清楚 |
| Shape | 选择最小可行架构 |
| Boundaries | 每个组件有 owner、inputs、outputs、failures |
| Data flow | 事实有 source precedence 和 conflict rules |
| Tools | schemas、permissions、audit、idempotency 已定义 |
| Safety | injection、privilege、memory、destructive risks 已处理 |
| Evals | correctness、safety、retrieval、tool、regression cases 存在 |
| Observability | 请求可被 traces replay |
| Cost/latency | budgets 和 caps 明确 |
| Rollback | 上线前有 known-safe path |
| Postmortem | incidents 转化为 prevention assets |

## 最终问题

批准前问一遍：

- 这个设计能否更简单？
- Agent 是否可能造成无法撤销的伤害？
- Agent 是否可能在没有证据时自信回答？
- bad prompt 或 model change 是否可能静默降低安全性？
- 现有 traces 是否足够调查 incident？
- 为什么这里必须用 Agent architecture，而不是普通 workflow？
