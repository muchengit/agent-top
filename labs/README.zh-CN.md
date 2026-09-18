---
title: Labs 索引
validated_date: 2026-09-19
i18n-key: labs-readme
last-synced: 2026-09-19
---

# Labs

可执行 Labs 是 Agent-Top 的主要动手学习形式。它们在本地运行、无需 API key，并通过确定性测试保证学习可验证。本仓库现有 23 个 Lab、444 个测试。

## 当前 Labs

### L0

- [`l0/first_llm_call`](l0/first_llm_call/README.md)：首次 LLM 调用的形态与术语。

### L1

- [`l1/minimal_react_agent`](l1/minimal_react_agent/README.md)：无框架的极简 ReAct Agent。
- [`l1/guardrail_helpers`](l1/guardrail_helpers/README.md)：本地工具策略与确认边界。
- [`l1/multi_turn_state`](l1/multi_turn_state/README.md)：多轮上下文状态与摘要交接。

### L2

- [`l2/single_agent_mcp`](l2/single_agent_mcp/README.md)：带 MCP 风格工具边界与护栏的单 Agent。
- [`l2/cost_aware_router`](l2/cost_aware_router/README.md)：成本与延迟感知路由。
- [`l2/mcp_tool_selection`](l2/mcp_tool_selection/README.md)：确定性 MCP 工具选择与校验。

### L3

- [`l3/rag_memory_observability`](l3/rag_memory_observability/README.md)：RAG、记忆与可观测性骨架。
- [`l3/rag_hybrid_search`](l3/rag_hybrid_search/README.md)：确定性关键词+向量混合检索。
- [`l3/rag_evaluator`](l3/rag_evaluator/README.md)：确定性检索评估。
- [`l3/multi_round_research_discussion`](l3/multi_round_research_discussion/README.md)：多轮证据规划与讨论收敛。
- [`l3/multi_agent_supervisor`](l3/multi_agent_supervisor/README.md)：确定性多 Agent 路由。

### L4

- [`l4/production_postmortem`](l4/production_postmortem/README.md)：可执行的生产复盘结构、覆盖检查与行动项闭环。
- [`l4/regression_gate`](l4/regression_gate/README.md)：安全、trace、回滚与成本的发布门禁。
- [`l4/cost_and_stability_guardrails`](l4/cost_and_stability_guardrails/README.md)：运行时成本、延迟、重试与降级护栏。
- [`l4/production_trace_integrity`](l4/production_trace_integrity/README.md)：面向生产可观测性的确定性 trace 完整性校验。
- [`l4/deployment_hygiene`](l4/deployment_hygiene/README.md)：结合可观测性、成本与发布门禁的部署决策。

### L5

- [`l5/custom_pattern_lab`](l5/custom_pattern_lab/README.md)：带安全与验证的可复用自定义模式。
- [`l5/pattern_catalog`](l5/pattern_catalog/README.md)：带就绪检查的可复用模式目录。
- [`l5/multilingual_pattern_lab`](l5/multilingual_pattern_lab/README.md)：同一模式翻译为 Python、Node.js、Rust、Go 与 TypeScript。
- [`l5/pattern_eval_gate`](l5/pattern_eval_gate/README.md)：模式进入目录前的确定性门禁。
- [`l5/supervision_incident_response`](l5/supervision_incident_response/README.md)：多 Agent 集群的确定性生产监督与事件响应。
- [`l5/vibe_coding_spec`](l5/vibe_coding_spec/README.md)：Vibe Coding 规范先行工作流的确定性提示就绪检查。

## 运行全部测试

```bash
python -m unittest discover -s labs -p "test_*.py"
```

预期结果：

```text
Ran ... tests
OK
```

## Lab 标准

每个 Lab 都应包含：

- 含 Goal、Prerequisites、Run、Common Pitfalls 与 Self-Check 的 `README.md`。
- 一个可执行的 `agent_top_labs_*.py` 文件。
- 一个确定性 `test_*.py` 文件。
- 无需 API key。
- 相关时在 README 中提供版本锚点。
- 示例翻译超出 Python 时，提供多语言对齐说明：权威源、负责人、运行时/工具链版本、smoke 命令与对齐状态。
