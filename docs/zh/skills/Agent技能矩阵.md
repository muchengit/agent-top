---
title: Agent 技能矩阵
validated_date: 2026-09-16
i18n-key: skills-matrix
last-synced: 2026-09-16
---

# Agent 技能矩阵

这页把 L0-L5 能力模型转换成具体知识、技能和可验证证据。

## 如何使用这个矩阵

- 用它规划学习路径。
- 用它搭建作品集。
- 用它安排面试复习。
- 用它提出新 Lab 或案例。

## 各级技能

| Level | 知识 | 技能 | 证据 |
| --- | --- | --- | --- |
| L0 | LLM request shape、tokens、prompts、context window | 跑第一次调用、解释限制、避免 API overfitting | API demo、prompt notes、术语 quiz |
| L1 | 感知、工具、规划、记忆、ReAct | 手搓最小 Agent、校验 tool args、添加 stop conditions | ReAct Lab、多轮状态 Lab、组件解释 |
| L2 | 框架边界、MCP-style tools、成本感知路由 | 设计可靠单 Agent、框架对比、调试 tool calls | 单 Agent project、framework notes、MCP Lab evidence |
| L3 | RAG、记忆、多 Agent、observability、研究流程 | 构建端到端系统、评估 retrieval、隔离多 Agent 状态 | RAG evaluator、memory flow notes、Langfuse-style trace report |
| L4 | 生产运维、evals、safety、rollback、incident | 运行发布门禁、postmortem、guardrail、成本/延迟预算 | regression gate、postmortem、生产 checklist evidence |
| L5 | patterns、开源贡献、外部影响力 | 定义可复用模式、写设计文档、开 PR 或分享 | pattern catalog entry、design doc、PR、talk、article |

## 技能类别

| 类别 | 衡量什么 | 证据示例 |
| --- | --- | --- |
| Concepts | 能否解释稳定 Agent 概念？ | teaching notes、glossary entries、diagrams |
| Code | 能否实现确定性行为？ | Labs、tests、runnable snippets |
| Architecture | 能否选择正确模式？ | design docs、trade-off analysis |
| Tools | 能否安全处理 tool/MCP 边界？ | tool contracts、permissions、logs |
| Evaluation | 能否衡量质量？ | evals、regression checks、dashboards |
| Safety | 能否防止伤害？ | guardrails、confirmations、postmortems |
| Production | 能否运行真实系统？ | release gates、rollback、incident evidence |
| Contribution | 能否改善生态？ | PRs、pattern docs、talks、guides |

## 推荐技能证据包

1. **L0-L1 Starter Pack**
   - First LLM call Lab。
   - Minimal ReAct Agent Lab。
   - 5 题概念 quiz。

2. **L2 Reliable Agent Pack**
   - 带 tool boundary 的单 Agent。
   - Framework comparison notes。
   - Cost-aware routing Lab。

3. **L3 System Pack**
   - RAG evaluator Lab。
   - Multi-agent supervisor Lab。
   - Trace/eval report。

4. **L4 Production Pack**
   - Regression gate Lab。
   - Production postmortem Lab。
   - Production checklist 完成证据。

5. **L5 Impact Pack**
   - Custom pattern Lab。
   - Pattern catalog Lab。
   - 开源贡献或设计文章。

## 贡献指南

新增技能时：

1. 说明它属于哪一层。
2. 至少提供一个可验证证据。
3. 链接相关 Lab 或案例。
4. 说明常见 failure modes。
5. 框架特定细节放在 Labs。

参见：[`../../../templates/Agent技能卡模板.md`](../../../templates/Agent技能卡模板.md)
