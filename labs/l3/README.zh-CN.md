---
title: L3 Labs
capability_level: L3
validated_date: 2026-09-19
---

# L3 Labs

英文版：[`README.md`](README.md)

## 目标

构建包含 RAG、记忆、可观测性与多 Agent 流程的端到端系统。

## 前置条件

- L2：可靠单 Agent 与 MCP
- Python 3.10+
- 熟悉 RAG、记忆与多 Agent 概念

## 本级别 Labs

- [`rag_memory_observability`](rag_memory_observability/README.md)：RAG、记忆与可观测性骨架。
- [`rag_hybrid_search`](rag_hybrid_search/README.md)：确定性关键词+向量混合检索。
- [`rag_evaluator`](rag_evaluator/README.md)：确定性检索评估。
- [`multi_round_research_discussion`](multi_round_research_discussion/README.md)：多轮证据规划与讨论收敛。
- [`multi_agent_supervisor`](multi_agent_supervisor/README.md)：确定性多 Agent 路由。

## 运行

```bash
python -m unittest discover -s labs/l3 -p "test_*.py"
```

## 常见踩坑

- 先加记忆，而不先评估检索质量。
- 多 Agent 拓扑无序扩张，缺少确定性 supervisor。
- 组合 RAG、记忆与编排时忘记可观测性。

## 自检

1. 如何确定性地评估检索质量？
2. supervisor 在多 Agent 路由中起什么作用？
3. 在 RAG 记忆管道中哪些可观测信号最重要？
