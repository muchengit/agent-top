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
| L5 | 形成原创模式、开源贡献、治理证据和真实影响力 |

## 仓库结构

```text
```text
```text
```text
```text
agent-top/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── documentation_request.md
│   ├── workflows/
│   │   └── ci.yml
│   ├── labels.yml
│   └── pull_request_template.md
├── docs/
│   ├── en/
│   │   ├── cases/
│   │   │   ├── README.md
│   │   │   ├── customer-support-multi-agent.md
│   │   │   ├── enterprise-multi-tool-agent.md
│   │   │   ├── multi-agent-collaboration.md
│   │   │   ├── pattern-contribution.md
│   │   │   ├── personal-knowledge-rag.md
│   │   │   └── production-regression-gate.md
│   │   ├── community/
│   │   │   ├── README.md
│   │   │   ├── agent-community-lab.md
│   │   │   ├── community-lab-host-script.md
│   │   │   ├── community-rhythm.md
│   │   │   ├── contribution-paths.md
│   │   │   ├── contributor-of-the-month.md
│   │   │   ├── contributor-onboarding.md
│   │   │   ├── glossary.md
│   │   │   ├── good-first-L5-candidates.md
│   │   │   ├── labels.md
│   │   │   ├── maintainer-rotation.md
│   │   │   └── translation-workflow.md
│   │   ├── concepts/
│   │   │   ├── agent-system-architecture.md
│   │   │   ├── agent-system-blueprint.md
│   │   │   ├── deep-dive-sources.md
│   │   │   ├── design-review-checklist.md
│   │   │   ├── design-review-workshop.md
│   │   │   ├── implementation-guide.md
│   │   │   ├── long-term-memory.md
│   │   │   ├── mcp.md
│   │   │   ├── model-hallucination.md
│   │   │   ├── multi-agent-scheduling.md
│   │   │   ├── multi-round-research-discussion.md
│   │   │   ├── overview.md
│   │   │   ├── plan-decision-making.md
│   │   │   ├── rag-memory-mcp-flow.md
│   │   │   └── react-pattern.md
│   │   ├── frameworks/
│   │   │   └── framework-map.md
│   │   ├── governance/
│   │   │   └── project-operating-model.md
│   │   ├── interviews/
│   │   │   ├── questions/
│   │   │   │   ├── README.md
│   │   │   │   ├── full-question-bank.md
│   │   │   │   ├── l0-basics.md
│   │   │   │   ├── l1-components.md
│   │   │   │   ├── l2-framework-mcp.md
│   │   │   │   ├── l3-system-design.md
│   │   │   │   ├── l4-production.md
│   │   │   │   ├── l5-patterns.md
│   │   │   │   └── question-bank-overview.md
│   │   │   ├── interview-answer-framework.md
│   │   │   └── interview-framework.md
│   │   ├── operations/
│   │   │   ├── 2026-09-17-eight-hour-execution-log.md
│   │   │   ├── 2026-09-17-project-dispatch-queue.md
│   │   │   ├── 2026-09-17-project-dispatch-run.md
│   │   │   ├── 2026-09-17-research-docs-supervision-snapshot.md
│   │   │   └── project-dispatch-run-template.md
│   │   ├── portfolio/
│   │   │   ├── README.md
│   │   │   ├── open-source-impact-guide.md
│   │   │   ├── personal-agent-portfolio.md
│   │   │   └── projects.md
│   │   ├── production/
│   │   │   ├── README.md
│   │   │   ├── cost-stability-operations.md
│   │   │   ├── evals-checklist.md
│   │   │   ├── evals-playbook.md
│   │   │   ├── observability-trace-contract.md
│   │   │   ├── quarterly-maintenance.md
│   │   │   ├── safety-checklist.md
│   │   │   └── team-agent-infrastructure.md
│   │   ├── quick-reference/
│   │   │   ├── README.md
│   │   │   ├── agent-glossary.md
│   │   │   ├── architecture-patterns.md
│   │   │   ├── lab-command-cheatsheet.md
│   │   │   └── production-checklist.md
│   │   ├── skills/
│   │   │   ├── README.md
│   │   │   └── tool-mcp-safety.md
│   │   ├── tutorials/
│   │   │   ├── industry-benchmark-and-l5-expert-path.md
│   │   │   ├── learning-paths.md
│   │   │   ├── open-source-inspirations.md
│   │   │   ├── open-source-pattern-matrix.md
│   │   │   ├── practice-handbook.md
│   │   │   ├── quick-navigation.md
│   │   │   ├── reference-map.md
│   │   │   └── search-supplements.md
│   │   ├── README.md
│   │   ├── agent-top-concrete-framework.md
│   │   ├── l0-first-llm-call.md
│   │   ├── l1-minimal-react-agent.md
│   │   ├── l2-single-agent-mcp.md
│   │   ├── l3-rag-memory-observability.md
│   │   ├── l4-production.md
│   │   └── l5-custom-patterns.md
│   └── zh/
│       ├── cases/
│       │   ├── 个人知识库RAG案例.md
│       │   ├── 企业多工具Agent案例.md
│       │   ├── 多Agent协作案例.md
│       │   ├── 多Agent客服案例.md
│       │   ├── 文档索引.md
│       │   ├── 模式贡献案例.md
│       │   └── 生产回归门禁案例.md
│       ├── community/
│       │   ├── Agent社区实验.md
│       │   ├── L5专家候选任务.md
│       │   ├── 文档索引.md
│       │   ├── 月度贡献者.md
│       │   ├── 术语表.md
│       │   ├── 标签说明.md
│       │   ├── 社区实验主持脚本.md
│       │   ├── 社区节奏.md
│       │   ├── 维护者轮值.md
│       │   ├── 翻译流程.md
│       │   ├── 贡献者入门.md
│       │   └── 贡献路径.md
│       ├── concepts/
│       │   ├── Agent概念总览.md
│       │   ├── Agent系统架构.md
│       │   ├── Agent系统蓝图.md
│       │   ├── Agent设计审查Workshop.md
│       │   ├── Agent设计审查清单.md
│       │   ├── MCP模型上下文协议.md
│       │   ├── Plan决策.md
│       │   ├── RAG记忆MCP数据流.md
│       │   ├── ReAct模式.md
│       │   ├── 多Agent调度.md
│       │   ├── 多轮研究讨论.md
│       │   ├── 核心Agent实施手册.md
│       │   ├── 核心概念深挖来源.md
│       │   ├── 模型幻觉.md
│       │   └── 长期记忆.md
│       ├── frameworks/
│       │   └── 框架地图.md
│       ├── governance/
│       │   └── 项目运营模式.md
│       ├── interviews/
│       │   ├── questions/
│       │   │   ├── L0-L5全题库.md
│       │   │   ├── L0入门.md
│       │   │   ├── L1组件题.md
│       │   │   ├── L2框架MCP题.md
│       │   │   ├── L3系统设计题.md
│       │   │   ├── L4生产化.md
│       │   │   ├── L5模式题.md
│       │   │   ├── 文档索引.md
│       │   │   └── 面试题总览.md
│       │   ├── 面试框架.md
│       │   └── 面试答案范例.md
│       ├── operations/
│       │   ├── 2026-09-17-8小时监督执行日志.md
│       │   ├── 2026-09-17-Research与Docs监督快照.md
│       │   ├── 2026-09-17-project-dispatch-queue.md
│       │   ├── 2026-09-17-项目调度运行记录.md
│       │   └── 项目调度运行记录模板.md
│       ├── portfolio/
│       │   ├── agent项目作品集指南.md
│       │   ├── 作品集项目.md
│       │   ├── 开源贡献与外部影响力指南.md
│       │   └── 文档索引.md
│       ├── production/
│       │   ├── 可观测性与Trace契约.md
│       │   ├── 团队Agent基础设施.md
│       │   ├── 季度维护.md
│       │   ├── 安全清单.md
│       │   ├── 成本稳定性运行手册.md
│       │   ├── 文档索引.md
│       │   ├── 评估与回归Playbook.md
│       │   └── 评估清单.md
│       ├── quick-reference/
│       │   ├── Agent术语表.md
│       │   ├── Lab命令速查.md
│       │   ├── 文档索引.md
│       │   ├── 架构模式速查.md
│       │   └── 生产清单.md
│       ├── skills/
│       │   ├── Agent技能指南.md
│       │   └── 工具MCP安全技能卡.md
│       ├── tutorials/
│       │   ├── 学习路径.md
│       │   ├── 开源模式矩阵.md
│       │   ├── 开源项目灵感目录.md
│       │   ├── 快速导航卡.md
│       │   ├── 搜索补充.md
│       │   ├── 教程参考地图.md
│       │   ├── 练习与Lab使用手册.md
│       │   └── 行业对标与L5专家路径.md
│       ├── Agent-Top具体框架.md
│       ├── L0第一次LLM调用.md
│       ├── L1最小ReActAgent.md
│       ├── L2可靠单Agent与MCP.md
│       ├── L3RAG记忆与可观测.md
│       ├── L4生产化.md
│       ├── L5原创模式.md
│       ├── README.md
│       └── 文档索引.md
├── docs-site/
│   └── index.html
├── examples/
│   ├── agent-decision-trace/
│   ├── agent-eval-regression/
│   ├── coding-task-navigation/
│   ├── coding-workspace-safety/
│   ├── data-source-policy/
│   ├── github-agent-review/
│   ├── mcp-tool-boundary/
│   ├── memory-index-evidence/
│   ├── memory-vs-evidence/
│   ├── model-gateway/
│   ├── observability-trace/
│   ├── rag-evidence-refusal/
│   ├── release-gate-evidence/
│   ├── safety-eval/
│   └── README.md
├── labs/
│   ├── l0/
│   │   └── first_llm_call/
│   ├── l1/
│   │   ├── guardrail_helpers/
│   │   ├── minimal_react_agent/
│   │   └── multi_turn_state/
│   ├── l2/
│   │   ├── cost_aware_router/
│   │   └── single_agent_mcp/
│   ├── l3/
│   │   ├── multi_agent_supervisor/
│   │   ├── multi_round_research_discussion/
│   │   ├── rag_evaluator/
│   │   └── rag_memory_observability/
│   ├── l4/
│   │   ├── cost_and_stability_guardrails/
│   │   ├── production_postmortem/
│   │   └── regression_gate/
│   └── l5/
│       ├── custom_pattern_lab/
│       ├── multilingual_pattern_lab/
│       │   ├── go/
│       │   ├── node/
│       │   ├── python/
│       │   ├── rust/
│       │   └── typescript/
│       └── pattern_catalog/
├── scripts/
│   ├── check_repository.py
│   ├── orchestrate_project.py
│   └── smoke_multilingual_labs.py
└── templates/
    ├── Agent技能卡模板.md
    ├── Agent设计审查Workshop模板.md
    ├── Agent设计审查范例.md
    ├── L5专家证据模板.md
    ├── README.md
    ├── agent-design-template.md
    ├── agent-skill-card-template.md
    ├── article-template.md
    ├── case-study-template.md
    ├── case-study-writing-guide.md
    ├── community-lab-template.md
    ├── contribution-checklist.md
    ├── design-review-example.md
    ├── design-review-workshop-template.md
    ├── employee-work-charter.md
    ├── eval-report-template.md
    ├── eval-trace-replay-template.md
    ├── interview-question-template.md
    ├── l5-expert-evidence-template.md
    ├── lab-template.md
    ├── main-agent-rework-log.md
    ├── monthly-contributor-report.md
    ├── observability-trace-template.md
    ├── paper-reading-session-template.md
    ├── paper-reading-session-template.zh-CN.md
    ├── postmortem-template.md
    ├── project-dispatch-plan.md
    ├── technical-talk-outline-template.md
    ├── technical-talk-outline-template.zh-CN.md
    ├── 主Agent返工日志.md
    ├── 可回放Eval和Trace模板.md
    ├── 可观测性Trace模板.md
    ├── 员工工作章程.md
    ├── 案例研究写作指南.md
    └── 案例研究模板.md
├── .gitignore
├── LICENSE
├── README.md
├── README.zh-CN.md
├── CODE_OF_CONDUCT.md
├── CODE_OF_CONDUCT.zh-CN.md
├── CONTRIBUTING.md
├── CONTRIBUTING.zh-CN.md
├── GOVERNANCE.md
├── GOVERNANCE.zh-CN.md
├── ROADMAP_STATUS.md
├── ROADMAP_STATUS.zh-CN.md
├── SECURITY.md
├── SECURITY.zh-CN.md
├── STYLE.md
├── STYLE.zh-CN.md
├── agent-top-roadmap.md
├── agent-top-roadmap.zh-CN.md
├── package.json
├── package-lock.json
├── pyproject.toml
└── requirements.txt
```

## 目录职责

- `docs/en/`：所有双语文档的英文主源。
- `docs/zh/`：中文镜像，目录结构与 `docs/en` 对齐。
- `examples/`：无需 API key 的 Agent 决策、评估、可观测、gateway、safety、MCP boundary、memory/index、release-gate、GitHub review 和 coding-task 练习材料。
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
- 行业对标与 L5 专家路径：[`docs/zh/tutorials/行业对标与L5专家路径.md`](docs/zh/tutorials/行业对标与L5专家路径.md)
- L5 专家证据模板：[`templates/L5专家证据模板.md`](templates/L5专家证据模板.md)
- 公司化长期运营模式：[`docs/zh/governance/项目运营模式.md`](docs/zh/governance/项目运营模式.md)
- 项目调度计划模板：[`templates/project-dispatch-plan.md`](templates/project-dispatch-plan.md)
- 员工工作章程：[`templates/员工工作章程.md`](templates/员工工作章程.md)
- 主 Agent 返工日志：[`templates/主Agent返工日志.md`](templates/主Agent返工日志.md)
- 可回放 Eval 和 Trace 模板：[`templates/可回放Eval和Trace模板.md`](templates/可回放Eval和Trace模板.md)
- 2026-09-17 调度运行记录：[`docs/zh/operations/2026-09-17-项目调度运行记录.md`](docs/zh/operations/2026-09-17-项目调度运行记录.md)
- 项目调度运行记录模板：[`docs/zh/operations/项目调度运行记录模板.md`](docs/zh/operations/项目调度运行记录模板.md)
- 调度预览脚本：[`scripts/orchestrate_project.py`](scripts/orchestrate_project.py)
- 多语言 L5 模式 Lab：[`labs/l5/multilingual_pattern_lab/README.md`](labs/l5/multilingual_pattern_lab/README.md)
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
