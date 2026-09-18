# Agent-Top

CI 状态见 [`.github/workflows/ci.yml`](.github/workflows/ci.yml)。

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
├── .github/       CI workflow, issue templates, labels, PR template
├── docs/          bilingual knowledge base (en + zh), organized by topic
├── docs-site/     static documentation site entry point
├── examples/      no-API-key practice materials (JSONL evidence + READMEs)
├── labs/          executable, deterministic L0-L5 exercises
├── scripts/       local validation and automation tooling
├── templates/     reusable contribution and review formats
├── package.json / requirements.txt / pyproject.toml
└── README.md + governance, security, and roadmap docs
```

Each top-level area has its own entry point:

- [`docs/en/README.md`](docs/en/README.md) and [`docs/zh/README.md`](docs/zh/README.md) organize the bilingual documentation.
- [`labs/README.md`](labs/README.md) lists every executable Lab by capability level; each `labs/l0`-`labs/l5` folder has its own entry README.
- [`examples/README.md`](examples/README.md) explains the evidence-file example sets.
- `scripts/`, `templates/`, and `.github/` keep tooling, formats, and CI in one place each.


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
