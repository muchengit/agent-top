---
title: L5 Labs
capability_level: L5
validated_date: 2026-09-19
---

# L5 Labs

英文版：[`README.md`](README.md)

## 目标

创造原创模式、可复用模式目录与多语言模式实现，并附安全与验证证据。

## 前置条件

- L4：已生产化的 Agent 系统
- Python 3.10+（多语言 Lab 另需 Node.js、Rust、Go 或 TypeScript）
- 熟悉模式优先设计与外部贡献

## 本级别 Labs

- [`custom_pattern_lab`](custom_pattern_lab/README.md)：带安全与验证的可复用自定义模式。
- [`pattern_catalog`](pattern_catalog/README.md)：带就绪检查的可复用模式目录。
- [`multilingual_pattern_lab`](multilingual_pattern_lab/README.md)：同一模式翻译为 Python、Node.js、Rust、Go 与 TypeScript。
- [`pattern_eval_gate`](pattern_eval_gate/README.md)：模式进入目录前的确定性门禁。
- [`supervision_incident_response`](supervision_incident_response/README.md)：多 Agent 集群的确定性生产监督与事件响应。
- [`vibe_coding_spec`](vibe_coding_spec/README.md)：Vibe Coding 规范先行工作流的确定性提示就绪检查。

## 运行

```bash
python -m unittest discover -s labs/l5 -p "test_*.py"
```

## 常见踩坑

- 声称原创模式却不提供安全与验证证据。
- 模式未通过就绪检查就加入目录。
- 让翻译实现与权威源语言发生漂移。

多语言 Lab 请按其 `README.md` 中各语言的 smoke 命令执行。

## 自检

1. 什么证据能证明自定义模式可复用且安全？
2. 模式何时可以进入目录？
3. 如何保持多语言实现对齐？
