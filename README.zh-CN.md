# Agent-Top

Agent-Top 是一个面向 LLM Agent 开发的开源学习框架。

它帮助学习者和工程师从第一次 LLM 调用，逐步成长到可生产落地的多 Agent 系统建设者。

## 快速开始

先做一件事：[`docs/en/tutorials/quick-navigation.md`](docs/en/tutorials/quick-navigation.md) 或中文 [`docs/zh/tutorials/快速导航卡.md`](docs/zh/tutorials/快速导航卡.md)。无需 API key 的练习在 [`examples/agent-decision-trace/README.md`](examples/agent-decision-trace/README.md)。

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

## 仓库结构

```text
agent-top/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── documentation_request.md
│   ├── labels.yml
│   ├── pull_request_template.md
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── en/                           # 英文主源，模块结构完整展开
│   │   ├── cases/                    # 案例研究
│   │   ├── community/                # 社区运营、翻译、活动、治理支持
│   │   ├── concepts/                 # Agent 稳定概念、架构蓝图、设计审查
│   │   ├── frameworks/               # 框架对比与选型
│   │   ├── interviews/               # 面试框架与 L1-L5 题库
│   │   ├── portfolio/                # 作品集项目路径
│   │   ├── production/               # 评估、回归、安全、维护、回滚
│   │   ├── quick-reference/          # 术语、命令、架构、生产速查表
│   │   ├── skills/                   # Agent 技能体系
│   │   ├── tutorials/                # 外部教程、开源项目灵感、模式矩阵、学习路径、快速导航、练习手册
│   │   ├── l0-l5 tutorials           # L0-L5 详细教程
│   │   ├── README.md                 # 英文文档索引
│   │   └── agent-top-concrete-framework.md
│   └── zh/                           # 中文文档，文件名使用中文
│       ├── 文档索引.md
│       ├── Agent-Top具体框架.md
│       ├── L0第一次LLM调用.md
│       ├── L1最小ReActAgent.md
│       ├── L2可靠单Agent与MCP.md
│       ├── L3RAG记忆与可观测.md
│       ├── L4生产化.md
│       ├── L5原创模式.md
│       ├── cases/                    # 中文案例研究
│       ├── community/                # 中文社区运营
│       ├── concepts/                 # 中文概念与架构
│       ├── frameworks/               # 中文框架地图
│       ├── interviews/               # 中文面试框架
│       ├── portfolio/                # 中文作品集路径
│       ├── production/               # 中文生产指南
│       ├── quick-reference/          # 中文速查表
│       ├── skills/                   # 中文 Agent 技能体系
│       └── tutorials/                # 中文教程与开源项目灵感
├── examples/
│   ├── agent-decision-trace/         # 无需 API key 的 Agent 决策练习
│   ├── memory-vs-evidence/           # Memory 与 Evidence 决策练习
│   ├── coding-workspace-safety/      # Coding workspace safety 练习
│   ├── data-source-policy/           # 数据源策略练习
│   ├── coding-task-navigation/       # Coding task-first navigation 练习
│   ├── agent-eval-regression/        # Agent 评估回归练习
│   ├── github-agent-review/          # GitHub Agent review 练习
│   ├── observability-trace/          # 可观测性与 trace 契约练习
│   ├── model-gateway/                # Model gateway evidence 练习
│   ├── safety-eval/                  # Safety eval evidence 练习
│   ├── mcp-tool-boundary/            # MCP tool boundary 练习
│   ├── memory-index-evidence/        # Memory 与 Index evidence 练习
│   └── rag-evidence-refusal/         # RAG 证据与拒绝回答练习
├── labs/
│   ├── l0/                           # 第一次 LLM 调用
│   ├── l1/                           # ReAct、guardrails、多轮状态
│   ├── l2/                           # 工具/MCP 边界与成本感知路由
│   ├── l3/                           # RAG、多轮研究、多 Agent supervisor
│   ├── l4/                           # 生产 postmortem、回归门禁与成本护栏
│   ├── l5/                           # 可复用模式 Lab 与模式目录
│   └── README.md
├── scripts/
│   └── check_repository.py           # Markdown、链接、双语、Lab 结构检查
├── templates/                        # 文章、Lab、面试、postmortem、设计审查、案例研究、贡献自查模板
├── docs-site/                        # 轻量文档站入口
├── README.md                         # 英文项目概览和仓库地图
├── README.zh-CN.md                   # 中文项目概览和仓库地图
├── CODE_OF_CONDUCT.md                # 英文行为准则
├── CODE_OF_CONDUCT.zh-CN.md          # 中文行为准则
├── CONTRIBUTING.md                   # 英文贡献指南
├── CONTRIBUTING.zh-CN.md             # 中文贡献指南
├── GOVERNANCE.md                     # 英文治理说明
├── GOVERNANCE.zh-CN.md               # 中文治理说明
├── ROADMAP_STATUS.md                 # 英文路线状态
├── ROADMAP_STATUS.zh-CN.md           # 中文路线状态
├── SECURITY.md                       # 英文安全策略
├── SECURITY.zh-CN.md                 # 中文安全策略
├── STYLE.md                          # 英文风格规范
├── STYLE.zh-CN.md                    # 中文风格规范
├── agent-top-roadmap.md              # 路线图
├── agent-top-roadmap.zh-CN.md        # 中文路线图
├── LICENSE
└── pyproject.toml
```

## 目录职责

- `docs/en/`：所有双语文档的英文主源。
- `docs/zh/`：中文镜像，目录结构与 `docs/en` 对齐。
- `examples/`：无需 API key 的 Agent 决策、评估、可观测、gateway、safety、MCP boundary、memory/index、GitHub review 和 coding-task 练习材料。
- `labs/`：可运行、确定性、无需 API key 的练习。
- `templates/`：可复用贡献模板，方便 reviewer 检查一致性。
- `scripts/`：本地校验链接、frontmatter、版本锚点和 Lab 完整性。
- `.github/`：CI、标签、Issue 模板和 PR 模板。

## 仓库地图

- 设计审查 Workshop：[`docs/en/concepts/design-review-workshop.md`](docs/en/concepts/design-review-workshop.md)
- 系统蓝图：[`docs/en/concepts/agent-system-blueprint.md`](docs/en/concepts/agent-system-blueprint.md)
- 快速导航：[`docs/en/tutorials/quick-navigation.md`](docs/en/tutorials/quick-navigation.md)
- 中文快速导航：[`docs/zh/tutorials/快速导航卡.md`](docs/zh/tutorials/快速导航卡.md)
- 本地练习：[`examples/README.md`](examples/README.md)
- 练习手册：[`docs/en/tutorials/practice-handbook.md`](docs/en/tutorials/practice-handbook.md)
- 中文练习手册：[`docs/zh/tutorials/练习与Lab使用手册.md`](docs/zh/tutorials/练习与Lab使用手册.md)
- 评估 Playbook：[`docs/en/production/evals-playbook.md`](docs/en/production/evals-playbook.md)
- 中文评估 Playbook：[`docs/zh/production/评估与回归Playbook.md`](docs/zh/production/评估与回归Playbook.md)
- 核心概念：[`docs/zh/concepts`](docs/zh/concepts)
- 框架地图：[`docs/zh/frameworks/框架地图.md`](docs/zh/frameworks/框架地图.md)
- 面试框架：[`docs/zh/interviews/面试框架.md`](docs/zh/interviews/面试框架.md)
- 学习路径：[`docs/zh/tutorials/学习路径.md`](docs/zh/tutorials/学习路径.md)
- 开源项目灵感目录：[`docs/zh/tutorials/开源项目灵感目录.md`](docs/zh/tutorials/开源项目灵感目录.md)
- 开源模式矩阵：[`docs/en/tutorials/open-source-pattern-matrix.md`](docs/en/tutorials/open-source-pattern-matrix.md)
- 可执行 Lab：[`labs`](labs)
- 内容模板：[`templates`](templates)
- 中文文档索引：[`docs/zh/文档索引.md`](docs/zh/文档索引.md)
- Agent 技能指南：[`docs/zh/skills/Agent技能指南.md`](docs/zh/skills/Agent技能指南.md)
- 治理规范：[`GOVERNANCE.zh-CN.md`](GOVERNANCE.zh-CN.md)
- 贡献指南：[`CONTRIBUTING.zh-CN.md`](CONTRIBUTING.zh-CN.md)
- 风格规范：[`STYLE.zh-CN.md`](STYLE.zh-CN.md)
- 社区：[`docs/zh/community/文档索引.md`](docs/zh/community/文档索引.md)
- 安全：[`SECURITY.zh-CN.md`](SECURITY.zh-CN.md)
- 路线状态：[`ROADMAP_STATUS.zh-CN.md`](ROADMAP_STATUS.zh-CN.md)

## 文档

具体框架见：

- [`docs/zh/Agent-Top具体框架.md`](docs/zh/Agent-Top具体框架.md)

配套路线图：

- [`agent-top-roadmap.zh-CN.md`](agent-top-roadmap.zh-CN.md)

## 贡献方式

Agent-Top 欢迎以下贡献路径：

- 撰写教程或 Lab
- 翻译内容
- 审校文档
- 维护示例
- 补充面试题、作品集项目、面试回答范例或可复用设计模板

适合入门的标签：

- `good first issue`
- `docs-only`
- `translation-needed`

## License

MIT License，详见 [`LICENSE`](LICENSE)。
