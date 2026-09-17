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
│   ├── labels.yml
│   ├── pull_request_template.md
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── en/
│   │   ├── cases/
│   │   │   ├── README.md
│   │   │   ├── customer-support-multi-agent.md
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
│   │   │   ├── design-review-checklist.md
│   │   │   ├── design-review-workshop.md
│   │   │   ├── multi-round-research-discussion.md
│   │   │   ├── overview.md
│   │   │   ├── rag-memory-mcp-flow.md
│   │   │   └── react-pattern.md
│   │   ├── frameworks/
│   │   │   └── framework-map.md
│   │   ├── interviews/
│   │   │   ├── interview-answer-framework.md
│   │   │   ├── interview-framework.md
│   │   │   └── questions/
│   │   │       ├── README.md
│   │   │       ├── l1-components.md
│   │   │       ├── l2-framework-mcp.md
│   │   │       ├── l3-system-design.md
│   │   │       ├── l4-production.md
│   │   │       └── l5-patterns.md
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
│   │   │   └── safety-checklist.md
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
│   │   │   ├── learning-paths.md
│   │   │   ├── industry-benchmark-and-l5-expert-path.md
│   │   │   ├── open-source-inspirations.md
│   │   │   ├── open-source-pattern-matrix.md
│   │   │   ├── practice-handbook.md
│   │   │   ├── quick-navigation.md
│   │   │   ├── reference-map.md
│   │   │   └── search-supplements.md
│   │   ├── agent-top-concrete-framework.md
│   │   ├── l0-first-llm-call.md
│   │   ├── l1-minimal-react-agent.md
│   │   ├── l2-single-agent-mcp.md
│   │   ├── l3-rag-memory-observability.md
│   │   ├── l4-production.md
│   │   ├── l5-custom-patterns.md
│   │   └── README.md
│   └── zh/
│       ├── 文档索引.md              # Chinese documentation index
│       ├── tutorials/               # 学习路径、快速导航、练习手册、开源项目灵感
│       └── ...                     # Chinese mirror with the same directory shape as docs/en
├── examples/
│   ├── README.md
│   ├── agent-decision-trace/
│   ├── memory-vs-evidence/
│   ├── coding-workspace-safety/
│   ├── data-source-policy/
│   ├── coding-task-navigation/
│   ├── agent-eval-regression/
│   ├── github-agent-review/
│   ├── observability-trace/
│   ├── model-gateway/
│   ├── safety-eval/
│   ├── mcp-tool-boundary/
│   ├── memory-index-evidence/
│   ├── release-gate-evidence/
│   └── rag-evidence-refusal/
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
│   ├── l5/
│   │   ├── custom_pattern_lab/
│   │   ├── multilingual_pattern_lab/
│   │   └── pattern_catalog/
│   └── README.md
├── scripts/
│   └── check_repository.py
├── templates/
│   ├── agent-design-template.md
│   ├── article-template.md
│   ├── Agent设计审查Workshop模板.md
│   ├── Agent设计审查范例.md
│   ├── case-study-template.md
│   ├── case-study-writing-guide.md
│   ├── contribution-checklist.md
│   ├── eval-report-template.md
│   ├── 案例研究模板.md
│   ├── 案例研究写作指南.md
│   ├── community-lab-template.md
│   ├── interview-question-template.md
│   ├── lab-template.md
│   ├── monthly-contributor-report.md
│   ├── postmortem-template.md
│   └── README.md
├── docs-site/
│   └── index.html
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
├── LICENSE
└── pyproject.toml
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
- 2026-09-17 dispatch run: [`docs/en/operations/2026-09-17-project-dispatch-run.md`](docs/en/operations/2026-09-17-project-dispatch-run.md)
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
