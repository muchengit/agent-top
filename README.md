# Agent-Top

Agent-Top is an open-source learning framework for LLM Agent development.

It helps learners and engineers build practical Agent skills from first LLM calls to production-grade multi-agent systems.

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
| L5 | Create original patterns, open-source contributions, and real-world influence |


## Repository Structure

```text
agent-top/
├── .github/                  # GitHub automation, labels, issue/PR templates
├── docs/
│   ├── en/                   # English source documentation
│   │   ├── cases/            # Case studies for realistic Agent scenarios
│   │   ├── community/        # Community operations, translation, labels, events
│   │   ├── concepts/         # Stable Agent concepts and architecture patterns
│   │   ├── frameworks/       # Framework comparison and selection notes
│   │   ├── interviews/       # Interview framework and L1-L5 question sets
│   │   ├── portfolio/        # Portfolio project tracks and evidence guides
│   │   ├── production/       # Evals, safety, observability, rollback, maintenance
│   │   ├── quick-reference/  # Glossary, commands, architecture and production checklists
│   │   ├── tutorials/        # External tutorial-to-Agent-Top reference map
│   │   ├── l0-first-llm-call.md        # L0 tutorial
│   └── zh/                   # Chinese mirror documentation, same directory shape as docs/en
├── labs/                     # Deterministic executable Labs, no API key required
│   ├── l0/                   # First LLM call shape
│   ├── l1/                   # ReAct, guardrails, multi-turn state
│   ├── l2/                   # Tool/MCP boundaries and cost-aware routing
│   ├── l3/                   # RAG, multi-round research, multi-agent supervisor
│   ├── l4/                   # Production postmortems and regression gates
│   └── l5/                   # Reusable pattern labs and pattern catalog
├── scripts/                  # Repository validation scripts
│   └── check_repository.py   # Markdown, link, bilingual, and Lab structure checks
├── templates/                # Contribution templates for articles, Labs, interviews, postmortems
├── docs-site/                # Lightweight static documentation landing page
├── README.md                 # English project overview and repository map
├── README.zh-CN.md           # Chinese project overview and repository map
├── GOVERNANCE.md             # Maintainer roles, review policy, decision principles
├── CONTRIBUTING.md           # English contribution guide
├── CONTRIBUTING.zh-CN.md     # Chinese contribution guide
├── ROADMAP_STATUS.md         # Current completion status and next priorities
├── ROADMAP_STATUS.zh-CN.md   # Chinese roadmap status
├── SECURITY.md               # Security reporting and safe Lab policy
├── SECURITY.zh-CN.md         # Chinese security policy
├── CODE_OF_CONDUCT.zh-CN.md  # Chinese code of conduct
└── agent-top-roadmap.zh-CN.md # Chinese roadmap
```

## Directory Responsibilities

- `docs/en/`: primary English source for all bilingual documentation.
- `docs/zh/`: Chinese mirror with the same module structure as `docs/en`.
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

- Concepts: [`docs/en/concepts`](docs/en/concepts)
- Framework map: [`docs/en/frameworks/framework-map.md`](docs/en/frameworks/framework-map.md)
- Interview framework: [`docs/en/interviews/interview-framework.md`](docs/en/interviews/interview-framework.md)
- Labs: [`labs`](labs)
- Templates: [`templates`](templates)
- Documentation index: [`docs/en/README.md`](docs/en/README.md)
- Governance: [`GOVERNANCE.md`](GOVERNANCE.md)
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
- Adding interview questions or portfolio projects

Good starting labels:

- `good first issue`
- `docs-only`
- `translation-needed`

## License

MIT License. See [`LICENSE`](LICENSE).
