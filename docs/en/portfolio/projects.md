---
title: Portfolio Project Tracks
validated_date: 2026-09-18
i18n-key: portfolio-projects
last-synced: 2026-09-18
---

# Portfolio Project Tracks

A strong Agent portfolio should show four gradients: RAG and memory, tool orchestration, multi-agent coordination, and abstraction.

## Track 1: Personal Knowledge Base Agent

Shows RAG + memory.

### Goal

Build a local Agent that can search personal notes, answer from retrieved evidence, and remember durable user preferences without requiring an API key for the core Lab.

### Minimum Scope

- Local document corpus.
- Chunking and retrieval.
- Answer generation with source references.
- User preference memory.
- Refusal when evidence is missing.
- Eval cases for stale or irrelevant documents.

### Key Decisions

- How to separate retrieved facts from remembered facts.
- How to cite sources.
- How to handle conflicting notes.
- How to prevent memory from overriding retrieved evidence.

### Evidence to Include

- Eval results.
- Example traces.
- Failure cases.
- Prompt and retrieval trade-offs.
- A short production checklist.

### Stretch Goal

Add long-term memory in Mem0 or Letta style, with privacy notes and forgetting rules.

## Track 2: Enterprise Multi-Tool Agent

Shows tool orchestration and MCP-style boundaries.

### Goal

Build a single Agent that can route between read-only lookup, write actions, and human escalation.

### Minimum Scope

- Tool allowlist.
- Input and output validation.
- Permission classification.
- Destructive action confirmation.
- Tool failure handling.
- Observability logs.

### Key Decisions

- Which tools are read-only versus write-capable.
- Which actions require approval.
- How ambiguous tool results are handled.
- How tool failures differ from empty results.

### Evidence to Include

- Tool schema table.
- Trace examples for success, rejection, and failure.
- Cost and latency notes.
- Rollback plan for risky tool paths.

### Stretch Goal

Expose the tool gateway through MCP-style interfaces and include transport/auth debugging notes.

## Track 3: Multi-Agent Collaboration System

Shows orchestration, consistency, and error isolation.

### Goal

Build a customer support system where router, retrieval, tool, verification, and escalation agents have explicit responsibilities.

### Minimum Scope

- Router agent.
- Retrieval agent.
- Tool execution agent.
- Verification agent.
- Escalation path.
- Shared trace model.
- Error isolation and retry rules.

### Key Decisions

- What state is shared versus isolated.
- Who can make final user-facing claims.
- How verification can override a subagent.
- How the system escalates ambiguous or unsafe cases.

### Evidence to Include

- Sequence diagram or Mermaid flow.
- Inter-agent message examples.
- Regression evals.
- Incident story with root cause and fix.

### Stretch Goal

Add a human-in-the-loop review queue and explain approval boundaries.

## Track 4: Custom Framework or Pattern

Shows abstraction, engineering depth, and contribution readiness.

### Goal

Design a reusable pattern or mini framework with stable inputs, outputs, safety checks, verification, and tests.

### Minimum Scope

- Pattern spec.
- Deterministic Lab.
- Unit tests.
- Tutorial with expected outputs.
- Version anchors.
- Failure mode documentation.
- Maintenance notes.

### Key Decisions

- What the pattern should not do.
- What safety checks run before execution.
- How verification becomes mandatory.
- How contributors maintain the pattern.

### Evidence to Include

- README and tutorial.
- Test output.
- Before/after comparison with framework-specific implementation.
- PR-ready contribution notes.

### Stretch Goal

Submit an open-source PR, write a short paper, or give a talk that teaches the pattern.

## Portfolio Presentation Template

For each project, write one page:

```markdown
# Project Name

## Problem
What user or engineering problem did you solve?

## Architecture
What components exist and why?

## Evaluation
What evals prove the project works?

## Failure Modes
What can break and how do you handle it?

## Production Readiness
What auth, safety, rollback, and observability controls exist?

## Trade-offs
What did you accept to move faster?

## Evidence
Links to traces, tests, docs, or PRs.
```

## Portfolio Quality Bar

A portfolio project should prove:

- The system can run.
- The system can be tested.
- The system can fail safely.
- The author can explain trade-offs.
- The author can improve the project under review.
