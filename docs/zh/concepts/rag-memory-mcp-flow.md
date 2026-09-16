---
i18n-key: concepts-rag-memory-mcp-flow
last-synced: 2026-09-16
validated_date: 2026-09-16
---

RAG、记忆、多 Agent、MCP 流程

生产 Agent 系统通常组合多个子系统。理解数据流比记框架名字更重要。

## 流程

1. 用户 query 进入 gateway。
2. Gateway 检查 auth、rate、safety。
3. RAG 检索相关文档。
4. 记忆 提供用户、任务或组织上下文。
5. Planner 选择 tool、subagent 或 answer path。
6. MCP 或 tool gateway 暴露工具和外部数据源。
7. 多 Agent 组件分解、验证或专门化处理工作。
8. Evaluation 和 observability 记录质量、延迟、成本和安全信号。

## 数据归属

| Source | 负责 | 风险 |
| --- | --- | --- |
| RAG | 当前问题的证据 | stale 或 irrelevant documents |
| 记忆 | 持久上下文 | privacy、stale facts、overgeneralization |
| Tool gateway | 外部动作和状态 | permission mistakes、side effects |
| Planner | 步骤选择和路由 | wrong route、loops、overconfidence |
| Observability | trace、cost、latency、errors | incomplete trace、missing fields |

## 设计规则

- Retrieval 应围绕问题 scoped。
- 记忆 是隐私敏感的。
- Subagent 职责必须明确。
- Tool inputs/outputs 要谨慎记录。
- 用 eval sets 捕捉回归。
- Evidence 和 generated text 要分离。

## 失败排查顺序

1. 用户请求是否信息足够？
2. Retrieval 是否返回正确 source？
3. 记忆 是否引入 stale/private context？
4. Planner 是否选择正确路径？
5. Tool 是否执行正确动作？
6. Verification 是否在回答前捕获错误？
7. Trace 是否完整？

