---
title: Agent Tutorial Reference Map
validated_date: 2026-09-16
---

# Agent Tutorial Reference Map

This page maps common topics from public Agent tutorials and frameworks into Agent-Top's stable learning assets.

The goal is not to copy external tutorials. The goal is to use them as prompts for mapping, verifying, and producing maintainable outputs.

## How to Use This Map

When you read an external Agent tutorial, ask:

1. Which Agent-Top capability level does it map to?
2. Is the core idea a stable pattern or framework-specific API?
3. Which local Lab can prove the concept?
4. What failure mode should be added?
5. What documentation or exercise should improve?

## Topic-to-Agent-Top Map

| External Tutorial Topic | Agent-Top Concept | Local Lab or Case | Output to Produce |
| --- | --- | --- | --- |
| First LLM call | [`../concepts/overview.md`](../concepts/overview.md) | [`../../labs/l0/first_llm_call/README.md`](../../labs/l0/first_llm_call/README.md) | Explain token, context, system prompt |
| Prompt engineering | [`../concepts/overview.md`](../concepts/overview.md) | [`../../labs/l0/first_llm_call/README.md`](../../labs/l0/first_llm_call/README.md) | Write a safer system prompt |
| ReAct or reasoning-action loop | [`../concepts/react-pattern.md`](../concepts/react-pattern.md) | [`../../labs/l1/minimal_react_agent/README.md`](../../labs/l1/minimal_react_agent/README.md) | Add stop conditions |
| Tool calling | [`../concepts/agent-system-architecture.md`](../concepts/agent-system-architecture.md) | [`../../labs/l2/single_agent_mcp/README.md`](../../labs/l2/single_agent_mcp/README.md) | Add guardrail checks |
| MCP-style tools | [`../frameworks/framework-map.md`](../frameworks/framework-map.md) | [`../../labs/l2/cost_aware_router/README.md`](../../labs/l2/cost_aware_router/README.md) | Route tool calls safely |
| RAG | [`../concepts/rag-memory-mcp-flow.md`](../concepts/rag-memory-mcp-flow.md) | [`../../labs/l3/rag_evaluator/README.md`](../../labs/l3/rag_evaluator/README.md) | Add a refusal eval |
| Multi-round research | [`../concepts/multi-round-research-discussion.md`](../concepts/multi-round-research-discussion.md) | [`../../labs/l3/multi_round_research_discussion/README.md`](../../labs/l3/multi_round_research_discussion/README.md) | Plan search queries |
| Memory | [`../concepts/overview.md`](../concepts/overview.md) | [`../../labs/l1/multi_turn_state/README.md`](../../labs/l1/multi_turn_state/README.md) | Decide what to summarize |
| Multi-agent orchestration | [`../concepts/agent-system-architecture.md`](../concepts/agent-system-architecture.md) | [`../../labs/l3/multi_agent_supervisor/README.md`](../../labs/l3/multi_agent_supervisor/README.md) | Assign supervisor routes |
| LangGraph-style state | [`../frameworks/framework-map.md`](../frameworks/framework-map.md) | [`../../labs/l1/multi_turn_state/README.md`](../../labs/l1/multi_turn_state/README.md) | Explain state ownership |
| CrewAI/AutoGen-style roles | [`../frameworks/framework-map.md`](../frameworks/framework-map.md) | [`../../labs/l3/multi_agent_supervisor/README.md`](../../labs/l3/multi_agent_supervisor/README.md) | Define role boundaries |
| Lightweight agent SDK | [`../frameworks/framework-map.md`](../frameworks/framework-map.md) | [`../../labs/l1/minimal_react_agent/README.md`](../../labs/l1/minimal_react_agent/README.md) | Compare SDK vs loop |
| Pydantic AI structured output | [`../frameworks/framework-map.md`](../frameworks/framework-map.md) | [`../../labs/l1/guardrail_helpers/README.md`](../../labs/l1/guardrail_helpers/README.md) | Validate schema-like inputs |
| DSPy-style optimization | [`../frameworks/framework-map.md`](../frameworks/framework-map.md) | [`../../labs/l4/regression_gate/README.md`](../../labs/l4/regression_gate/README.md) | Define eval gate |
| Evaluation and observability | [`../production/evals-checklist.md`](../production/evals-checklist.md) | [`../../labs/l4/regression_gate/README.md`](../../labs/l4/regression_gate/README.md) | Build release gate |
| Safety guardrails | [`../production/safety-checklist.md`](../production/safety-checklist.md) | [`../../labs/l1/guardrail_helpers/README.md`](../../labs/l1/guardrail_helpers/README.md) | Classify tool risk |
| Postmortem and incident response | [`../production/quarterly-maintenance.md`](../production/quarterly-maintenance.md) | [`../../labs/l4/production_postmortem/README.md`](../../labs/l4/production_postmortem/README.md) | Write action items |
| Pattern contribution | [`../concepts/agent-system-architecture.md`](../concepts/agent-system-architecture.md) | [`../../labs/l5/pattern_catalog/README.md`](../../labs/l5/pattern_catalog/README.md) | Draft a reusable pattern |

## Suggested Learning Path from External Tutorials

1. Read one beginner LLM Agent tutorial.
2. Map it to L0 or L1 in Agent-Top.
3. Run the related local Lab.
4. Write one difference between the external tutorial and Agent-Top's pattern-first view.
5. Add a follow-up issue if the gap is useful.

## Example Discussion Notes

```markdown
# Tutorial Mapping Notes

## Source Topic
Briefly name the topic.

## Stable Concept
What pattern survives framework changes?

## Framework-Specific Parts
What should stay in a Lab or comparison table?

## Agent-Top Mapping
Which capability level, Lab, and case study match?

## Gap or Follow-up
What should Agent-Top add, translate, or improve?
```

## Maintainer Rule

Do not paste large chunks of external tutorials into Agent-Top. Add mappings, summaries, trade-off notes, and original exercises.
