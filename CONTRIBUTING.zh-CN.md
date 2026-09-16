# 贡献指南

感谢帮助完善 Agent-Top。本仓库偏好清晰、小而可审查的贡献。

## 贡献路径

- 撰写教程或 Lab
- 翻译内容
- 审校文档
- 维护示例
- 补充面试题
- 补充作品集项目路径

## 本地检查

提交 PR 前运行：

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
```

## 内容规范

每篇文章或 Lab 都应包含：

- 目标
- 前置要求与能力等级
- 步骤
- 版本锚点（框架相关内容）
- 常见踩坑
- 自测问题

## 双语流程

- 英文默认作为主源。
- 中文翻译通过 `translation-needed` 认领。
- 翻译更新时同步 `last-synced` 元数据。
