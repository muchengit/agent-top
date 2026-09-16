# Agent-Top

Agent-Top 是一个面向 LLM Agent 开发的开源学习框架。

它帮助学习者和工程师从第一次 LLM 调用，逐步成长到可生产落地的多 Agent 系统建设者。

## 项目覆盖内容

- L0–L5 能力模型
- API 基础与 Prompt 工程
- Agent 核心组件：感知、工具调用、规划、记忆
- 多轮状态与上下文压缩
- 主流 Agent 框架与版本锚定 Lab
- MCP 接入
- RAG pipeline、检索评估与多轮研究讨论
- 长期记忆（Mem0 / Letta）
- 多 Agent 通信、编排与 Supervisor 路由
- 评估、可观测、安全护栏、部署与成本优化
- 发布门禁与生产回归检查
- 生产 Postmortem 与 Trade-off 思维
- 面试题库与作品集项目路径

## 核心理念

模式优先，抗速朽。

教程重点讲稳定模式，例如 ReAct、规划、记忆、工具调用和多 Agent 拓扑；框架相关代码隔离在 Lab 中，并通过 `tested_against`、`validated_date` 等版本锚点管理保鲜成本。

## 内容形态

默认内容形态为 Markdown + 可执行 Lab。

每篇文章或 Lab 遵循统一结构：

1. 目标
2. 前置要求
3. 步骤
4. 版本锚定代码
5. 常见踩坑
6. 自测问题

## 能力等级

| 等级 | 目标 |
| --- | --- |
| L0 | 跑通第一次 LLM 调用 |
| L1 | 理解并实现 Agent 核心组件 |
| L2 | 用框架和 MCP 构建可靠单 Agent |
| L3 | 构建包含 RAG、记忆、可观测和多 Agent 流程的端到端系统 |
| L4 | 完成生产化：评估、安全、部署、成本与 Postmortem |
| L5 | 形成原创模式、开源贡献和真实影响力 |

## 仓库地图

- 核心概念：[`docs/en/concepts`](docs/en/concepts)
- 框架地图：[`docs/en/frameworks/framework-map.md`](docs/en/frameworks/framework-map.md)
- 面试框架：[`docs/en/interviews/interview-framework.md`](docs/en/interviews/interview-framework.md)
- 可执行 Lab：[`labs`](labs)
- 内容模板：[`templates`](templates)
- 治理规范：[`GOVERNANCE.md`](GOVERNANCE.md)
- 贡献指南：[`CONTRIBUTING.md`](CONTRIBUTING.md)
- 路线状态：[`ROADMAP_STATUS.md`](ROADMAP_STATUS.md)

## 文档

具体框架见：

- [`docs/en/agent-top-concrete-framework.md`](docs/en/agent-top-concrete-framework.md)

配套路线图：

- [`agent-top-roadmap.md`](agent-top-roadmap.md)

## 贡献方式

Agent-Top 欢迎以下贡献路径：

- 撰写教程或 Lab
- 翻译内容
- 审校文档
- 维护示例
- 补充面试题或作品集项目

适合入门的标签：

- `good first issue`
- `docs-only`
- `translation-needed`

## License

MIT License，详见 [`LICENSE`](LICENSE)。
