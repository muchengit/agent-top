---
i18n-key: interviews-questions-l2-framework-mcp
last-synced: 2026-09-16
validated_date: 2026-09-16
---

L2 框架和 MCP 题

## 1. 如何选 graph orchestration 还是 lightweight SDK？

答案要点：

- 复杂状态、循环、checkpoint、human review 用 graph。
- 小型线性流程用 SDK 或 plain loop。
- 选择能让 failure modes 明确的最简单方案。

## 2. 好的工具边界是什么？

答案要点：

- 一个工具只做一件事。
- 输入输出类型化。
- 副作用明确。
- 错误和空结果区分。
- 破坏性动作需 confirmation。

## 3. MCP server integration 失败怎么排查？

答案要点：

- server availability。
- transport。
- schema discovery。
- auth。
- first tool call logs。
- discovery、invocation、timeout、parsing 分层。

