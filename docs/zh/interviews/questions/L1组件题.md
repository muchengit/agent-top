---
i18n-key: interviews-questions-l1-components
last-synced: 2026-09-16
validated_date: 2026-09-16
---

L1 组件题

## 1. 解释 Agent 四个核心组件。

答案要点：

- 感知 把输入、工具、观察变成 context。
- 规划 决定下一步。
- Tool use 执行外部动作。
- 记忆 保存跨步或跨会话上下文。

面试官听：

- 组件边界清晰。
- 知道 failure 如何传播。

Follow-up：

- 工具反馈模糊时会坏在哪里？

## 2. 为什么 ReAct 要 max step limit？

答案要点：

- 防无限循环。
- 限制 latency/cost。
- 让失败可见可调试。

