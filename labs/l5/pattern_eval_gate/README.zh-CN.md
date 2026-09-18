---
title: L5 Lab：模式评估门禁
capability_level: L5
validated_date: 2026-09-19
i18n-key: l5-pattern-eval-gate
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L5 Lab：模式评估门禁

## Goal

构建一个确定性门禁，评估可复用 Agent 模式是否准备好进入目录：对可复现性、证据、安全、文档与所有权打分，再把每个模式聚合为 passed、needs-fix 或 rejected。

## Prerequisites

- L4：生产化 Agent 系统
- Python 3.10+
- 熟悉模式优先设计与发布门禁

## Run

```bash
python -m unittest labs.l5.pattern_eval_gate.test_lab
```

## 常见踩坑

- 把缺失复现步骤或未缓解的高风险项当作可修复；它们是阻塞性的，必须拒绝该模式。
- 即使没有未解决项，也跳过高风险模式的人工签核。
- 混淆“needs review”（需要人工关注）与“needs fix”（明确补救）或“rejected”（阻塞）。
- 忘记文档与所有权缺口是质量门，不是安全阻塞项。

## Self-Check

1. 哪些维度直接阻塞模式，哪些只要求修复？
2. 高风险模式什么时候通过而不是需要 review？
3. 你会如何添加第六个维度，如性能证据？
