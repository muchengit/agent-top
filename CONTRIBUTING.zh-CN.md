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

## 质量门槛

每次提交 PR 前必须通过以下检查：

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

文档改动需保持 en/zh 双语文档同步：`docs/zh` 下的中文翻译应与英文源保留相同 `i18n-key`，源文档变更时同步更新 `last-synced` 元数据。如果 PR 更新了英文文档，应在同一 PR 内更新或标注对应的中文镜像，避免双语内容失步。

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

提交 PR 前使用 [`templates/contribution-checklist.md`](templates/contribution-checklist.md)。

请包含：

- 改了什么。
- 为什么改。
- 运行了哪些检查。
- 是否影响翻译或框架版本。
- 是否需要后续跟进。
