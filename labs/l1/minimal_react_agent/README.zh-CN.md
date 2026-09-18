---
title: 极简 ReAct Agent
capability_level: L1
validated_date: 2026-09-19
i18n-key: l1-minimal-react-agent
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L1 Lab：极简 ReAct Agent

## Goal

用第一性原理构建一个极小的 ReAct 风格 Agent，不依赖任何框架。

## Run

```bash
python -m unittest labs.l1.minimal_react_agent.test_lab
```

## 要学什么

- 感知（Perception）是当前的观察结果。
- 规划（Planning）选择下一个动作。
- 工具调用产生观察。
- 停止条件防止无限循环。

## Prerequisites

- 完成 L0。
- 熟悉 Python 控制流与简单函数。

## 常见踩坑

- 让 Agent 在没有停止条件的情况下无限循环。
- 不经验证就把工具输出当作事实。
- 把感知、规划、执行混成一个不透明的步骤。

## Self-Check

1. 工具调用后 Agent 收到什么观察？
2. 为什么停止条件是必要的？
3. 如果工具输出格式错误会怎样？
