# Agent-Top 贡献指南

感谢帮助完善 Agent-Top。本仓库偏好清晰、小而可审查的贡献。

## 贡献路径

- 撰写教程或 Lab
- 翻译内容
- 审校文档
- 维护示例
- 补充面试题
- 补充作品集项目路径、面试回答范例、设计模板或开源影响力指南

适合入门的标签：

- `good first issue`
- `docs-only`
- `translation-needed`
- `sync-required`

## 本地检查

提交 PR 前运行：

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

## 内容规范

每篇文章或 Lab 都应包含：

- 目标
- 前置要求与能力等级
- 步骤或运行命令
- 预期输出或验证方式
- 版本锚点（框架相关内容）
- 常见踩坑
- 自测问题

默认内容形态为 Markdown + 可执行 Lab。具体 Lab 的代码和测试应放在同一 Lab 目录，并在 README 中写明运行命令。

## 双语流程

- 英文默认作为主源，除非明确标注例外。
- 中文翻译位于 `docs/zh`，并保留相同 `i18n-key`。
- 翻译更新时同步 `last-synced` 元数据。
- 稳定术语以 glossary 为准。

## 审查规则

- 同一作者不应在同一模块同月兼任内容作者和审阅者。
- 架构和安全主题需要 Maintainer 审查。
- 普通 Lab 需要 Reviewer 审查。
- 翻译需要语言审校和内容源一致性检查。

## PR 说明

请包含：

- 改了什么。
- 为什么改。
- 运行了哪些检查。
- 是否影响翻译或框架版本。
- 是否需要后续跟进。
