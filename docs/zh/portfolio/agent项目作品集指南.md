---
title: 个人 Agent 项目作品集指南
validated_date: 2026-09-17
i18n-key: portfolio-personal-agent-portfolio
last-synced: 2026-09-17
---

# 个人 Agent 项目作品集指南

一个强作品集应证明你能设计、构建、评估、运维并解释 Agent 系统。本指南说明作品集应有什么形状、每个项目必须携带什么证据、如何写项目 README、如何准备面试摘要，以及如何衡量质量。

## 目标读者与目的

- **主要读者**：为 Agent 系统岗位或 L5 评审做准备的学习者，以及需要一致证据标准的面试官。
- **目的**：把完成的 Labs 和案例工作转化为可审查、可解释的项目产物。
- **不适合**：学习第一周的人。先完成 [`学习路径.md`](../tutorials/学习路径.md) 的入门路径，再建作品集。

## 推荐组合

准备 2–4 个项目：

- **个人知识库 Agent**：证明 RAG、memory、引用和拒绝回答。
- **企业工具 Agent**：证明 tool use、权限、MCP 风格边界和错误处理。
- **多 Agent 协作**：证明 orchestration、verification 和一致性。
- **原创模式或框架贡献**：证明抽象、测试和可维护性。

## 分步骤工作流

1. **选定 2–4 条轨道**。覆盖 RAG、tool orchestration、multi-agent coordination 和 abstraction。
2. **划定一个可交付切片**。第一版保持小到可以演示。
3. **记录决策**。设计决策和 trade-offs 边做边写，不要事后补。
4. **构建评估**。添加 datasets、metrics、negative cases 和 release gates。
5. **添加安全与可观测性**。记录工具权限、guardrails、traces 和 alerts。
6. **按模板写 README**。填满每个章节，包括你刻意没有自动化的部分。
7. **排练一分钟故事**。把 README 变成 STAR 摘要。
8. **链接证据**。把项目连接到 Labs、案例和生产检查清单。

## 如何选择项目

- **选你真实遇到的问题**。真实失败比假设问题更能写出好叙事。
- **覆盖四个梯度**。RAG、tool orchestration、multi-agent coordination、abstraction 展示广度。
- **深度优先于数量**。两个带 eval、safety、rollback 的项目胜过五个演示。
- **复用 Labs 和案例**。[`作品集项目.md`](作品集项目.md) 说明了哪些轨道对应哪些 Labs。
- **保留一个外部项目**。被接受的 PR 或维护者评论是最强的独立信号。

## 每个项目必须有的证据

- Problem statement。
- User 或 customer。
- Non-goals。
- Architecture diagram。
- Design decisions 与 trade-offs。
- Evaluation plan。
- Safety controls。
- Observability plan。
- Cost and latency assumptions。
- Known failure modes。
- Rollback 或 degradation strategy。
- Demo video 或 reproducible commands。
- 十倍流量时会改什么。

## 项目 README 模板

```markdown
# Agent Project Name

## Problem
解决什么用户问题？

## Scope
包含什么，明确不包含什么？

## Architecture
架构图和组件边界。

## Design Decisions
为什么选这个模式而不是更小或更大的方案？

## Evaluation
dataset、指标、negative cases、release gates。

## Safety and Permissions
工具、风险、guardrails、审批、拒绝回答。

## Observability
traces、logs、alerts、dashboards、debugging workflow。

## Cost and Stability
预算、降级模式、回滚路径、容量假设。

## Demo
命令、截图或视频链接。

## Results
什么有效，什么失败，你改了什么。
```

## 作品集索引模板

```markdown
# Portfolio Index

## Project 1 — Personal Knowledge Agent
一句话问题、一个 README 链接、一个 eval 结果。

## Project 2 — Enterprise Tool Agent
一句话问题、一个 README 链接、一个安全决策。

## Project 3 — Multi-Agent Collaboration
一句话问题、一个 README 链接、一次失败与修复。

## Project 4 — Pattern Contribution
一句话问题、PR 链接、维护者评论。
```

## 叙事质量

每个项目都要回答：

- 最先会坏在哪里？
- 如何知道它错了？
- 如何不靠人工恢复？
- 什么数据证明它有效？
- 哪些事情你刻意没有自动化？

## 常见错误与规避

- **只有 demo 没有证据**——能跑通的 demo 不是证明。添加可复现命令和 eval 结果。
- **隐藏失败**——审查者更看重记录在案的失败，而不是完美的 demo。记录什么失败了、你改了什么。
- **没有 non-goals**——没有 non-goals，项目显得无边界。明确写出什么不在范围内。
- **跳过 observability**——logs 和 traces 是判断系统出错的方式。包含 debugging workflow。
- **指标不清晰**——构建前就定义"有效"是什么。否则评估只是事后解释。
- **作品集过度铺开**——两个强项目胜过五个浅项目。深度才是区分度。

## 可衡量指标

- **Reproducibility**：审查者可以在没有你帮助的情况下运行 demo 命令。
- **Eval coverage**：每个论断都有 datasets、metrics、negative cases 和 release gates。
- **Safety depth**：权限、guardrails、审批、拒绝回答都有文档且可测试。
- **Operational maturity**：traces、logs、alerts、rollback 或 degradation 路径都存在。
- **Clarity**：一分钟 STAR 摘要能让非专家听懂。

## 真实示例片段

```markdown
# Personal Knowledge Agent

## Problem
我的会议纪要答案没有来源，后续问题不断重复陈旧事实。

## Evaluation
- Dataset：30 篇个人笔记；指标：答案级来源覆盖率。
- Negative cases：证据缺失、笔记过期、笔记相互矛盾。
- Release gate：每个答案必须引用检索到的 chunk。

## Safety and Permissions
- 只读文件访问；任何工具都不能写入或删除笔记。
- 没有 chunk 支撑论断时使用拒绝模板。

## Results
- 来源覆盖率达到 28/30；2 个失败是矛盾笔记。
- eval 后新增了矛盾处理规则。
```

## 面试版 STAR

每个项目准备一分钟版本：

- Situation：业务或学习问题。
- Task：你的 Agent 设计责任。
- Action：架构、evals、safety、observability 选择。
- Result：可衡量行为和 trade-offs。

## 下一步行动清单

- [ ] 在四个梯度中选定 2–4 个项目。
- [ ] 为第一个项目定义问题、用户和 non-goals。
- [ ] 画架构图并记录设计决策。
- [ ] 构建带 negative cases 和 release gate 的评估。
- [ ] 记录安全、可观测性和成本假设。
- [ ] 用模板写 README。
- [ ] 排练一分钟 STAR 摘要。
- [ ] 把作品集链接到 Labs、案例和生产检查清单。

## 关联资产

- [`作品集项目.md`](作品集项目.md)
- [`开源贡献与外部影响力指南.md`](开源贡献与外部影响力指南.md)
- [`../interviews/面试框架.md`](../interviews/面试框架.md)
- [`../production/评估清单.md`](../production/评估清单.md)
- [`../concepts/Agent设计审查清单.md`](../concepts/Agent设计审查清单.md)
