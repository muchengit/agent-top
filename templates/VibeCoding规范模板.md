---
title: Vibe Coding 规范模板
i18n-key: vibe-coding-spec-template
last-synced: 2026-09-18
validated_date: 2026-09-18
---

# Vibe Coding 规范

写提示之前先填这份模板。如果某个字段是空的，说明你还在探索——先调研。

## 目标

变更后必须成立的事实是什么？用一句话说清楚。

## 范围

- 范围内：
- 范围外：

## 接口

- 输入：
- 输出：
- 错误行为：

## 验收

必须通过的精确检查——评审者会跑的同一命令：

```bash
# 例如 python3 -m unittest labs.lX.lab_name.test_lab
```

## 约束

绝不能破坏什么：

## 打磨记录

贴出真实错误和失败输入，而不是"它不工作"。

- 第 1 轮失败：
- 第 1 轮修复：
- 第 2 轮失败：
- 第 2 轮修复：

## 审查记录

- diff 审查人：
- 无关变更是否回退：
- 保留的证据（测试 / trace / eval）：
