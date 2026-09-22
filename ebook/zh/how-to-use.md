# 如何使用这本书

Agent-Top 按 L0-L5 能力模型组织。如果你从零开始，建议按顺序阅读；如果你已有背景，可以直接跳到对应层级。

每个章节都遵循从概念到实践的路径：

1. 阅读章节。
2. 查看相关 Lab 或 Example。
3. 运行最小相关检查。
4. 记录证据后再进入下一步。

## 本地检查

在仓库根目录运行：

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

## 证据原则

笔记应聚焦输入、决策、输出和检查。简短的证据链比冗长复盘更实用。
