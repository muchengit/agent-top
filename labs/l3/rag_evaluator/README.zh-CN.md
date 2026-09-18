---
title: RAG 评估器 Lab
capability_level: L3
validated_date: 2026-09-19
i18n-key: l3-rag-evaluator
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L3 Lab：RAG 评估器

## Goal

练习用必需来源与拒答场景评估检索行为。

## Prerequisites

- L3 RAG、记忆与可观测性概念。
- Python 3.10+。

## Run

```bash
python -m unittest labs.l3.rag_evaluator.test_lab
```

## 本 Lab 教什么

- 检索必须对照必需来源检查。
- 缺失证据可以通过拒答处理。
- 评估用例需要显式的预期行为。

## 常见踩坑

- 把任何检索文本都当作成功。
- 忘记无答案用例。
- 混淆检索召回率与最终答案正确性。

## Self-Check

1. 为什么评估集应包含无答案用例？
2. 缺失来源与错误来源有什么区别？
3. 你会如何扩展它以衡量引用质量？
