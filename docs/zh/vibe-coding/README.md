---
title: Vibe Coding 指南
validated_date: 2026-09-18
i18n-key: vibe-coding-readme
last-synced: 2026-09-18
---

# Vibe Coding 指南

Vibe Coding（氛围式编程）是一种 AI 辅助工作流：开发者用自然语言表达意图，让模型生成初稿，然后通过快速反馈循环进行审查、运行和打磨。"vibe" 强调的是减少输入摩擦，而不是免除工程判断。

本版块是 Agent-Top 中使用 Vibe Coding 的参考：在保持确定性、证据和产品判断的前提下应用它。

## 从这里开始

- 概念：[什么是 Vibe Coding？](什么是VibeCoding.md)
- 方法：[规范先行工作流](规范先行工作流.md)
- 验证：[运行与校验](运行与校验.md)
- 护栏：[常见踩坑](常见踩坑.md)

## 与 Agent-Top 的映射

- L0-L2：用 vibe coding 探索框架 API 和小型单 Agent Lab，始终带上可运行的测试。
- L3-L4：把规范先行工作流用于系统设计、RAG、可观测性和生产门禁。
- L5：把每个 vibe-coded 产物当作携带 `validated_date` 和 `tested_against` 的证据包。
- Examples 与 Labs 保持确定性且无需 API key；vibe coding 改变的是写作方式，而不是验收标准。

## 一句话规则

如果你不能用一句话说清目标、接口和验收检查，那你还不是在提示——你还在探索。探索没有错，但那还不是 vibe coding，而是调研。
## 动手 Lab

- [`labs/l5/vibe_coding_spec`](../../../labs/l5/vibe_coding_spec/README.zh-CN.md)：一个把"一句话规则"编码为检查的确定性 Lab。运行：

```bash
python3 -m unittest labs.l5.vibe_coding_spec.test_lab
```

- 可打印规范表单：[`Vibe Coding 规范模板`](../../../templates/VibeCoding规范模板.md)（英文源：[`vibe-coding-spec-template.md`](../../../templates/vibe-coding-spec-template.md)）。
