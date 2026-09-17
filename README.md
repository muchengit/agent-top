# Agent-Top

Agent-Top is an open-source learning framework for LLM Agent development.

It helps learners and engineers build practical Agent skills from first LLM calls to production-grade multi-agent systems.

## Quick Start

Start here: [`docs/en/tutorials/quick-navigation.md`](docs/en/tutorials/quick-navigation.md) and [`examples/agent-decision-trace/README.md`](examples/agent-decision-trace/README.md).

## What This Project Covers

- L0–L5 capability model
- API basics and prompt engineering
- Core Agent components: perception, tool use, planning, and memory
- Multi-turn state and context compression
- Mainstream Agent frameworks with version-anchored Labs
- MCP integration
- RAG pipelines, retrieval evaluation, and multi-round research discussion
- Long-term memory with Mem0 / Letta
- Multi-agent communication, orchestration, and supervisor routing
- Evaluation, observability, safety guardrails, deployment, and cost optimization
- Release gates and production regression checks
- Production postmortems and trade-off thinking
- Interview questions and portfolio project tracks

## Core Philosophy

Pattern-first, anti-staleness.

Tutorials focus on stable patterns such as ReAct, planning, memory, tool use, and multi-agent topologies. Framework-specific code is isolated in Labs and marked with version anchors such as `tested_against` and `validated_date`.

## Content Style

The main content format is Markdown plus executable Labs.

Each article or Lab follows a consistent structure:

1. Goal
2. Prerequisites
3. Steps
4. Version-anchored code
5. Common pitfalls
6. Self-check questions

## Capability Levels

| Level | Goal |
| --- | --- |
| L0 | Run the first LLM call |
| L1 | Understand and implement core Agent components |
| L2 | Build a reliable single Agent with a framework and MCP |
| L3 | Build end-to-end systems with RAG, memory, observability, and multi-agent flows |
| L4 | Productionize Agent systems with evaluation, safety, deployment, cost, and postmortems |
| L5 | Create original patterns, open-source contributions, governance evidence, and real-world influence |


## Repository Structure

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

## Directory Responsibilities

- `docs/en/`: primary English source for all bilingual documentation.
- `docs/zh/`: Chinese mirror with the same module structure as `docs/en`.
- `examples/`: fictional, no-API-key practice materials for Agent decisions and evidence.
- `labs/`: runnable, deterministic exercises that prove each capability level.
- `templates/`: reusable contribution formats so reviewers can check consistency.
- `scripts/`: local validation for links, frontmatter, version anchors, and Lab completeness.
- `.github/`: CI workflow, labels, issue templates, and PR templates.

## Local Checks

Run the repository checks:

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

## Repository Map

- Design review workshop: [`docs/en/concepts/design-review-workshop.md`](docs/en/concepts/design-review-workshop.md)
- Agent system blueprint: [`docs/en/concepts/agent-system-blueprint.md`](docs/en/concepts/agent-system-blueprint.md)
- Quick navigation: [`docs/en/tutorials/quick-navigation.md`](docs/en/tutorials/quick-navigation.md)
- No-API-key examples: [`examples/README.md`](examples/README.md)
- Practice handbook: [`docs/en/tutorials/practice-handbook.md`](docs/en/tutorials/practice-handbook.md)
- Eval playbook: [`docs/en/production/evals-playbook.md`](docs/en/production/evals-playbook.md)
- Concepts: [`docs/en/concepts`](docs/en/concepts)
- Framework map: [`docs/en/frameworks/framework-map.md`](docs/en/frameworks/framework-map.md)
- Design review checklist: [`docs/en/concepts/design-review-checklist.md`](docs/en/concepts/design-review-checklist.md)
- Open-source inspirations: [`docs/en/tutorials/open-source-inspirations.md`](docs/en/tutorials/open-source-inspirations.md)
- Open-source pattern matrix: [`docs/en/tutorials/open-source-pattern-matrix.md`](docs/en/tutorials/open-source-pattern-matrix.md)
- Industry benchmark and L5 expert path: [`docs/en/tutorials/industry-benchmark-and-l5-expert-path.md`](docs/en/tutorials/industry-benchmark-and-l5-expert-path.md)
- L5 expert evidence template: [`templates/l5-expert-evidence-template.md`](templates/l5-expert-evidence-template.md)
- Company-style long-run operating model: [`docs/en/governance/project-operating-model.md`](docs/en/governance/project-operating-model.md)
- Project dispatch plan template: [`templates/project-dispatch-plan.md`](templates/project-dispatch-plan.md)
- Employee work charter: [`templates/employee-work-charter.md`](templates/employee-work-charter.md)
- Main agent rework log: [`templates/main-agent-rework-log.md`](templates/main-agent-rework-log.md)
- Eval and trace replay template: [`templates/eval-trace-replay-template.md`](templates/eval-trace-replay-template.md)
- 2026-09-17 dispatch run: [`docs/en/operations/2026-09-17-project-dispatch-run.md`](docs/en/operations/2026-09-17-project-dispatch-run.md)
- Project dispatch run template: [`docs/en/operations/project-dispatch-run-template.md`](docs/en/operations/project-dispatch-run-template.md)
- Orchestration preview script: [`scripts/orchestrate_project.py`](scripts/orchestrate_project.py)
- Multilingual L5 pattern Lab: [`labs/l5/multilingual_pattern_lab/README.md`](labs/l5/multilingual_pattern_lab/README.md)
- Interview framework: [`docs/en/interviews/interview-framework.md`](docs/en/interviews/interview-framework.md)
- Labs: [`labs`](labs)
- Templates: [`templates`](templates)
- Documentation index: [`docs/en/README.md`](docs/en/README.md)
- Agent skills guide: [`docs/en/skills/README.md`](docs/en/skills/README.md)
- Governance: [`GOVERNANCE.md`](GOVERNANCE.md)
- Style guide: [`STYLE.md`](STYLE.md)
- Contributing: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Chinese contribution guide: [`CONTRIBUTING.zh-CN.md`](CONTRIBUTING.zh-CN.md)
- Community: [`docs/en/community/README.md`](docs/en/community/README.md)
- Security: [`SECURITY.md`](SECURITY.md)
- Chinese security policy: [`SECURITY.zh-CN.md`](SECURITY.zh-CN.md)
- Roadmap status: [`ROADMAP_STATUS.md`](ROADMAP_STATUS.md)
- Chinese roadmap status: [`ROADMAP_STATUS.zh-CN.md`](ROADMAP_STATUS.zh-CN.md)

## Documentation

See the concrete framework:

- [`docs/en/agent-top-concrete-framework.md`](docs/en/agent-top-concrete-framework.md)

Related roadmap:

- [`agent-top-roadmap.md`](agent-top-roadmap.md)

## Contribution Paths

Agent-Top welcomes contributions through:

- Writing tutorials or Labs
- Translating content
- Reviewing documentation
- Maintaining examples
- Adding interview questions, portfolio projects, interview examples, or reusable design templates

Good starting labels:

- `good first issue`
- `docs-only`
- `translation-needed`

## License

MIT License. See [`LICENSE`](LICENSE).
