---
i18n-key: frameworks-framework-map
last-synced: 2026-09-16
validated_date: 2026-09-16
---

框架地图

Agent-Top 把框架当作稳定模式的例子。持久学习目标是 pattern，框架是版本化实现。

## 阵营

| Camp | Frameworks | 为什么重要 | Best Fit | 注意 |
| --- | --- | --- | --- | --- |
| Graph orchestration | LangGraph | 明确状态、循环、checkpoint、调试 | 复杂 workflow、human review、retry | orchestration overhead |
| Multi-agent | CrewAI, AutoGen | 角色 workflow 和对话协调 | 专门化 agent、角色边界 | coordination cost |
| Lightweight | Smolagents, Agno | API 小、迭代快 | 小 Agent、学习、demo | 生产控制需额外添加 |
| SDK | OpenAI, Claude, Google ADK | 平台模型 API | 平台原生功能 | 绑定 provider |
| Type-safe | Pydantic AI | schema 和 validation ergonomics | structured output | schema discipline |
| Enterprise | Semantic Kernel | .NET/企业生态、插件 | 企业栈、治理插件 | 企业约束 |
| RAG | LlamaIndex, Haystack | 检索和文档 pipeline | 搜索密集应用 | 仍需 evals |
| Optimization | DSPy | 声明式 prompt/pipeline optimization | prompt pipeline | 需要强 eval harness |

## 框架选择问题

- 是否需要 graph state 和 checkpoints？
- 是否需要 multi-agent role separation？
- 是否需要 provider-native model APIs？
- 是否需要强 schema validation？
- 是否需要 enterprise plugin governance？
- 是否需要 RAG-specific pipelines？
- 是否需要 prompt optimization？
- 下一个季度是否还能维护？

## 稳定边界

不管框架，都应教：

- 感知 和 context assembly。
- Tool invocation 和 validation。
- 规划 loops 和 stop conditions。
- 记忆 lifecycle。
- Retrieval boundaries。
- Observability。
- Safety guardrails。
- Rollback 和 failure modes。

## 示例策略

框架代码放在 Lab。概念尽量框架无关。示例包含：

```yaml
validated_date: YYYY-MM-DD
tested_against: framework-name x.y.z
```

