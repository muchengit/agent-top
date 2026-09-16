---
i18n-key: concepts-agent-system-architecture
last-synced: 2026-09-16
validated_date: 2026-09-16
---

Agent 系统架构

大多数 Agent 教程最终都收敛到同样模式：LLM call、loop、RAG、tool use、memory、observability 和 multi-agent coordination。

## 1. 最小 LLM 调用

第一次构建块是带 user message 和 system prompt 的模型调用。

学习点：

- Token 和上下文限制。
- System prompt 与 user prompt 的区别。
- 直接回答不一定是最优路径。

## 2. 单 Agent Loop

单 Agent 使用 plan、act、observe、update、repeat。

学习点：

- Stop conditions。
- Max step limit。
- Tool result ambiguity。
- 每一步的 observability。

## 从第一次 LLM 调用到多轮 Agent

| 阶段 | 系统内容 | 学习者应证明 |
| --- | --- | --- |
| 第一次 LLM 调用 | request、system prompt、user message、response | 能解释 context 和输出形态 |
| 单轮循环 | tool、observation、下一步决策 | 能停止并从工具结果恢复 |
| 多轮 Agent | history、memory、tools、verification、escalation | 能解释每一轮为什么存在 |

## 3. 工具调用 Agent

Tool use 让模型成为系统参与者。工具提供外部事实、当前状态和副作用。

学习点：

- Tool schema validation。
- Role 和 tenant permissions。
- Read-only、write、destructive action 分类。
- 不可逆操作需要 confirmation。

## 4. RAG Agent

RAG 用检索源支撑回答。私有、当前或大规模知识尤其需要它。

学习点：

- Query planning。
- Chunking 和 retrieval。
- Source freshness。
- Evidence 缺失时 refusal。
- 第一轮检索失败时多轮搜索。

## 5. 记忆增强 Agent

记忆 添加跨轮和跨会话上下文。它有用但有风险：可能过期、私密或过度自信。

## 6. 多 Agent 系统

多 Agent 系统拆分职责。只有每个 agent 边界清晰且 orchestrator 能验证或升级时才值得使用。

## 7. 生产 Agent 系统

生产系统围绕 Agent loop 增加门禁：gateway、runtime、tool gateway、RAG、memory、observability、evaluation、rollback。

## 阅读外部教程的方法

1. 这是单 LLM 调用还是控制循环？
2. 是否使用 tools、RAG、memory 或 multi-agent？
3. Stop condition 是什么？
4. 回答前需要什么证据？
5. Safety 和 rollback 在哪里？
6. 哪些是稳定模式，哪些是框架 API？

