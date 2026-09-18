---
title: L3 Lab：RAG 混合检索
capability_level: L3
validated_date: 2026-09-19
i18n-key: l3-rag-hybrid-search
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L3 Lab：RAG 混合检索

## Goal

实现确定性混合检索流水线：将 BM25 风格关键词打分与简单的字符重叠“向量”分数结合，再把两种信号融合成最终排序。

## Prerequisites

- L2：可靠的单 Agent 与 MCP
- Python 3.10+
- 基本熟悉 RAG 检索与排序

## Run

```bash
python -m unittest labs.l3.rag_hybrid_search.test_lab
```

## 要学什么

- 词汇检索（BM25 风格 TF-IDF）精确但会漏掉改写匹配。
- 字符/单词重叠分数可替代稠密嵌入，捕获近义词重叠。
- 加权求和与倒数排名融合（RRF）都能把信号合成一个稳定排序。
- 融合不是魔法：只有两种信号互补时才真正有帮助。

## 常见踩坑

- 期望融合对每个查询都能推翻强关键词匹配；融合是合并信号，不是替换信号。
- 忽略平局处理：确定性排序需要一个稳定的次级键（如文档 id）。
- 在必须离线运行、无 API key 的 Lab 中使用真实 embedding 提供商。

## Self-Check

1. 纯词汇检索何时会漏掉相关文档？
2. 加权求和融合与 RRF 有何不同？
3. 为什么融合排序在多次运行间保持确定性？
