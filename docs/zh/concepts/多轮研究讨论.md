---
i18n-key: concepts-multi-round-research-discussion
last-synced: 2026-09-16
validated_date: 2026-09-16
---

多轮研究与讨论流程

多轮研究表示 Agent 在回答前进行多轮证据收集。多轮讨论表示 Agent 可以澄清、质疑弱证据，并在足够时停止。

## 为什么需要多轮

单次回答在以下场景会失败：

- 问题模糊。
- 第一轮检索漏掉关键来源。
- 证据过期。
- 最终回答需要高风险动作。

## 参考流程

1. 澄清问题。
2. 用多个 query shape 搜索。
3. 排序和比较来源。
4. 决定回答、再搜、问用户或拒绝。
5. 解释最终证据边界。

## 核心概念

### Query 规划

把模糊请求转成多个证据检索 query。

### Source Selection

检查结果是否真正包含回答所需证据。

维度：relevance、freshness、trust、scope。

### Discussion Rounds

每一轮可以是：search more、ask user、refuse weak evidence、draft answer、verify answer、stop。

### Convergence

应停止时：

- required evidence present。
- answer within scope。
- stale/conflicting claims 被指出。
- next action clear。

## 本地 Lab

- 多轮研究 Lab：[`../../../labs/l3/multi_round_research_discussion/README.md`](../../../labs/l3/multi_round_research_discussion/README.md)

