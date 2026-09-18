# Agent-Top 路线图

Agent-Top 的路线图用于定义高层学习路径、发布节奏和社区建设方向。具体执行细节见 [`docs/en/agent-top-concrete-framework.md`](docs/en/agent-top-concrete-framework.md)。

## 目标

帮助学习者从第一次 LLM 调用，逐步成长为能设计、评估、部署并复盘生产级 Agent 系统的工程师。

核心目标：

- 用 L0–L5 能力模型组织学习内容。
- 用稳定模式替代短期框架追新。
- 用 Markdown + 可执行 Lab 保证可复现。
- 用版本锚点和 CI 保鲜机制降低过期成本。
- 用面试与作品集路径连接学习和求职。
- 用双语、贡献分级和社区治理支撑长期维护。

## 路线阶段

### Phase 0：框架与文档基础

状态：✅ 已完成

目标：建立项目结构、能力模型和贡献规范。

交付物：

- `README.md`
- `README.zh-CN.md`
- `agent-top-roadmap.md`
- `docs/en/agent-top-concrete-framework.md`
- 贡献入口与标签规范草案

出口标准：新读者能在 10 分钟内理解项目定位、能力等级和贡献方式。

### Phase 1：L0–L1 入门与核心组件

状态：✅ 已完成

目标：跑通第一个 LLM 调用，并理解 Agent 四大组件。

交付物：

- L0 API demo Lab
- Prompt 基础讲解
- Token / context window / system prompt 速查
- 纯 Python 最小 ReAct Agent Lab
- 感知、工具、规划、记忆职责说明

出口标准：学习者能解释 Agent 核心职责，并无框架跑通最小 ReAct。

### Phase 2：L2 框架层与可靠单 Agent

状态：✅ 已完成

目标：用主线框架构建可靠单 Agent。

交付物：

- 单 Agent 项目模板
- 框架对比笔记
- 至少 1 个 MCP server 接入 Lab
- Guardrail 基础 Lab

出口标准：完成单 Agent 项目，并说明框架选择权衡。

### Phase 3：L3 系统能力

状态：✅ 已完成

目标：构建端到端 Agent 系统。

交付物：

- 自研 RAG pipeline Lab
- Mem0 / Letta 记忆接入
- Langfuse 可观测性示例
- 多 Agent 通信与编排示例
- RAG → 记忆 → 多 Agent → MCP 数据流案例

出口标准：学习者能解释系统数据流，并输出评估报告。

### Phase 4：L4 生产化

状态：✅ 已完成

目标：把 Agent 系统推向生产工程。

交付物：

- 多智能体拓扑设计模板
- 评估指标与自动化回归
- 安全护栏清单
- 部署与成本优化指南
- Postmortem 模板

出口标准：完成生产化设计、评估与线上复盘。

### Phase 5：L5 专家路径与生态建设

状态：🔄 进行中

目标：形成原创模式、开源影响力和团队级 Agent 基础设施能力。

交付物：

- 原创模式案例
- 开源 PR 指南
- 技术分享 / 论文导读模板
- 团队 Agent 基础设施设计指南

出口标准：贡献者能产出外部影响力物证，例如 PR、论文、演讲、案例或工具。

## 内容生产节奏

- 双周教程：推进核心能力路径
- 月度面试题：连接学习与求职评估
- 季度路线图回顾：调整内容优先级
- 双周论文共读：追踪研究方向
- 月度 showcase：展示作品集与社区成果
- 季度 Hackathon：集中攻坚复杂案例

## 质量机制

每篇内容必须包含：

- 目标能力层 Lx
- `validated_date`
- `tested_against`
- 前置依赖
- 可执行步骤
- 常见踩坑
- 自测问题

CI 建议检查：

- 死链
- Markdown 构建
- 拼写
- i18n 同步
- 版本锚点缺失
- deprecated 内容引用

## 社区与贡献

角色路径：

- Contributor → Reviewer → Maintainer → Core

贡献路径：

- 撰稿
- 翻译
- 校对
- 维护

入门标签：

- `good first issue`
- `docs-only`
- `translation-needed`

双语策略：

- EN 为主源
- ZH 通过 `translation-needed` 认领
- 每章目标：认领后 ≤3 天完成初译
- CI 监测 `last-synced` 滞后并自动开 `sync-required`

## 当前优先事项

1. 初始化仓库并补全基础文档
2. 建立目录结构与贡献规范
3. 完成 L0 第一个 API demo Lab
4. 完成 L1 最小 ReAct Agent Lab
5. 建立版本锚点与 CI 检查

