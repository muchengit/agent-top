---
title: Framework Map
validated_date: 2026-09-16
---

# Framework Map

Agent-Top treats frameworks as examples of stable patterns. The durable learning target is the pattern; the framework is the versioned implementation.

## Camps

| Camp | Frameworks | Why It Matters | Best Fit | Watch Out For |
| --- | --- | --- | --- | --- |
| Graph orchestration | LangGraph | Explicit state, cycles, checkpoints, and debugging | Complex workflows, human review, retries | Added orchestration overhead |
| Multi-agent | CrewAI, AutoGen | Role-based workflows and conversational coordination | Specialized agents, role boundaries | Coordination cost and hidden loops |
| Lightweight | Smolagents, Agno | Small APIs and fast iteration | Small agents, learning, demos | Production controls must be added |
| SDK | OpenAI, Claude, Google ADK | Direct model platform integration | Platform-native features, tool calls | Ties learning to provider APIs |
| Type-safe | Pydantic AI | Strong schema and validation ergonomics | Structured output and tool contracts | Schema discipline required |
| Enterprise | Semantic Kernel | .NET and enterprise ecosystems, plugins | Corporate stacks, governed plugins | Enterprise-specific constraints |
| RAG | LlamaIndex, Haystack | Retrieval and document pipelines | Search-heavy apps | Retrieval quality still needs evals |
| Optimization | DSPy | Declarative prompt and pipeline optimization | Prompt pipelines and compile-style tuning | Requires strong eval harness |

## Framework Selection Questions

Before choosing a framework, answer:

- Do I need explicit graph state and checkpoints?
- Do I need multi-agent role separation?
- Do I need provider-native model APIs?
- Do I need strong schema validation?
- Do I need enterprise plugin governance?
- Do I need RAG-specific pipelines?
- Do I need prompt optimization?
- Can I maintain this framework for the next quarter?

## Stable Boundaries to Teach

Regardless of framework, teach:

- Perception and context assembly.
- Tool invocation and validation.
- Planning loops and stop conditions.
- Memory lifecycle.
- Retrieval boundaries.
- Observability.
- Safety guardrails.
- Rollback and failure modes.

## Example Policy

Framework-specific code belongs in Labs. Concepts should stay independent of one framework where possible.

Each framework-sensitive example should include:

```yaml
validated_date: YYYY-MM-DD
tested_against: framework-name x.y.z
```

## Anti-Staleness Rules

- Separate concept text from framework-specific code.
- Keep framework examples small.
- Prefer pattern descriptions over framework APIs in tutorials.
- Mark breaking changes immediately.
- Use `sync-required` when translations lag.
- Archive stale examples with replacement links.

## Framework Code Placement

```text
docs/en/*.md              Stable concepts and follow-along tutorials
labs/l*/...               Runnable, version-anchored examples
docs/frameworks/...       Cross-framework comparison
docs/interviews/...       Framework trade-off questions
```

## Framework Trade-Off Examples

### LangGraph vs Plain Loop

Use LangGraph when the system needs:

- Persistent state.
- Cycles with explicit checkpoints.
- Human approval nodes.
- Replayable debugging.

Use a plain loop when the system needs:

- Minimal code.
- Teaching clarity.
- Few branches.
- Easy local testing.

### CrewAI/AutoGen vs Single Agent

Use multi-agent when:

- Work can be decomposed cleanly.
- Specialized roles improve verification or isolation.
- The team can own each role.

Avoid multi-agent when:

- A single Agent with tools is sufficient.
- Shared state coordination is complex.
- Debugging already feels hard.

### RAG Framework vs Custom Retrieval Lab

Use a RAG framework when:

- The document pipeline has many components.
- Evaluation needs mature indexing support.

Use a custom retrieval Lab when:

- The learning goal is retrieval boundaries.
- You need deterministic local examples.

## Maintainer Note

When adding a new framework:

1. Identify the camp.
2. Keep tutorial concepts framework-independent.
3. Add a small Lab only if it teaches a stable boundary.
4. Include `validated_date` and `tested_against`.
5. Add a translation-needed marker if ZH content needs work.
