---
title: L0 第一次 LLM 调用
validated_date: 2026-09-16
tested_against: "python 3.10+"
i18n-key: l0-first-llm-call
last-synced: 2026-09-16
---

# L0 第一次 LLM 调用

## 目标

跑通第一次 LLM 请求/响应循环，理解请求中的每个概念，并把概念连接到仓库中的可执行 Lab。

## 前置

- Python 3.10+
- 基础命令行使用能力
- 不需要 API key

## 你应该学会

- Prompt 是发给模型的指令。
- System prompt 定义助手角色和约束。
- Response 是模型生成的文本。
- Token 不等同于英文单词。
- Context window 是模型可处理输入的预算。

## 为什么本教程使用 Fake Model

L0 的目标是理解请求结构，而不是折腾 API 配置。本 Lab 使用确定性的 fake model，方便你在本地运行、查看结果，并且不需要凭证。

这个 fake model 故意非常简单：

```python
class FakeModel:
    def complete(self, system_prompt: str, prompt: str) -> str:
        if not prompt:
            return "No user prompt provided."
        return f"[{system_prompt}] I received {len(prompt.split())} prompt tokens: {prompt}"
```

这不是真实 LLM。它只是教学替身，用来保留同一个概念：你发送 system role 和 user prompt，然后收到生成文本。

## 一次模型请求包含什么

一次最小模型调用有三个概念：

1. **System prompt**：助手角色。
2. **User prompt**：用户当前请求。
3. **Response**：模型返回的文本。

在 Lab 中，它们由这个函数表示：

```python
def first_llm_call(
    system_prompt: str = "You are helpful.",
    prompt: str = "Explain agents simply.",
) -> str:
    model = FakeModel()
    return model.complete(system_prompt, prompt)
```

默认运行时，应看到：

```text
[You are helpful.] I received 3 prompt tokens: Explain agents simply.
```

## 逐步操作

### 1. 不需要额外安装

L0 Lab 只用 Python 标准库。

```bash
python --version
```

### 2. 直接运行 Lab

```bash
python -m labs.l0.first_llm_call.agent_top_labs_l0_first_llm_call
```

预期输出：

```text
[You are helpful.] I received 3 prompt tokens: Explain agents simply.
```

### 3. 修改 prompt

```bash
python - <<'PY'
from labs.l0.first_llm_call.agent_top_labs_l0_first_llm_call import first_llm_call
print(first_llm_call(prompt="hello world"))
PY
```

预期输出：

```text
[You are helpful.] I received 2 prompt tokens: hello world
```

### 4. 修改 system prompt

```bash
python - <<'PY'
from labs.l0.first_llm_call.agent_top_labs_l0_first_llm_call import first_llm_call
print(first_llm_call(system_prompt="You are concise.", prompt="hello"))
PY
```

预期输出：

```text
[You are concise.] I received 1 prompt tokens: hello
```

### 5. 测试空 prompt 的 guardrail

```bash
python - <<'PY'
from labs.l0.first_llm_call.agent_top_labs_l0_first_llm_call import first_llm_call
print(first_llm_call(prompt=""))
PY
```

预期输出：

```text
No user prompt provided.
```

## Token 是什么

本 Lab 用空格切分来近似 token：

```python
len(prompt.split())
```

真实模型的分词更复杂。英文单词可能被拆成更小的部分，标点可能成为独立 token，非英文语言的切分方式也不同。但核心概念一样：**token 是模型计数的单位，不是人类自然计数的单位。**

这很重要，因为：

- prompt 长度影响成本；
- prompt 长度影响延迟；
- prompt 长度影响内容是否能进入 context window；
- prompt 长度影响哪些上下文会被包含或丢弃。

## System Prompt 与 User Prompt

System prompt 是助手角色，定义行为边界。

User prompt 是当前指令，定义当前要做什么。

例如：

```text
System prompt: You are helpful.
User prompt: Explain agents simply.
```

修改 system prompt 会改变角色；修改 user prompt 会改变任务。

## Context Window

Context window 是一次请求中模型能考虑的全部文本。它包括：

- system prompt；
- user prompt；
- 检索到的文档；
- 工具返回结果；
- 仍保留在上下文中的 assistant 输出。

L0 Lab 没有模拟 context 限制，但生产系统需要它。上下文太长会增加成本、提高延迟，甚至让重要指令被淹没。

## 运行测试

```bash
python -m unittest labs.l0.first_llm_call.test_lab
```

预期结果：

```text
Ran 2 tests in 0.00Xs

OK
```

## 常见错误

- 把 token 数当成词数。
- 发送空 prompt 并期待模型自动理解意图。
- 假设每次 LLM 响应都是确定性的。
- 混淆 system prompt 和 user prompt。
- 忘记 context window 是所有请求文本共享的预算。

## 自测

1. System prompt 的作用是什么？
2. 为什么 `len(prompt.split())` 只是 token 数的近似值？
3. Lab 中空 prompt 会发生什么？
4. 生产应用中，空 prompt 应该发生什么？
5. 为什么 context window 大小会影响成本和延迟？

## 关联 Lab

运行完整可执行 Lab：

```bash
python -m unittest labs.l0.first_llm_call.test_lab
```

阅读 Lab README：[`../../labs/l0/first_llm_call/README.md`../labs/l0/first_llm_call/README.md)。

## 下一步

继续 [`L1 最小 ReAct Agent`](L1最小ReActAgent.md)，不使用框架构建一个小型 Agent 循环。
