---
title: L3 Lab: RAG Hybrid Search
capability_level: L3
validated_date: 2026-09-18
tested_against: "python 3.10+"
---

# L3 Lab: RAG Hybrid Search

## Goal

Implement a deterministic hybrid retrieval pipeline that combines BM25-style keyword scoring with a simple character-overlap "vector" score, then fuses both signals into a final ranking.

## Prerequisites

- L2: reliable single Agent and MCP
- Python 3.10+
- Basic familiarity with RAG retrieval and ranking

## Run

```bash
python -m unittest labs.l3.rag_hybrid_search.test_lab
```

## What to Learn

- Lexical retrieval (BM25-style TF-IDF) is precise but misses paraphrase matches.
- Character/word overlap scores stand in for dense embeddings and capture near-synonym overlap.
- Weighted-sum and reciprocal-rank fusion (RRF) both combine signals into one stable ranking.
- Fusion is not magic: it only helps when the two signals are complementary.

## Common Pitfalls

- Expecting fusion to overturn a strong keyword match for every query; fusion merges signals, it does not replace them.
- Ignoring tie-breaking: deterministic result ordering requires a stable secondary key such as document id.
- Using a real embedding provider in a lab that must run offline without API keys.

## Self-Check

1. When does lexical-only retrieval miss a relevant document?
2. How does weighted-sum fusion differ from RRF?
3. Why does the fused ranking stay deterministic across runs?
