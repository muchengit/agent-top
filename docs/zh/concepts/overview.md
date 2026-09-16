---
i18n-key: concepts-overview
last-synced: 2026-09-16
validated_date: 2026-09-16
---

Agent 概念总览

Agent 是使用 LLM、工具、记忆、规划和控制循环完成任务的系统。

关键点不是模型有魔法，而是系统控制模型：提供 context、校验动作、观察结果，并决定是否继续。

## 核心组件

### 感知

把用户输入、工具结果、检索文档和 observation 转成可用 context。

### 规划

决定下一步做什么。简单计划可以是 ReAct loop；复杂计划可以拆给 subagents。

### 工具使用

让 Agent 调用外部函数、API、数据库、shell 或 MCP。

### 记忆

存储跨轮或跨任务信息。短期记忆是会话状态；长期记忆跨会话持久化。

## 数据流

1. 用户请求进入。
2. Gateway 检查身份、权限、速率和输入限制。
3. 从 prompt、retrieval、memory、tool definitions 组装 context。
4. 模型提出 reasoning 和 tool calls。
5. Tool calls 被校验并执行。
6. 工具返回 observations。
7. Agent 更新状态，回答、澄清、升级或继续规划。
8. Observability 记录 prompt、tool calls、latency、cost 和 eval results。

## 第一性原则

- 明确状态优于隐藏 magic。
- 安全相关输出需要确定性检查。
- 小工具优于大而模糊的工具。
- 先 eval 再扩大复杂度。
- 高风险动作前先定义 rollback。
- 小范围记忆优于广泛记忆。

## 常见失败模式

- 用 context stuffing 代替 context selection。
- 无界 loop。
- 把 ambiguous tool result 当成成功。
- 把 memory 当事实。
- 默认 retrieval 总是新鲜。
- 只在 final prompt 里做安全检查。

