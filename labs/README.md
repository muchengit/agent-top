---
title: Labs Index
validated_date: 2026-09-16
---

# Labs

Executable Labs are the primary hands-on format for Agent-Top. They run locally without API keys and use deterministic tests to make learning verifiable. The repository currently has 23 Labs and 387 tests.

## Current Labs

### L0

- [`l0/first_llm_call`](l0/first_llm_call/README.md): first LLM call shape and terminology.

### L1

- [`l1/minimal_react_agent`](l1/minimal_react_agent/README.md): minimal ReAct agent without a framework.
- [`l1/guardrail_helpers`](l1/guardrail_helpers/README.md): local tool policy and confirmation boundaries.
- [`l1/multi_turn_state`](l1/multi_turn_state/README.md): multi-turn context state and summary handoff.

### L2

- [`l2/single_agent_mcp`](l2/single_agent_mcp/README.md): single Agent with MCP-style tool boundary and guardrails.
- [`l2/cost_aware_router`](l2/cost_aware_router/README.md): cost and latency-aware routing.
- [`l2/mcp_tool_selection`](l2/mcp_tool_selection/README.md): deterministic MCP tool selection and validation.

### L3

- [`l3/rag_memory_observability`](l3/rag_memory_observability/README.md): RAG, memory, and observability skeleton.
- [`l3/rag_hybrid_search`](l3/rag_hybrid_search/README.md): deterministic hybrid keyword-plus-vector retrieval.
- [`l3/rag_evaluator`](l3/rag_evaluator/README.md): deterministic retrieval evaluation.
- [`l3/multi_round_research_discussion`](l3/multi_round_research_discussion/README.md): multi-round evidence planning and discussion convergence.
- [`l3/multi_agent_supervisor`](l3/multi_agent_supervisor/README.md): deterministic multi-agent routing.

### L4

- [`l4/production_postmortem`](l4/production_postmortem/README.md): executable production postmortem structure, coverage checks, and action-item closure.
- [`l4/regression_gate`](l4/regression_gate/README.md): release gating for safety, trace, rollback, and cost.
- [`l4/cost_and_stability_guardrails`](l4/cost_and_stability_guardrails/README.md): runtime cost, latency, retry, and degradation guardrails.
- [`l4/production_trace_integrity`](l4/production_trace_integrity/README.md): deterministic trace integrity validation for production observability.
- [`l4/deployment_hygiene`](l4/deployment_hygiene/README.md): combined observability, cost, and release gate deploy decision.

### L5

- [`l5/custom_pattern_lab`](l5/custom_pattern_lab/README.md): reusable custom pattern with safety and verification.
- [`l5/pattern_catalog`](l5/pattern_catalog/README.md): reusable pattern catalog with readiness checks.
- [`l5/multilingual_pattern_lab`](l5/multilingual_pattern_lab/README.md): one pattern translated across Python, Node.js, Rust, Go, and TypeScript.
- [`l5/pattern_eval_gate`](l5/pattern_eval_gate/README.md): deterministic gate for patterns entering the catalog.
- [`l5/supervision_incident_response`](l5/supervision_incident_response/README.md): deterministic production supervision and incident response for multi-agent fleets.
- [`l5/vibe_coding_spec`](l5/vibe_coding_spec/README.md): deterministic prompt-readiness check for the Vibe Coding spec-first workflow.

## Run All Tests

```bash
python -m unittest discover -s labs -p "test_*.py"
```

Expected result:

```text
Ran ... tests
OK
```

## Lab Standards

Every Lab should include:

- `README.md` with Goal, Prerequisites, Run, Common Pitfalls, and Self-Check.
- One executable `agent_top_labs_*.py` file.
- One deterministic `test_*.py` file.
- No API key requirement.
- Version anchor in README when relevant.
- Multilingual parity note when examples are translated beyond Python: source of truth, owner, runtime/toolchain versions, smoke command, and parity status.
