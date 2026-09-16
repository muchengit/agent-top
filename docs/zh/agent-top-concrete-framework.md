---
i18n-key: agent-top-concrete-framework
last-synced: 2026-09-16
validated_date: 2026-09-16
---

# Agent-Top 具体框架

本文件是 Agent-Top 的中文核心框架说明。英文源文件见 [`../en/agent-top-concrete-framework.md`](./agent-top-concrete-framework.md)。

## 目标

Agent-Top 用 L0-L5 能力模型组织 LLM Agent 学习路径，让学习者从第一次 LLM 调用，逐步走到生产级 Agent 系统、原创模式和开源贡献。

## 核心理念

- 模式优先，框架其次。
- 先概念后代码。
- 先本地可运行，再生产化。
- 框架代码隔离在 Lab，稳定概念留在文档。
- 所有关键内容有 `validated_date`，框架相关内容加 `tested_against`。

## L0-L5 能力模型

| 层级 | 定位 | 出口标准 |
| --- | --- | --- |
| L0 | 入门 | 跑通一次 LLM 调用，并解释 token、上下文窗口、系统提示 |
| L1 | 核心 | 手写最小 ReAct Agent，讲清感知、工具、规划、记忆 |
| L2 | 框架层 | 用框架构建可靠单 Agent，并接入 MCP-style 工具边界 |
| L3 | 系统 | 做 RAG、记忆、可观测、多 Agent 流程 |
| L4 | 生产 | 完成评估、安全、部署、成本、postmortem |
| L5 | 专家 | 形成原创模式、开源 PR、论文或演讲等影响力物证 |

## 学习路径

1. API 基础与 Prompt 工程。
2. Agent 四组件：感知、工具、规划、记忆。
3. 框架层：图编排、多智能体、轻量 SDK、类型安全。
4. 数据流：RAG、记忆、MCP、Multi-Agent。
5. 评估、可观测、安全、部署。
6. 原创模式与贡献。

## 内容形态

- 概念讲解：解释稳定模式和 trade-off。
- 代码 Lab：本地可运行、无需 API key。
- 案例研究：把模式放到真实场景中。
- 速查表：帮助面试、设计、生产上线快速查阅。
- 搜索补充：把外部教程主题映射回 Agent-Top。

## 生产级要求

生产内容必须说明：

- 鉴权和权限。
- 限流和成本控制。
- 评估集和回归测试。
- 可观测 trace。
- 回滚路径。
- Postmortem 和 action items。

## 社区贡献

四类贡献路径：

- 撰稿。
- 翻译。
- 校对。
- 维护。

入口标签：`good first issue`、`docs-only`、`translation-needed`、`sync-required`。

## 关联文档

- L0-L5 中文教程：[`l0-first-llm-call.md`](l0-first-llm-call.md)
- Agent 架构：[`concepts/agent-system-architecture.md`](concepts/agent-system-architecture.md)
- 框架地图：[`frameworks/framework-map.md`](frameworks/framework-map.md)
- 生产清单：[`quick-reference/production-checklist.md`](quick-reference/production-checklist.md)
