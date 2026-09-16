---
title: 练习与 Lab 使用手册
validated_date: 2026-09-17
i18n-key: tutorials-practice-handbook
last-synced: 2026-09-17
---

# 练习与 Lab 使用手册

用这份手册把学习材料转成作品集证据。

## 两条练习路线

- **Examples**：本地、虚构、无需 API key 的练习，见 [`../../../examples/README.md`](../../../examples/README.md)。
- **Labs**：确定性可运行测试，见 [`../../../labs/README.md`](../../../labs/README.md)。

## 使用方法

1. 从 [`学习路径.md`](学习路径.md) 选择一个能力层。
2. 如果要有可运行证据，跑对应 Lab。
3. 如果要有设计证据，完成对应 Example。
4. 写一份简短产物：decision log、design note、review result 或 postmortem。
5. 用三句话解释 trade-off。

## 推荐搭配

| Level | Example | Lab |
| --- | --- | --- |
| L1 | Agent decision trace | [`../../../labs/l1/minimal_react_agent/README.md`](../../../labs/l1/minimal_react_agent/README.md) |
| L2 | Agent decision trace | [`../../../labs/l2/single_agent_mcp/README.md`](../../../labs/l2/single_agent_mcp/README.md) |
| L3 | RAG evidence refusal | [`../../../labs/l3/rag_evaluator/README.md`](../../../labs/l3/rag_evaluator/README.md) |
| L4 | Agent decision trace + design review | [`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md) |
| L5 | 任意 exercise + pattern writeup | [`../../../labs/l5/custom_pattern_lab/README.md`](../../../labs/l5/custom_pattern_lab/README.md) |

## 证据格式

每个练习产物都保留：

- Task。
- Decision 或 output。
- Evidence link。
- Trade-off。
- Follow-up。

## 自评

当你能做到下面这些，就可以进入下一层：

- 说出 failure mode。
- 指出 evidence source。
- 解释 tool action 为什么 allow 或 block。
- 说明如何再次测试这个决策。
- 说明 source stale 时什么会变。
