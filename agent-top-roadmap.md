# Agent-Top Roadmap


中文版：[`agent-top-roadmap.zh-CN.md`](agent-top-roadmap.zh-CN.md)

The Agent-Top roadmap defines the high-level learning path, release cadence, and community-building direction. For concrete execution details, see [`docs/en/agent-top-concrete-framework.md`](docs/en/agent-top-concrete-framework.md).

## Goals

Help learners grow from their first LLM call into engineers who can design, evaluate, deploy, and postmortem production-grade Agent systems.

Core goals:

- Organize learning content around the L0-L5 capability model.
- Replace short-lived framework chasing with stable patterns.
- Make content reproducible with Markdown plus executable Labs.
- Lower the cost of staleness with version anchors and CI freshness tooling.
- Connect learning and job hunting through interviews and portfolio paths.
- Sustain long-term maintenance with bilingual content, contribution levels, and community governance.

## Roadmap Phases

### Phase 0: Framework and Documentation Foundation

Status: ✅ Complete

Goal: Establish project structure, capability model, and contribution conventions.

Deliverables:

- `README.md`
- `README.zh-CN.md`
- `agent-top-roadmap.md`
- `docs/en/agent-top-concrete-framework.md`
- Contribution entry points and draft label conventions

Exit criteria: a new reader can understand the project positioning, capability levels, and contribution paths within 10 minutes.

### Phase 1: L0-L1 Onboarding and Core Components

Status: ✅ Complete

Goal: Run the first LLM call and understand the four core Agent components.

Deliverables:

- L0 API demo Lab
- Prompt basics
- Token / context window / system prompt quick reference
- Minimal pure-Python ReAct Agent Lab
- Responsibilities for perception, tools, planning, and memory

Exit criteria: learners can explain core Agent responsibilities and run a minimal ReAct loop without a framework.

### Phase 2: L2 Framework Layer and Reliable Single Agent

Status: ✅ Complete

Goal: Build a reliable single Agent with a mainstream framework.

Deliverables:

- Single-Agent project template
- Framework comparison notes
- At least one MCP server integration Lab
- Guardrail basics Lab

Exit criteria: complete a single-Agent project and explain framework-selection trade-offs.

### Phase 3: L3 System Capabilities

Status: ✅ Complete

Goal: Build end-to-end Agent systems.

Deliverables:

- Self-built RAG pipeline Lab
- Mem0 / Letta memory integration
- Langfuse observability example
- Multi-Agent communication and orchestration example
- RAG to memory to multi-Agent to MCP data-flow case

Exit criteria: learners can explain system data flow and produce an evaluation report.

### Phase 4: L4 Production Hardening

Status: ✅ Complete

Goal: Push Agent systems to production engineering.

Deliverables:

- Multi-Agent topology design template
- Evaluation metrics and automated regression
- Safety guardrail checklist
- Deployment and cost-optimization guide
- Postmortem template

Exit criteria: complete a production design, evaluation, and live postmortem.

### Phase 5: L5 Expert Path and Ecosystem Building

Status: 🔄 In progress

Goal: Form original patterns, open-source influence, and team-level Agent infrastructure capabilities.

Deliverables:

- Original pattern case studies
- Open-source PR guide
- Vibe Coding spec workflow with a deterministic readiness Lab and bilingual template
- Tech talk / paper reading templates
- Team Agent infrastructure design guide

Exit criteria: contributors can produce external-influence evidence such as PRs, papers, talks, cases, or tools.

## Content Production Cadence

- Biweekly tutorial: advance the core capability path
- Monthly interview questions: connect learning with job-hunting evaluation
- Quarterly roadmap review: adjust content priorities
- Biweekly paper reading: track research directions
- Monthly showcase: present portfolio and community outcomes
- Quarterly Hackathon: focus on complex cases

## Quality Mechanisms

Every piece of content must include:

- Target capability level Lx
- `validated_date`
- `tested_against`
- Prerequisites
- Executable steps
- Common pitfalls
- Self-check questions

Suggested CI checks:

- Broken links
- Markdown build
- Spelling
- i18n sync
- Missing version anchors
- Deprecated content references

## Community and Contributions

Role path:

- Contributor → Reviewer → Maintainer → Core

Contribution paths:

- Writing
- Translation
- Review
- Maintenance

Beginner labels:

- `good first issue`
- `docs-only`
- `translation-needed`

Bilingual strategy:

- EN is the primary source
- ZH is claimed through `translation-needed`
- Chapter goal: finish the first translation within ≤3 days after claiming
- CI tracks `last-synced` lag and automatically opens `sync-required`

## Current Priorities

1. Initialize the repository and complete base documentation
2. Establish directory structure and contribution conventions
3. Complete the L0 first API demo Lab
4. Complete the L1 minimal ReAct Agent Lab
5. Establish version anchors and CI checks
