---
title: 多 Agent 监督者 Lab
capability_level: L3
validated_date: 2026-09-19
i18n-key: l3-multi-agent-supervisor
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L3 Lab：多 Agent 监督者

## Goal

练习从确定性任务画像为专用 Agent 分配工作。

## Prerequisites

- L3 多 Agent 流程概念。
- Python 3.10+。

## Run

```bash
python -m unittest labs.l3.multi_agent_supervisor.test_lab
```

## 本 Lab 教什么

- 监督者应选择最小有用的 Agent 集合。
- 人工确认是高风险工具工作的一条 Agent 路由。
- 验证可以是独立的 Agent 职责。

## 常见踩坑

- 创建超出需要的 Agent。
- 让工具 Agent 自己决定安全边界。
- 对证据密集任务忘记验证者。

## Self-Check

1. 什么时候单 Agent 优于监督者设置？
2. 为什么确认应在工具调用前路由？
3. 你会如何为这个监督者添加重试循环？
