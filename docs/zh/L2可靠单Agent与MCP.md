---
title: L2 带 MCP 的可靠单 Agent
validated_date: 2026-09-16
tested_against: "python 3.10+"
i18n-key: l2-single-agent-mcp
last-synced: 2026-09-16
---

# L2 带 MCP 的可靠单 Agent

## 目标

构建一个通过清晰 MCP 风格边界调用工具的可靠单 Agent。

## 前置

- 已完成 L0 和 L1
- 理解 guardrail 与工具校验
- 不需要 API key

## 核心思路

- Tool server 应暴露小型、类型清晰的操作。
- Agent 应在调用工具前校验输入。
- 工具结果应在成为最终答案前再次检查。
- Guardrail 应阻止空输入、过长输入或高风险请求。

## 为什么需要工具边界

工具边界是 Agent 请求另一个系统执行工作的地方。在 MCP 风格设计中，这个边界应该显式。

也就是说：

- 工具名已知；
- payload 结构已知；
- 非法输入要尽早拒绝；
- Agent 不能默认认为工具输出一定安全。

## Lab 结构

L2 Lab 有三个部分：

1. `ToolServer`
2. `Guardrail`
3. `run_single_agent()`

```python
class ToolServer:
    def list_tools(self) -> list[str]:
        return ["search_docs"]

    def call_tool(self, name: str, payload: dict[str, str]) -> str:
        if name != "search_docs":
            raise ValueError(f"Unknown tool: {name}")
        query = payload.get("query", "").strip()
        if not query:
            raise ValueError("query is required")
        return json.dumps({"hits": [f"synthetic result for {query}"]})

class Guardrail:
    def allow(self, query: str) -> bool:
        trimmed = query.strip()
        return bool(trimmed) and len(trimmed) <= 200

def run_single_agent(query: str) -> dict[str, object]:
    guardrail = Guardrail()
    if not guardrail.allow(query):
        return {"ok": False, "reason": "guardrail rejected query"}
    server = ToolServer()
    result = server.call_tool("search_docs", {"query": query.strip()})
    return {"ok": True, "result": result}
```

## 逐步操作

### 1. 运行合法查询

```bash
python - <<'PY'
from labs.l2.single_agent_mcp.agent_top_labs_l2_single_agent_mcp import run_single_agent
print(run_single_agent("agent memory"))
PY
```

预期输出：

```text
{'ok': True, 'result': '{"hits": ["synthetic result for agent memory"]}'}
```

### 2. 运行非法查询

```bash
python - <<'PY'
from labs.l2.single_agent_mcp.agent_top_labs_l2_single_agent_mcp import run_single_agent
print(run_single_agent("   "))
PY
```

预期输出：

```text
{'ok': False, 'reason': 'guardrail rejected query'}
```

### 3. 查看工具列表

```bash
python - <<'PY'
from labs.l2.single_agent_mcp.agent_top_labs_l2_single_agent_mcp import ToolServer
print(ToolServer().list_tools())
PY
```

预期输出：

```text
['search_docs']
```

### 4. 运行测试

```bash
python -m unittest labs.l2.single_agent_mcp.test_lab
```

预期结果：

```text
Ran 2 tests in 0.00Xs

OK
```

## 为什么 guardrail 要放在前面

在真实系统中，坏输入可能导致：

- 昂贵的模型调用；
- 错误的工具调用；
- 不安全的副作用；
- 难以排查的日志；
- 用户可见但原因不明的失败。

把 guardrail 放在工具调用前，会让拒绝变得便宜且可预测。

## MCP 改变了什么

真实的 MCP server 会通过协议层暴露工具。这个 Lab 不需要网络服务，但保留了同一个思想：

- `list_tools()` 描述可用工具；
- `call_tool()` 是入口；
- 在边界处做 payload 校验；
- Agent 收到结构化工具输出。

## 调试问题

当工具调用失败时，问这些问题：

- 工具名是否允许？
- payload 形状是否正确？
- guardrail 是否过早拒绝？
- 工具输出是否是合法 JSON？
- Agent 是否正确处理了工具结果？

## 常见错误

- 不校验输入就调用工具。
- 把工具输出直接当成最终事实。
- 让空输入或不安全请求到达工具边界。
- 把协议逻辑和业务逻辑混在一起。

## 自测

1. 为什么 guardrail 要先于工具调用执行？
2. 如果工具名未知会发生什么？
3. 为什么 `query.strip()` 在这里有用？
4. 工具边界能降低什么生产风险？
5. 如果要增加第二个工具，你会怎么扩展？

## 关联 Lab

阅读 Lab README：[`../../labs/l2/single_agent_mcp/README.md`../labs/l2/single_agent_mcp/README.md)。

运行 Lab 测试：

```bash
python -m unittest labs.l2.single_agent_mcp.test_lab
```

## 下一步

继续 [`L3 RAG、记忆与可观测`](L3RAG记忆与可观测.md)，组合检索、记忆和 trace。
