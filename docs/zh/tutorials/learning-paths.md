---
i18n-key: tutorials-learning-paths
last-synced: 2026-09-16
validated_date: 2026-09-16
---

# 学习路径

学习路径连接 Agent-Top 的教程、Lab、案例、速查表和作品集证据。

## 入门路径：从第一次调用到单 Agent

1. 阅读 [`../l0-first-llm-call.md`](../l0-first-llm-call.md)。
2. 运行 [`../../../labs/l0/first_llm_call/README.md`](../../../labs/l0/first_llm_call/README.md)。
3. 阅读 [`../concepts/react-pattern.md`](../concepts/react-pattern.md)。
4. 运行 [`../../../labs/l1/minimal_react_agent/README.md`](../../../labs/l1/minimal_react_agent/README.md)。
5. 添加 stop conditions，并解释 tool-result ambiguity。

出口证据：

- 用一句话解释第一次 LLM 调用。
- 本地跑通一个 ReAct loop。
- 解释一个停止条件。

## 进阶路径：可靠单 Agent

1. 阅读 [`../l2-single-agent-mcp.md`](../l2-single-agent-mcp.md)。
2. 运行 [`../../../labs/l2/single_agent_mcp/README.md`](../../../labs/l2/single_agent_mcp/README.md)。
3. 运行 [`../../../labs/l1/guardrail_helpers/README.md`](../../../labs/l1/guardrail_helpers/README.md)。
4. 运行 [`../../../labs/l2/cost_aware_router/README.md`](../../../labs/l2/cost_aware_router/README.md)。
5. 写一个工具风险分类表。

出口证据：

- Tool allowlist。
- Destructive-action confirmation rule。
- 成本或延迟感知路由决策。

## 系统路径：RAG、记忆、多 Agent

1. 阅读 [`../l3-rag-memory-observability.md`](../l3-rag-memory-observability.md)。
2. 阅读 [`../concepts/multi-round-research-discussion.md`](../concepts/multi-round-research-discussion.md)。
3. 运行 [`../../../labs/l3/rag_evaluator/README.md`](../../../labs/l3/rag_evaluator/README.md)。
4. 运行 [`../../../labs/l3/multi_round_research_discussion/README.md`](../../../labs/l3/multi_round_research_discussion/README.md)。
5. 运行 [`../../../labs/l3/multi_agent_supervisor/README.md`](../../../labs/l3/multi_agent_supervisor/README.md)。

出口证据：

- required-source retrieval eval。
- missing evidence refusal case。
- 多 Agent 路由分配。

## 生产路径

1. 阅读 [`../l4-production.md`](../l4-production.md)。
2. 阅读 [`../production/evals-checklist.md`](../production/evals-checklist.md)。
3. 阅读 [`../production/safety-checklist.md`](../production/safety-checklist.md)。
4. 运行 [`../../../labs/l4/production_postmortem/README.md`](../../../labs/l4/production_postmortem/README.md)。
5. 运行 [`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md)。

出口证据：

- Release gate checklist。
- 带 owner 和 due date 的 incident postmortem。
- Rollback plan。

## 专家路径：原创模式

1. 阅读 [`../l5-custom-patterns.md`](../l5-custom-patterns.md)。
2. 阅读 [`../concepts/agent-system-architecture.md`](../concepts/agent-system-architecture.md)。
3. 运行 [`../../../labs/l5/custom_pattern_lab/README.md`](../../../labs/l5/custom_pattern_lab/README.md)。
4. 运行 [`../../../labs/l5/pattern_catalog/README.md`](../../../labs/l5/pattern_catalog/README.md)。
5. 起草一个带 safety 和 verification 的可复用 pattern。

出口证据：

- Pattern spec。
- Deterministic Lab。
- Failure-mode section。
- Reviewer-ready contribution notes。
