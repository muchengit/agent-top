---
i18n-key: quick-reference-lab-command-cheatsheet
last-synced: 2026-09-17
validated_date: 2026-09-17
---

# Lab 命令速查

所有 Lab 都是确定性的，不需要 API key。Lab 位于 `labs/l0` 到 `labs/l5`；每个 lab 包含
`agent_top_labs_*.py` 模块、`test_lab.py` 和带 Goal、Run、Self-Check 等章节的 `README.md`。

## 运行全部 Lab

用 unittest discovery 跑完整套件：

```bash
python -m unittest discover -s labs -p "test_*.py"
```

加 verbose 输出查看每个测试名：

```bash
python -m unittest discover -v -s labs -p "test_*.py"
```

## 运行仓库检查

```bash
python scripts/check_repository.py
python -m compileall -q labs scripts
python -m ruff check .
python scripts/smoke_multilingual_labs.py
```

- `check_repository.py` 校验必需路径、frontmatter 日期、双语 key 配对、相对链接、lab README 章节和 example JSONL 文件。
- `smoke_multilingual_labs.py` 验证 L5 多语言模式 lab 在 Python、Node.js、Rust、Go 和 TypeScript 下都能工作。

## 全部 Lab 命令

用带点的模块路径单独运行任意 lab，这是最快的调试方式：

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

在同一个进程里运行同一层的多个 lab：

```bash
python -m unittest labs.l1.guardrail_helpers.test_lab labs.l1.minimal_react_agent.test_lab labs.l1.multi_turn_state.test_lab
```

## Lab 地图

| Level | Lab | 练习内容 | 运行命令 |
| --- | --- | --- | --- |
| l0 | first_llm_call | 无 API key 的 LLM 请求/响应基础形状 | `python -m unittest labs.l0.first_llm_call.test_lab` |
| l1 | guardrail_helpers | 不调用外部工具的本地工具策略决策 | `python -m unittest labs.l1.guardrail_helpers.test_lab` |
| l1 | minimal_react_agent | 从第一性原理构建极简 ReAct agent | `python -m unittest labs.l1.minimal_react_agent.test_lab` |
| l1 | multi_turn_state | 多轮状态、最近消息窗口、摘要 handoff | `python -m unittest labs.l1.multi_turn_state.test_lab` |
| l2 | cost_aware_router | 按工具需求、检索需求、确认状态、延迟预算路由 | `python -m unittest labs.l2.cost_aware_router.test_lab` |
| l2 | single_agent_mcp | 单 Agent + 小型 MCP 风格工具接口 | `python -m unittest labs.l2.single_agent_mcp.test_lab` |
| l2 | mcp_tool_selection | 确定性的 MCP 工具选择与校验 | `python -m unittest labs.l2.mcp_tool_selection.test_lab` |
| l3 | rag_evaluator | 带必需来源和 refusal 用例的检索评估 | `python -m unittest labs.l3.rag_evaluator.test_lab` |
| l3 | rag_memory_observability | 检索、记忆、生成、可观测性骨架 | `python -m unittest labs.l3.rag_memory_observability.test_lab` |
| l3 | multi_agent_supervisor | 从任务 profile 给专业 agent 分配工作 | `python -m unittest labs.l3.multi_agent_supervisor.test_lab` |
| l3 | multi_round_research_discussion | 多轮研究：规划、选证据、澄清、回答 | `python -m unittest labs.l3.multi_round_research_discussion.test_lab` |
| l3 | rag_hybrid_search | 确定性的关键词+向量混合检索 | `python -m unittest labs.l3.rag_hybrid_search.test_lab` |
| l4 | regression_gate | 安全、trace 完整性、rollback、成本的发布门禁 | `python -m unittest labs.l4.regression_gate.test_lab` |
| l4 | cost_and_stability_guardrails | 成本、延迟、重试、降级的运行时 guardrails | `python -m unittest labs.l4.cost_and_stability_guardrails.test_lab` |
| l4 | production_postmortem | 带根因和行动项的结构化 postmortem | `python -m unittest labs.l4.production_postmortem.test_lab` |
| l4 | production_trace_integrity | 面向生产可观测性的确定性 trace 完整性校验 | `python -m unittest labs.l4.production_trace_integrity.test_lab` |
| l4 | deployment_hygiene | 可观测性、成本与发布门禁合并的部署决策 | `python -m unittest labs.l4.deployment_hygiene.test_lab` |
| l5 | custom_pattern_lab | 抽象带稳定契约的可复用模式 | `python -m unittest labs.l5.custom_pattern_lab.test_lab` |
| l5 | pattern_catalog | 定义带安全检查与验证的可复用模式 | `python -m unittest labs.l5.pattern_catalog.test_lab` |
| l5 | multilingual_pattern_lab | 一个模式用 Python、Node.js、Rust、Go、TypeScript 实现 | `python -m unittest labs.l5.multilingual_pattern_lab.test_lab` |
| l5 | pattern_eval_gate | 模式进入目录前的确定性门禁 | `python -m unittest labs.l5.pattern_eval_gate.test_lab` |
| l5 | supervision_incident_response | 多 Agent 生产监督与事件响应的确定性决策 | `python -m unittest labs.l5.supervision_incident_response.test_lab` |

## 各层一览

- **l0**：入门。`first_llm_call` 在无需 API key 的情况下讲解 LLM 请求/响应形状。
- **l1**：核心机制。Guardrails、极简 ReAct agent 和纯本地的多轮状态。
- **l2**：路由与集成。成本感知路由和带 MCP 风格工具接口的单 Agent。
- **l3**：组合。RAG 评估、记忆与可观测性、supervisor 和多轮研究。
- **l4**：生产就绪。Regression gates、成本与稳定性 guardrails 和 postmortem。
- **l5**：模式工程。可复用模式目录、自定义模式，以及一个模式五种语言实现。

## 查看一个 Lab

每个 lab 目录结构相同，例如 `labs/l3/rag_evaluator`：

```text
labs/l3/rag_evaluator/
  README.md
  __init__.py
  agent_top_labs_l3_rag_evaluator.py
  test_lab.py
```

常用查看命令：

```bash
ls labs/l3/rag_evaluator/
sed -n '/^## Goal/,/^## Prerequisites/p' labs/l3/rag_evaluator/README.md
rg -n "def test_" labs/l3/rag_evaluator/test_lab.py
rg -n "def " labs/l3/rag_evaluator/agent_top_labs_l3_rag_evaluator.py
```

## 常见失败模式与修复

- **ImportError 或找不到模块**：模块路径必须是相对仓库根目录的带点路径，例如 `labs.l3.rag_evaluator.test_lab`，并且要从根目录运行。
- **测试数量不符**：新增测试方法后保持模块可被发现，不要改动其他 lab 依赖的共享 fixture。
- **双语 frontmatter 不匹配**：zh 镜像必须保持相同 `i18n-key` 和最新的 `last-synced`，否则 `check_repository.py` 会失败。
- **日期过期**：任何 `validated_date` 超过 180 天的文档都会让 `check_repository.py` 失败，重新核验内容时要更新日期。
- **相对链接损坏**：链接目标以当前 Markdown 文件所在目录为基准解析，要按该文件而不是仓库根目录核对路径。

## 验证清单

提 PR 前按顺序运行：

```bash
python -m unittest discover -s labs -p "test_*.py"
python scripts/check_repository.py
python -m compileall -q labs scripts
python -m ruff check .
python scripts/smoke_multilingual_labs.py
```

## 常用调试命令

```bash
python -m unittest -v labs.l3.rag_evaluator.test_lab
python -m unittest -v labs.l4.regression_gate.test_lab
rg -n "def test_|assert" labs/l3 labs/l4
rg -n "validated_date|tested_against" docs labs
python scripts/check_repository.py
```

按类和方法运行单个测试用例：

```bash
python -m unittest -v labs.l3.rag_evaluator.test_lab.RagEvaluatorTest.test_refuses_without_required_source
```

列出某个 lab 的全部测试方法：

```bash
rg -n "def test_" labs/l3/rag_evaluator/test_lab.py
```

## 排错

- Lab 失败时，先单独运行该 Lab 隔离问题。
- 链接检查失败时，从当前 Markdown 文件位置核对相对路径。
- 双语检查失败时，确认 `i18n-key` 和 `last-synced` frontmatter 匹配。
- Python lint 失败时，运行 `python -m ruff check .`，不要为 Lab 代码随意添加例外。
- 多语言 smoke 测试失败时，检查 `labs/l5/multilingual_pattern_lab` 下每个语言目录，并重跑 `python scripts/smoke_multilingual_labs.py`。
- 命令找不到时，确认在仓库根目录运行，因为所有命令都使用相对仓库根目录的路径。
