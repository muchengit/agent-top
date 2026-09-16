---
title: MCP 模型上下文协议
validated_date: 2026-09-16
i18n-key: concepts-mcp
last-synced: 2026-09-16
---

# MCP 模型上下文协议

MCP，即 Model Context Protocol，是一种让 LLM 应用连接外部 server 的标准方式。这些 server 可以暴露 tools、resources、prompts、schemas 和外部 context。

## MCP 解决什么问题？

在 MCP 风格边界出现前，每个应用常常要自己重新接工具：schema、auth、logging、retry、error handling 和 UI prompt 都散落在本地实现里，且互不一致。MCP 给这类集成一个共享形状。

它帮助团队回答：

- 有哪些 tools 或 resources 可用？
- 每个 tool 接受什么 input schema？
- 谁能调用这个 tool？
- 返回了什么 evidence 或 error？
- 如何审计和调试这次调用？

## 核心角色

| 角色 | 作用 | 例子 |
| --- | --- | --- |
| MCP Host | 包含 Agent 的 app 或 runtime | Chat app、IDE assistant、workflow runner |
| MCP Client | 把 host 连接到一个或多个 server | In-process client、stdio client |
| MCP Server | 向 client 暴露能力 | Search server、file server、database server |
| Tool | server 可以执行的动作 | `search_docs`、`create_ticket`、`read_file` |
| Resource | 可读数据源 | 文件、URL、表格、workspace file |
| Prompt | 可复用 prompt 模板 | `summarize_issue`、`review_pr` |

```mermaid
flowchart QR
  Host[MCP Host / Agent App] --> Client[MCP Client]
  Client --> Server[MCP Server]
  Server --> Tools[Tools]
  Server --> Resources[Resources]
  Server --> Prompts[Prompts]
  Server --> Systems[External Systems]
```

## MCP 和 Function Calling 的区别

Function calling 是模型能力：模型提出一个 tool call，包含工具名和 JSON 参数。

MCP 是围绕这个能力建立的系统边界。

| 层 | 问题 | 例子 |
| --- | --- | --- |
| Function calling | 模型应该请求哪个 tool？ | `search_docs({"query": "refund"})` |
| Schema validation | 参数是否合法？ | `query` 必须是非空字符串 |
| MCP server | 暴露了哪些能力？ | tools、resources、prompts、metadata |
| Tool gateway | 调用是否授权和审计？ | actor、tenant、permissions、logs |
| Agent runtime | 结果如何影响下一步？ | answer、retry、clarify、escalate |

MCP 不替代模型、Agent loop 或生产 guardrails。它让工具和 context 集成更容易检查。

## MCP 不是什么？

MCP 不是：

- 自动授权系统；
- 安全策略；
- 记忆系统；
- RAG engine；
- 框架；
- “工具结果一定为真”的保证。

Permissions、audit、retry policy、rollback、rate limits 和 data retention 仍然需要显式设计。

## Agent-Top 如何使用 MCP 思想？

Agent-Top 在 Labs 中使用 MCP-style ideas，但不要求真实 server：

- `list_tools()` 暴露可用能力。
- `call_tool()` 强制 tool name 和 payload 边界。
- Guardrails 在 side-effecting tools 前运行。
- Tool output 被视为 evidence，而不是最终真理。

阅读 L2 教程：[`../L2可靠单Agent与MCP.md`](../L2可靠单Agent与MCP.md)。

## 调试清单

当 MCP-style integration 失败时：

1. Server 是否可达？
2. Tool name 是否存在？
3. Payload 是否符合 schema？
4. Actor 是否有权限？
5. External system 是否返回 error？
6. Agent 是否正确解释结果？
7. Trace 是否完整到可以复现调用？

## 相关链接

- Tool/MCP 安全技能卡：[`../skills/工具MCP安全技能卡.md`](../skills/工具MCP安全技能卡.md)
- Lab：[`../../../labs/l2/single_agent_mcp/README.md`](../../../labs/l2/single_agent_mcp/README.md)
