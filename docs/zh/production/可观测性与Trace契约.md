---
title: 可观测性与 Trace 契约
validated_date: 2026-09-17
i18n-key: production-observability-trace-contract
last-synced: 2026-09-17
---

# 可观测性与 Trace 契约

可观测性不只是打日志。对 Agent 系统来说，可观测性是明确契约：当任何行为发生变化时，我们能知道用户问了什么、Agent 看到了哪些证据、调用了哪些工具、检查了哪些 guardrail、输出了什么答案，以及花了多少成本。

本页给出一套稳定的 Agent trace contract。它不绑定框架，可以用 Langfuse、OpenTelemetry GenAI、promptfoo 风格 eval report、内部日志，或者本地 JSONL 文件实现。

## 为什么需要这个契约

Demo 只需要给出答案。生产 Agent 要能回答、解释、验证、恢复和持续改进。Trace 是连接这些行为的证据层。

没有 trace 契约时：

- 事故复盘会变成“靠记忆争论”。
- 坏 prompt 看起来像模型故障。
- 工具 bug 看起来像规划 bug。
- 检索失败看起来像幻觉。
- 成本回归要等账单才发现。
- 安全事故无法复现。

有了 trace 契约后：

- 每个决策都能回放。
- 每个故障都能分派 owner。
- 每个事故都能转成 eval、guardrail、trace field 或 rollback rule。

## Trace 范围

一个 trace 应覆盖一次用户可见请求，即使它包含多轮、多工具、多检索、memory write 和 retry。

必需层级：

| 层级 | 示例 | 是否必需 |
| --- | --- | --- |
| Request | 用户请求、session id、tenant、locale | 是 |
| Plan | 考虑的步骤、选择动作、stop condition | 非简单 Agent 系统必需 |
| Retrieval | query、source ids、freshness、permission state | 使用 RAG 或证据时必需 |
| Tool | tool 名称、版本、参数、结果、latency | 调用工具时必需 |
| Guardrail | check 名称、verdict、matched policy、remediation | 安全相关动作必需 |
| Memory | read/write/delete、owner、reason | 涉及 memory 时必需 |
| Answer | final text、citations、refusal reason、confidence | 是 |
| Runtime | model、prompt version、latency、tokens、cost | 生产必需 |
| Incident | root cause、owner、rollback、follow-up eval | 事故后必需 |

## 稳定事件类型

事件名保持稳定，方便跨时间过滤和比较：

- `request.received`
- `plan.selected`
- `retrieval.queries`
- `retrieval.results`
- `tool.called`
- `tool.result`
- `guardrail.checked`
- `memory.read`
- `memory.write`
- `memory.deleted`
- `answer.generated`
- `answer.delivered`
- `error.raised`
- `release.gate.checked`

## 必需字段

每个 trace 至少包含：

```json
{
  "trace_id": "stable request id",
  "session_id": "user or conversation id",
  "tenant_id": "workspace or account scope",
  "request": "normalized user request",
  "prompt_version": "system/user prompt version",
  "model": "model name and setting",
  "plan": "selected steps and stop condition",
  "tools": [],
  "retrievals": [],
  "guardrails": [],
  "memory": [],
  "answer": {
    "text": "final answer",
    "citations": [],
    "refusal_reason": "none or reason"
  },
  "latency_ms": 0,
  "tokens": {},
  "cost": {},
  "status": "ok|blocked|error|escalated"
}
```

不要把 secret、完整私有记录或未脱敏客户数据写入 trace。存储 source id、policy name 和有限 excerpt 就够诊断。

## PII 与隐私规则

- secret 进入 trace 前必须脱敏。
- 原始客户数据默认不进入 trace。
- 只保留诊断需要的证据：source id、timestamp、permission state、policy name、bounded excerpt。
- 敏感字段要标注 retention class。
- 用户数据删除时，对应 trace evidence 也要删除或过期。

## 故障类型与 Owner

用 trace 字段快速分派事故：

| 故障 | Owner | 先看的字段 |
| --- | --- | --- |
| 缺少 citation | Retrieval 或 answer policy | `retrieval.results`、`answer.citations` |
| 工具未审批即调用 | Tool policy 或 MCP boundary | `tool.called`、`guardrail.checked` |
| memory preference 错 | Memory lifecycle | `memory.read`、`memory.write` |
| prompt regression | Prompt owner | `prompt_version`、eval fixture result |
| cost spike | Runtime 或 planner | `tokens`、`cost`、`plan.selected` |
| 缺少发布证据 | Release owner | `release.gate.checked`、CI commit SHA、dataset version、rollback plan |

## 发布门禁

出现以下情况，生产发布应失败：

- 必需 trace 字段缺失。
- trace retention 或 redaction policy 未定义。
- tool call 没有 risk classification。
- retrieval result 没有 source version 或 permission state。
- factual claim 的最终答案没有证据链接。
- 每个请求没有采集 cost 和 latency。

## 什么叫“好”

好的 Agent trace 能让队友不用重新问模型，直接回答：

1. 用户问了什么？
2. 当时有哪些证据？
3. 调用了哪些工具？
4. 哪个 policy 允许或阻止了动作？
5. Agent 最终回答了什么？
6. 花了多少成本？
7. 和上一个可用版本相比，什么变了？
8. 哪个 eval、guardrail 或 rollback action 能防止复发？

## 相关

- [`../concepts/核心Agent实施手册.md`](../concepts/核心Agent实施手册.md)
- [`评估与回归Playbook.md`](评估与回归Playbook.md)
- [`安全清单.md`](安全清单.md)
- [`../../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md)
- [`../../../templates/可观测性Trace模板.md`](../../../templates/可观测性Trace模板.md)
