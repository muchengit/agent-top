---
title: Lab Command Cheatsheet
validated_date: 2026-09-17
i18n-key: quick-reference-lab-command-cheatsheet
last-synced: 2026-09-17
---

# Lab Command Cheatsheet

All Labs are deterministic and do not require an API key. Labs live under `labs/l0`
through `labs/l5`; each lab has an `agent_top_labs_*.py` module, a `test_lab.py`, and a
`README.md` with Goal, Run, and Self-Check sections.

## Run All Labs

Run the entire suite with unittest discovery:

```bash
python -m unittest discover -s labs -p "test_*.py"
```

Run with verbose output to see every test name:

```bash
python -m unittest discover -v -s labs -p "test_*.py"
```

## Run Repository Checks

```bash
python scripts/check_repository.py
python -m compileall -q labs scripts
python -m ruff check .
python scripts/smoke_multilingual_labs.py
```

- `check_repository.py` validates required paths, frontmatter dates, bilingual key pairs,
  relative links, lab README sections, and example JSONL files.
- `smoke_multilingual_labs.py` verifies that the L5 multilingual pattern lab works across
  Python, Node.js, Rust, Go, and TypeScript.

## All Lab Commands

Run any lab in isolation with its dotted module path. This is the fastest way to debug.

```bash
python -m unittest labs.l0.first_llm_call.test_lab
python -m unittest labs.l1.guardrail_helpers.test_lab
python -m unittest labs.l1.minimal_react_agent.test_lab
python -m unittest labs.l1.multi_turn_state.test_lab
python -m unittest labs.l2.cost_aware_router.test_lab
python -m unittest labs.l2.single_agent_mcp.test_lab
python -m unittest labs.l3.rag_evaluator.test_lab
python -m unittest labs.l3.rag_memory_observability.test_lab
python -m unittest labs.l3.multi_agent_supervisor.test_lab
python -m unittest labs.l3.multi_round_research_discussion.test_lab
python -m unittest labs.l4.regression_gate.test_lab
python -m unittest labs.l4.cost_and_stability_guardrails.test_lab
python -m unittest labs.l4.production_postmortem.test_lab
python -m unittest labs.l5.custom_pattern_lab.test_lab
python -m unittest labs.l5.pattern_catalog.test_lab
python -m unittest labs.l5.multilingual_pattern_lab.test_lab
```

Run labs from the same level together in one process:

```bash
python -m unittest labs.l1.guardrail_helpers.test_lab labs.l1.minimal_react_agent.test_lab labs.l1.multi_turn_state.test_lab
```

## Lab Map

| Level | Lab | What it practices | Run command |
| --- | --- | --- | --- |
| l0 | first_llm_call | Basic LLM request/response shape without an API key | `python -m unittest labs.l0.first_llm_call.test_lab` |
| l1 | guardrail_helpers | Local tool policy decisions without calling external tools | `python -m unittest labs.l1.guardrail_helpers.test_lab` |
| l1 | minimal_react_agent | Tiny ReAct-style agent from first principles | `python -m unittest labs.l1.minimal_react_agent.test_lab` |
| l1 | multi_turn_state | Multi-turn state, recent-message windows, summary handoff | `python -m unittest labs.l1.multi_turn_state.test_lab` |
| l2 | cost_aware_router | Route by tool need, retrieval need, confirmation, latency budget | `python -m unittest labs.l2.cost_aware_router.test_lab` |
| l2 | single_agent_mcp | Single agent with a small MCP-style tool interface | `python -m unittest labs.l2.single_agent_mcp.test_lab` |
| l3 | rag_evaluator | Retrieval evaluation with required sources and refusal cases | `python -m unittest labs.l3.rag_evaluator.test_lab` |
| l3 | rag_memory_observability | Retrieval, memory, generation, observability skeleton | `python -m unittest labs.l3.rag_memory_observability.test_lab` |
| l3 | multi_agent_supervisor | Assign work to specialized agents from a task profile | `python -m unittest labs.l3.multi_agent_supervisor.test_lab` |
| l3 | multi_round_research_discussion | Multi-round research: plan, select evidence, clarify, answer | `python -m unittest labs.l3.multi_round_research_discussion.test_lab` |
| l4 | regression_gate | Release gating for safety, trace completeness, rollback, cost | `python -m unittest labs.l4.regression_gate.test_lab` |
| l4 | cost_and_stability_guardrails | Runtime guardrails for cost, latency, retries, degradation | `python -m unittest labs.l4.cost_and_stability_guardrails.test_lab` |
| l4 | production_postmortem | Structured postmortem with root causes and action items | `python -m unittest labs.l4.production_postmortem.test_lab` |
| l4 | production_trace_integrity | Deterministic trace integrity validation for production observability | `python -m unittest labs.l4.production_trace_integrity.test_lab` |
| l4 | deployment_hygiene | Combined observability, cost, and release gate deploy decision | `python -m unittest labs.l4.deployment_hygiene.test_lab` |
| l5 | custom_pattern_lab | Abstract a reusable pattern with stable contracts | `python -m unittest labs.l5.custom_pattern_lab.test_lab` |
| l5 | pattern_catalog | Define reusable patterns with safety checks and verification | `python -m unittest labs.l5.pattern_catalog.test_lab` |
| l5 | multilingual_pattern_lab | One pattern in Python, Node.js, Rust, Go, TypeScript | `python -m unittest labs.l5.multilingual_pattern_lab.test_lab` |
| l5 | pattern_eval_gate | Deterministic gate for patterns entering the catalog | `python -m unittest labs.l5.pattern_eval_gate.test_lab` |
| l5 | supervision_incident_response | Deterministic production supervision and incident response | `python -m unittest labs.l5.supervision_incident_response.test_lab` |

## Levels at a Glance

- **l0**: Orientation. `first_llm_call` teaches the LLM request/response shape without an API key.
- **l1**: Core mechanics. Guardrails, a minimal ReAct agent, and multi-turn state with no external calls.
- **l2**: Routing and integration. Cost-aware routing and a single agent with an MCP-style tool interface.
- **l3**: Composition. RAG evaluation, memory and observability, supervisors, and multi-round research.
- **l4**: Production readiness. Regression gates, cost and stability guardrails, and postmortems.
- **l5**: Pattern engineering. Reusable pattern catalogs, custom patterns, and one pattern implemented in five languages.

## Inspecting a Lab

Each lab directory follows the same shape, for example `labs/l3/rag_evaluator`:

```text
labs/l3/rag_evaluator/
  README.md
  __init__.py
  agent_top_labs_l3_rag_evaluator.py
  test_lab.py
```

Useful inspection commands:

```bash
ls labs/l3/rag_evaluator/
sed -n '/^## Goal/,/^## Prerequisites/p' labs/l3/rag_evaluator/README.md
rg -n "def test_" labs/l3/rag_evaluator/test_lab.py
rg -n "def " labs/l3/rag_evaluator/agent_top_labs_l3_rag_evaluator.py
```

## Common Failure Modes and Fixes

- **ImportError or module not found**: the lab module path must be dotted and relative to the
  repository root, such as `labs.l3.rag_evaluator.test_lab`, and you must run from the root.
- **Test count mismatch**: if you added a test method, keep the module discoverable and avoid
  changing shared fixtures that other labs rely on.
- **Bilingual frontmatter mismatch**: the `zh` mirror must keep the same `i18n-key` and an
  up-to-date `last-synced`; `check_repository.py` fails otherwise.
- **Stale date**: any doc with `validated_date` older than 180 days fails
  `check_repository.py`, so refresh the date when you re-validate content.
- **Broken relative links**: link targets are resolved from the directory of the current
  Markdown file; verify the path relative to that file, not the repository root.

## Verification Checklist

Before opening a pull request, run in order:

```bash
python -m unittest discover -s labs -p "test_*.py"
python scripts/check_repository.py
python -m compileall -q labs scripts
python -m ruff check .
python scripts/smoke_multilingual_labs.py
```

## Useful Debugging Commands

```bash
python -m unittest -v labs.l3.rag_evaluator.test_lab
python -m unittest -v labs.l4.regression_gate.test_lab
rg -n "def test_|assert" labs/l3 labs/l4
rg -n "validated_date|tested_against" docs labs
python scripts/check_repository.py
```

Run a single test case by class and method:

```bash
python -m unittest -v labs.l3.rag_evaluator.test_lab.RagEvaluatorTest.test_refuses_without_required_source
```

List every test method in a lab:

```bash
rg -n "def test_" labs/l3/rag_evaluator/test_lab.py
```

## Troubleshooting

- If a Lab fails, run it alone first to isolate the scenario.
- If repository checks fail on links, verify relative paths from the current Markdown file.
- If bilingual checks fail, confirm matching `i18n-key` and `last-synced` frontmatter.
- If lint fails after Python edits, run `python -m ruff check .` and avoid adding exceptions for generated or Lab code.
- If the multilingual smoke test fails, check each language directory under `labs/l5/multilingual_pattern_lab` and rerun `python scripts/smoke_multilingual_labs.py`.
- If a command is not found, confirm you are in the repository root, since all commands use repository-root-relative paths.
