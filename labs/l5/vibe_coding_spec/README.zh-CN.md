---
title: Vibe Coding 规范 Lab
capability_level: L5
validated_date: 2026-09-18
i18n-key: l5-vibe-coding-spec
last-synced: 2026-09-18
tested_against: "python 3.10+"
---

# L5 Lab: Vibe Coding 规范

## 目标

练习把一个模糊想法变成可提示的规范。本 Lab 把 Vibe Coding 的一句话规则编码为确定性检查：只有当目标、接口和验收都存在时，规范才算就绪。

## 前置要求

- 阅读 [Vibe Coding 指南](../../../docs/zh/vibe-coding/README.md)。
- Python 3.10+。

## 模板

使用可打印的表单：[`Vibe Coding 规范模板`](../../../templates/VibeCoding规范模板.md)（英文源：[`vibe-coding-spec-template.md`](../../../templates/vibe-coding-spec-template.md)）。

## 运行

```bash
python3 -m unittest labs.l5.vibe_coding_spec.test_lab
```

预期输出：

```text
Ran 12 tests
OK
```

## 本 Lab 教什么

- 可提示的规范需要目标、接口和验收。
- 模糊或空字段会失败关闭，而不是生成"看起来合理"的提示。
- 验收字段应包含一个评审者可以重跑的命令。

## 常见踩坑

- 把主题句当成目标：目标要说明变更后必须成立的事实。
- 忘记验收命令："应该能跑"不是检查。
- 绿灯后扩大范围：停在最小的通过变更。

## 自测

1. 你能用一句话复述目标、接口和验收吗？
2. 你的验收包含评审者可以运行的命令吗？
3. 字段为空时你会怎么做——直接提示，还是先调研？
