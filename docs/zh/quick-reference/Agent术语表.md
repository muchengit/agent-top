---
i18n-key: quick-reference-agent-glossary
last-synced: 2026-09-16
validated_date: 2026-09-16
---

# Agent 术语表

这份术语表用于统一文档、Lab、面试和生产 incident 的表述。

## 核心术语

| Term | 含义 |
| --- | --- |
| Agent | 使用 LLM、工具、记忆、规划和控制循环完成任务的系统 |
| 感知 | 将用户输入、工具结果和检索 context 变成可用状态 |
| 规划 | 决定下一个 action 或 reasoning step |
| Action | 工具调用、检索请求、消息或系统动作 |
| Observation | 工具、检索、模型或环境返回的证据 |
| ReAct | 推理和动作交替的循环 |
| Tool | 有类型化输入输出的外部函数或动作 |
| MCP | 连接 LLM app 和 MCP server 的标准协议；MCP server 可暴露 tools、resources、prompts、schemas 和 context |
| RAG | 使用检索源的生成 |
| 记忆 | 跨轮或跨会话存储的 context |
| Guardrail | 防止不安全行为的规则 |
| Eval | 衡量 Agent 行为的测试 |
| Trace | prompt、tool calls、decisions、outcomes 记录 |
| Rollback | 恢复已知安全行为的路径 |

## 生产术语

| Term | 含义 |
| --- | --- |
| Contract | Agent 或工具的 input/output/failure-mode 约定 |
| Handoff | 把任务状态传给另一个 Agent 或阶段 |
| Verifier | 检查 evidence 和 recommendations 的组件或 Agent |
| Supervisor | 路由任务给 worker 并执行 stop conditions 的编排者 |
| Human-in-the-loop | 人工审批或复核高风险步骤的流程 |
| Confidence | 回答背后证据强度，不替代验证 |
| Citation | 连接到 claim 或 answer 的证据 |
| Fallback | evidence、tool 或 model 不足时的安全回答 |
| Idempotency | 工具可安全重试且不会重复副作用 |
| Regression Gate | 阻断 unsafe behavior 上线的发布门禁 |
| Blast Radius | 失败影响的、数据或系统范围 |
| Postmortem | 把 incident 转成 prevention actions 的无责复盘 |

## 决策术语

| Term | 含义 |
| --- | --- |
| Fail closed | 停止或拒绝，而不是带着 unsafe assumptions 继续 |
| Trade-off | accuracy、latency、cost、safety、maintainability 的显式权衡 |
| Stable pattern | 跨框架仍然有效的设计思想 |
| Framework boundary | 应隔离在 Lab 里的框架 API 细节 |
| Validated date | 文档或示例被检查的日期 |
| Tested against | 可执行示例对应的版本或环境锚点 |

## 审查问题

- 每个外部 action 是否有 typed tool contract？
- 证据密集的回答是否有 verifier？
- evidence 缺失时是否有 refusal path？
- 外部副作用是否有 rollback path？
- 行为能否用 eval 测，而不是靠猜？
