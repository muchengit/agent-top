---
title: Lab Command Cheatsheet
validated_date: 2026-09-16
i18n-key: quick-reference-lab-command-cheatsheet
last-synced: 2026-09-16
---

# Lab Command Cheatsheet

All Labs are deterministic and do not require an API key.

## Run All Labs

```bash
python -m unittest discover -s labs -p "test_*.py"
```

## Run Repository Checks

```bash
python scripts/check_repository.py
python -m compileall -q labs scripts
python -m ruff check .
```

## All Lab Commands

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

## Troubleshooting

- If a Lab fails, run it alone first to isolate the scenario.
- If repository checks fail on links, verify relative paths from the current Markdown file.
- If bilingual checks fail, confirm matching `i18n-key` and `last-synced` frontmatter.
- If lint fails after Python edits, run `python -m ruff check .` and avoid adding exceptions for generated or Lab code.
