---
i18n-key: community-contributor-onboarding
last-synced: 2026-09-16
validated_date: 2026-09-16
---

新人贡献引导

欢迎参与 Agent-Top。这个指南帮助你做出维护者能快速审查的第一次贡献。

## 第一步

1. 读 README 和中文文档索引。
2. 选择一个标签：`good first issue`、`docs-only`、`translation-needed`。
3. 修改前后运行本地检查。
4. 保持改动小。
5. 解释改了什么以及为什么。

## 本地检查

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

## PR 前检查

- 相对链接是否有效？
- 内容变化是否更新 `validated_date`？
- Lab 是否有 `tested_against`？
- 双语文件是否保持 `i18n-key`？

