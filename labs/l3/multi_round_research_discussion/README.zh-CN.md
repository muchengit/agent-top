---
title: 多轮研究讨论 Lab
capability_level: L3
validated_date: 2026-09-19
i18n-key: l3-multi-round-research-discussion
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L3 Lab：多轮研究讨论

## Goal

练习多轮研究与讨论工作流：规划搜索、选择证据、请求澄清，并决定何时作答。

## Prerequisites

- L3 RAG、记忆与可观测性概念。
- Python 3.10+。

## Run

```bash
python -m unittest labs.l3.multi_round_research_discussion.test_lab
```

## 工作流

1. 当用户请求含糊时澄清问题。
2. 按相关性、新鲜度与可信度搜索并排序候选来源。
3. 只选择含证据的来源。
4. 当证据过时或缺失时，询问用户或重新搜索。
5. 仅在证据充分时作答。

## 本 Lab 教什么

- 讨论不只是多次 LLM 调用；它是证据管理。
- 新鲜度与可信度是来源排序的一部分。
- 拒答与澄清都是有效结果。

## 常见踩坑

- 把第一个检索结果当作充分证据。
- 在澄清含糊问题之前就作答。
- 忽略过时证据。
- 混淆检索置信度与答案正确性。

## Self-Check

1. 为什么新鲜度应影响来源优先级？
2. 系统何时应向用户请求澄清？
3. 你会如何为这个 Lab 添加引用质量？
