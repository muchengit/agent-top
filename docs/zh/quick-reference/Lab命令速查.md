---
i18n-key: quick-reference-lab-command-cheatsheet
last-synced: 2026-09-16
validated_date: 2026-09-16
---

# Lab 命令速查

所有 Lab 都是确定性的，不需要 API key。

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

## 全部 Lab 命令

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
```

## 常用调试命令

```bash
python -m unittest -v labs.l3.rag_evaluator.test_lab
python -m unittest -v labs.l4.regression_gate.test_lab
rg -n "def test_|assert" labs/l3 labs/l4
rg -n "validated_date|tested_against" docs labs
python scripts/check_repository.py
```

## 排错

- Lab 失败时，先单独运行该 Lab 隔离问题。
- 链接检查失败时，从当前 Markdown 文件位置核对相对路径。
- 双语检查失败时，确认 `i18n-key` 和 `last-synced` frontmatter 匹配。
- Python lint 失败时，运行 `python -m ruff check .`，不要为 Lab 代码随意添加例外。
