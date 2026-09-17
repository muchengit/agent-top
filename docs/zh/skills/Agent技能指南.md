---
title: Agent 技能指南
validated_date: 2026-09-16
i18n-key: skills-matrix
last-synced: 2026-09-16
---

# Agent 技能指南

Skill 不是框架名、API 包装或教程清单。它是你能重复使用、解释、验证并迁移到真实项目中的 Agent 能力。

## 什么是 Skill？

一个 Agent skill 是可复用的工作方式，帮助你设计、构建、评估、运维和贡献 Agent 系统。

好的 skill 必须能回答：

1. 解决什么问题？
2. 什么时候使用？
3. 怎么练习？
4. 如何证明掌握？
5. 常见失败是什么？

例如：

- 框架知识：知道某个框架怎么调用工具。
- Skill：知道如何把工具风险分类、加权限、记录日志、失败回滚。
- 框架知识：知道某个库怎么配置记忆。
- Skill：知道什么时候该用短期上下文、RAG、长期记忆或显式记忆策略。

Agent-Top 更重视后者：框架会变，skill 会继续有用。

## 为什么需要 Skill？

只用框架会让学习很快过气。Skill 让能力沉淀下来：

- 学得更稳：从会调用 API，变成理解 Agent 组件和边界。
- 开发更快：遇到问题时知道先查权限、trace、eval、工具契约还是记忆策略。
- 面试更强：能解释 trade-off、失败模式和证据，而不只是背名词。
- 作品集更有价值：每个项目能证明一种可迁移能力。
- 贡献更容易：把团队经验抽成模式，别人能 review 和复用。

## 如何使用 Skills？

按这个循环使用：

1. **选一个目标能力**：例如“可靠调用工具”或“评估 RAG 质量”。
2. **读最小概念**：只读和该能力直接相关的教程或概念页。
3. **跑关联 Lab**：用确定性和可测试的练习建立手感。
4. **产出证据**：代码、trace、eval、设计说明或复盘记录。
5. **迁移到新场景**：把同一个 skill 用在一个新项目里。
6. **沉淀 skill card**：重复出现两次以上的工作流，可以写成技能卡。

## Skill 会带来什么效果？

### 对个人学习

- 不再只追框架热点，而是知道哪些模式跨框架稳定。
- 能解释自己的项目为什么这样设计。
- 能把一次报错变成系统改进：eval、guardrail、rollback 或 trace。

### 对实际项目

- 工具边界更清楚：什么能读、什么能写、什么需要人工确认。
- 系统更可靠：知道何时加 retry、verifier、checkpoint 或 human-in-the-loop。
- 评估更具体：回答质量、工具成功率、证据覆盖率和安全失败率能被测量。

### 对面试和工作

- 可以按证据讲项目，而不是只说“做过 Agent”。
- 能回答系统设计问题：组件划分、失败隔离、成本延迟、安全和回滚。
- 能和团队讨论标准：哪些模式值得抽象，哪些只是框架写法。

## Skill 和 Lab 的区别

- **Lab** 是练习环境，用来跑通一个能力。
- **Skill** 是把能力迁移到新场景时带走的能力模型。

比如 `single_agent_mcp` Lab 是练习工具边界；“工具风险分类 + 权限 + 审计 + 回滚”才是可迁移 skill。

## 能力分层技能

下面这张表是学习地图，不是考试等级。只有当你能产出证据时，才算真正跨过一层。

| Level | 知识 | Skill | 证据 |
| --- | --- | --- | --- |
| L0 | LLM request shape、tokens、prompt、context window | 跑第一次调用，解释模型限制 | API demo、prompt notes、概念 quiz |
| L1 | 感知、工具、规划、记忆、ReAct | 手搓最小 Agent，添加 stop conditions | ReAct Lab、多轮状态 Lab、组件说明 |
| L2 | 框架边界、MCP-style tools、成本感知路由 | 设计可靠单 Agent，调试 tool calls | 单 Agent project、framework notes、MCP evidence |
| L3 | RAG、记忆、多 Agent、observability、研究流程 | 构建端到端系统，评估 retrieval | RAG evaluator、memory notes、trace report |
| L4 | 生产运维、evals、safety、rollback、incident | 运行发布门禁、postmortem、guardrails | regression gate、postmortem、生产 checklist |
| L5 | patterns、governance、开源贡献、外部影响力 | 定义可复用模式，打包专家证据，mentor reviewer，产出可维护影响力 artifact | pattern catalog、L5 专家证据包、design doc、PR、talk、article |

## 如何把一个经验沉淀成 Skill？

一次性修复不是 skill。当同一问题重复出现两次以上，就把它写成 skill。

1. 命名问题：例如“工具写操作可能重复执行副作用”。
2. 写契约：输入、输出、失败模式、证据。
3. 加练习：Lab 或案例。
4. 加证明：测试、trace、eval 或 checklist。
5. 写贡献说明：什么时候用，什么时候不要用。

模板见：[`../../../templates/Agent技能卡模板.md`](../../../templates/Agent技能卡模板.md)。

## 示例技能卡

- [`工具MCP安全技能卡.md`](工具MCP安全技能卡.md)：L2-L4 工具与 MCP 安全边界。

## 推荐阅读顺序

1. 先读 L0-L1 教程和 Lab。
2. 再读 Tool/MCP 安全技能卡。
3. 然后进入 L2/L3 教程和案例。
4. 最后用生产清单和 postmortem 模板做复盘。
5. 若要证明 L5，阅读 [`../tutorials/行业对标与L5专家路径.md`](../tutorials/行业对标与L5专家路径.md)，并填写 [`../../../templates/L5专家证据模板.md`](../../../templates/L5专家证据模板.md)。
