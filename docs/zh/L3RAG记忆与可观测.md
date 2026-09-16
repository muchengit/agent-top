---
title: L3 RAG、记忆与可观测
validated_date: 2026-09-16
tested_against: "python 3.10+"
i18n-key: l3-rag-memory-observability
last-synced: 2026-09-16
---

# L3 RAG、记忆与可观测

## 目标

把 RAG、记忆、生成和可观测组合成可追踪骨架。

## 前置

- 已完成 L0 到 L2
- 理解检索与上下文组装
- 不需要 API key

## 核心数据流

1. 用户 query 进入。
2. RAG 检索限定范围上下文。
3. 记忆 补充长期上下文。
4. Agent 规划并调用工具。
5. Observability 记录 prompt、检索、工具调用、延迟和成本。

## 为什么重要

生产 Agent 的失败往往不是抽象地说“模型错了”，而通常是很具体的问题：

- 检索没有命中正确文档；
- memory 注入了过期上下文；
- 日志不足以调试；
- 最终答案没有展示使用了哪些证据。

这个 Lab 就是这类系统的可追踪骨架。

## Lab 结构

```python
@dataclass
class Trace:
    event: str
    data: dict[str, str]

class In记忆Store:
    def __init__(self, documents: list[str]) -> None:
        self.documents = documents

    def retrieve(self, query: str, top_k: int = 2) -> list[str]:
        return [doc for doc in self.documents if query.lower() in doc.lower()][:top_k]

class Session记忆:
    def __init__(self) -> None:
        self.turns: list[str] = []

    def remember(self, message: str) -> None:
        self.turns.append(message)

    def recent(self, limit: int = 3) -> list[str]:
        return self.turns[-limit:]

def answer_with_trace(
    query: str,
    store: In记忆Store,
    memory: Session记忆,
) -> tuple[str, list[Trace]]:
    memory.remember(query)
    retrieved = store.retrieve(query)
    traces = [
        Trace("retrieve", {"query": query, "hits": str(len(retrieved))}),
        Trace("memory", {"recent_turns": str(len(memory.recent()))}),
    ]
    answer = " | ".join(retrieved) if retrieved else "No retrieved context."
    return answer, traces
```

## 逐步操作

### 1. 建立一个小文档集

```bash
python - <<'PY'
from labs.l3.rag_memory_observability.agent_top_labs_l3_rag_memory_observability import In记忆Store, Session记忆, answer_with_trace
store = In记忆Store(["RAG retrieves context", "MCP exposes tools", "记忆 persists turns"])
memory = Session记忆()
answer, traces = answer_with_trace("RAG", store, memory)
print(answer)
for trace in traces:
    print(trace.event, trace.data)
PY
```

预期输出：

```text
RAG retrieves context
retrieve {'query': 'RAG', 'hits': '1'}
memory {'recent_turns': '1'}
```

### 2. 增加第二轮对话

```bash
python - <<'PY'
from labs.l3.rag_memory_observability.agent_top_labs_l3_rag_memory_observability import In记忆Store, Session记忆, answer_with_trace
store = In记忆Store(["RAG retrieves context", "MCP exposes tools", "记忆 persists turns"])
memory = Session记忆()
answer_with_trace("RAG", store, memory)
_, traces = answer_with_trace("MCP", store, memory)
print(traces[1].data)
PY
```

预期输出：

```text
{'recent_turns': '2'}
```

### 3. 运行测试

```bash
python -m unittest labs.l3.rag_memory_observability.test_lab
```

预期结果：

```text
Ran 1 test in 0.00Xs

OK
```

## 各部分作用

- `In记忆Store` 是一个小检索层。
- `Session记忆` 是一个小会话层。
- `answer_with_trace()` 把两者连接起来并生成 trace。
- `Trace` 是调试视图，记录发生了什么。

## 为什么 trace 重要

Trace 给你一条按时间顺序的记录。

在生产中通常会包括：

- prompt id；
- retrieved document ids；
- memory keys used；
- tool call id；
- latency；
- token usage；
- cost；
- success or failure reason。

这样你可以回答：

- 是否检索到了正确上下文？
- memory 是否引入了过期数据？
- 哪一步耗时最长？
- 哪种失败模式反复出现？

## 常见错误

- 检索过多上下文。
- 把会话 memory 和长期 user memory 混在一起。
- 输出答案但不记录使用了哪些上下文。
- 默认认为 memory 永远正确。
- 忘记记录工具调用边界。

## 自测

1. 检索和记忆有什么区别？
2. 为什么 trace 应该包含 retrieved hits？
3. 检索范围过宽有什么风险？
4. 为什么 trace 中的 `recent_turns` 有用？
5. 进入生产前你还会增加什么？

## 关联 Lab

阅读 Lab README：[`../../labs/l3/rag_memory_observability/README.md`../labs/l3/rag_memory_observability/README.md)。

运行 Lab 测试：

```bash
python -m unittest labs.l3.rag_memory_observability.test_lab
```

## 下一步

继续 [`L4 Production`](L4生产化.md)，进入 evals、guardrails、rollback 和 postmortem。
