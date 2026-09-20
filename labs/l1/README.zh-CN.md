---
title: L1 Labs
capability_level: L1
validated_date: 2026-09-19
---

# L1 Labs

英文版：[`README.md`](README.md)

## 目标

理解并实现核心 Agent 组件：工具使用、护栏与多轮状态，且不依赖框架。

## 前置条件

- L0：首次 LLM 调用概念
- Python 3.10+
- 熟悉 ReAct 模式

## 本级别 Labs

- [`minimal_react_agent`](minimal_react_agent/README.md)：不依赖框架的极简 ReAct Agent。
- [`guardrail_helpers`](guardrail_helpers/README.md)：本地工具策略与确认边界。
- [`multi_turn_state`](multi_turn_state/README.md)：多轮上下文状态与摘要交接。

## 运行

```bash
python -m unittest discover -s labs/l1 -p "test_*.py"
```

## 常见踩坑

- 新增工具时跳过护栏。每个工具边界都需要策略。
- 未做摘要导致多轮之间丢失会话上下文。
- 在无框架 Lab 里混入框架概念；每个 Lab 应保持自包含。

## 自检

1. 极简 ReAct Agent 的核心组件有哪些？
2. 什么情况下工具调用需要确认边界？
3. 多轮状态如何保存与压缩？
