---
title: 多语言模式 Lab
capability_level: L5
validated_date: 2026-09-19
i18n-key: l5-multilingual-pattern
last-synced: 2026-09-19
tested_against: "python 3.10+, node 20+, rust 1.58+, go 1.21+, typescript 7.0.2"
---

# L5 Lab：多语言模式

## Goal

把一个稳定的 L5 Agent 模式翻译为五种语言实现：Python、Node.js、Rust、Go 与 TypeScript。

## Prerequisites

- L5 自定义模式概念。
- 相关时本地具备一种语言运行时。

## Run

Python 始终通过仓库测试套件可用：

```bash
python -m unittest labs.l5.multilingual_pattern_lab.test_lab
```

安装 smoke 运行器使用的本地 TypeScript 编译器：

```bash
npm ci
```

跨语言 smoke 检查：

```bash
python scripts/smoke_multilingual_labs.py
```

预期当本地运行时与编译器可用时，smoke 分支覆盖 Python、Node.js、Rust、Go 与 TypeScript。

## 维护契约

对于每个非 Python Lab，在 Lab README 或 Lab 负责人的 PR 说明中维护以下字段：

- 权威源：规范的模式契约或上游 Lab。
- 负责人：负责对齐与过期修复的语言维护者。
- 工具链：校验所用的包管理器、编译器、运行时与编译标志。
- 验证：确切的本地命令与预期输出形态。
- 对齐：与 Python 行为可接受的差异及为什么是有意为之。

多语言 Lab 只有在纯语法移植时不算完成；只有维护者能从一个干净检出重跑检查并解释任何行为差异后才算完成。

## 本 Lab 教什么

- 语言语法不同；模式契约应保持稳定。
- 每个实现都必须展示 `clarify`、`execute` 与 `verify`。
- 当安全规则命中时，每个实现都必须在执行前停止。

## 常见踩坑

- 复制框架特定的 Agent 代码而不是可复用模式。
- 跨语言使用不同输出形态却不记录原因。
- 把 TypeScript 语法当作合法 Node.js 运行时代码放在 JS 文件中。

## Self-Check

1. 什么不变量必须在跨语言翻译后依然成立？
2. 为什么被拦截的安全检查应返回空 plan steps？
3. 你会如何在不改变契约的情况下把这个模式扩展到另一个 Lab？
