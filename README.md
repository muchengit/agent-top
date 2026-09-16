# Agent-Top

Agent-Top is an open-source learning framework for LLM Agent development.

It helps learners and engineers build practical Agent skills from first LLM calls to production-grade multi-agent systems.

## What This Project Covers

- L0–L5 capability model
- API basics and prompt engineering
- Core Agent components: perception, tool use, planning, and memory
- Mainstream Agent frameworks with version-anchored Labs
- MCP integration
- RAG pipelines
- Long-term memory with Mem0 / Letta
- Multi-agent communication and orchestration
- Evaluation, observability, safety guardrails, deployment, and cost optimization
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

## Local Checks

Run the repository checks:

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
```

## Repository Map

- Concepts: [`docs/concepts`](docs/concepts)
- Framework map: [`docs/frameworks/framework-map.md`](docs/frameworks/framework-map.md)
- Interview framework: [`docs/interviews/interview-framework.md`](docs/interviews/interview-framework.md)
- Labs: [`labs`](labs)
- Templates: [`templates`](templates)
- Documentation index: [`docs/README.md`](docs/README.md)
- Governance: [`GOVERNANCE.md`](GOVERNANCE.md)
- Contributing: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Community: [`docs/community/README.md`](docs/community/README.md)
- Security: [`SECURITY.md`](SECURITY.md)
- Roadmap status: [`ROADMAP_STATUS.md`](ROADMAP_STATUS.md)

## Documentation

See the concrete framework:

- [`docs/agent-top-concrete-framework.md`](docs/agent-top-concrete-framework.md)

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
