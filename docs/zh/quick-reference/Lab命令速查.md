---
i18n-key: quick-reference-lab-command-cheatsheet
last-synced: 2026-09-16
validated_date: 2026-09-16
---

Lab 命令速查

## 运行全部 Lab

```bash
python -m unittest discover -s labs -p "test_*.py"
```

## 运行仓库检查

```bash
python scripts/check_repository.py
python -m compileall -q labs scripts
python -m ruff check .
```

## 常用 Lab 命令

```bash
python -m unittest labs.l1.minimal_react_agent.test_lab
python -m unittest labs.l1.multi_turn_state.test_lab
python -m unittest labs.l2.cost_aware_router.test_lab
python -m unittest labs.l3.rag_evaluator.test_lab
python -m unittest labs.l3.multi_agent_supervisor.test_lab
python -m unittest labs.l4.regression_gate.test_lab
python -m unittest labs.l5.pattern_catalog.test_lab
```

