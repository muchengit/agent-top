---
title: L1 最小 ReAct Agent
validated_date: 2026-09-16
tested_against: "python 3.10+"
i18n-key: l1-minimal-react-agent
last-synced: 2026-09-16
---

# L1 最小 ReAct Agent

## 目标

不使用 Agent 框架，从零构建一个小型 ReAct 风格 Agent 循环。

## 前置

- 已完成 L0
- 熟悉 Python 函数、循环和简单控制流
- 不需要 API key

## 什么是 ReAct

ReAct 表示 Agent 在推理和行动之间交替。

一个最小循环如下：

1. 观察当前状态。
2. 思考下一步。
3. 需要时调用工具。
4. 观察工具输出。
5. 重复，直到 Agent 能回答或必须停止。

本教程故意使用简单的确定性 planner，而不是真实 LLM。目标是先理解控制流。

## 核心思想

一个 Agent 需要四个部分：

- **Goal**：用户想要什么。
- **Observation**：Agent 已经看到什么。
- **Tool**：返回更多信息的动作。
- **Stop condition**：安全结束循环的方式。

## 最小实现

Lab 代码的结构如下：

```python
from dataclasses import dataclass, field
from typing import Callable

Tool = Callable[[str], str]

@dataclass
class AgentRun:
    observations: list[str] = field(default_factory=list)
    steps: list[str] = field(default_factory=list)

def add_tool(expression: str) -> str:
    return "2+3=5"

def plan_next_action(goal: str, observations: list[str]) -> tuple[str, str] | None:
    if not observations:
        if goal.isdigit():
            return ("call_tool", "call_tool")
        return ("answer", f"I need a numeric goal, but got: {goal}")
    return ("answer", f"Result: {observations[-1]}")

def run_react_agent(goal: str, tools: dict[str, Tool], max_steps: int = 5) -> AgentRun:
    run = AgentRun()
    for _ in range(max_steps):
        action = plan_next_action(goal, run.observations)
        if action is None:
            run.steps.append("STOP: max_steps exceeded")
            return run
        action_type, action_value = action
        if action_type == "answer":
            run.steps.append(f"ANSWER: {action_value}")
            return run
        tool = tools.get(action_value)
        if tool is None:
            run.steps.append(f"STOP: missing tool {action_value}")
            return run
        observation = tool(goal)
        run.observations.append(observation)
        run.steps.append(f"OBSERVE: {observation}")
    run.steps.append("STOP: max_steps exceeded")
    return run
```

## 逐步操作

### 1. 直接运行 Lab

```bash
python -m labs.l1.minimal_react_agent.agent_top_labs_l1_minimal_react_agent
```

预期输出：

```text
OBSERVE: 2+3=5
ANSWER: Result: 2+3=5
```

### 2. 用一个数字目标运行循环

```bash
python - <<'PY'
from labs.l1.minimal_react_agent.agent_top_labs_l1_minimal_react_agent import run_react_agent, add_tool
result = run_react_agent("5", {"call_tool": add_tool})
print(result.steps)
print(result.observations)
PY
```

预期输出：

```text
['OBSERVE: 2+3=5', 'ANSWER: Result: 2+3=5']
['2+3=5']
```

过程是：

1. Agent 还没有 observation。
2. 因为 goal 是数字，它计划调用工具。
3. 它调用 `add_tool`。
4. 它观察到 `2+3=5`。
5. 它生成最终答案。

### 3. 用非数字目标运行

```bash
python - <<'PY'
from labs.l1.minimal_react_agent.agent_top_labs_l1_minimal_react_agent import run_react_agent, add_tool
result = run_react_agent("hello", {"call_tool": add_tool})
print(result.steps)
PY
```

预期输出：

```text
['ANSWER: I need a numeric goal, but got: hello']
```

这展示了 stop condition。当输入不适合工具时，Agent 不会无限循环。

### 4. 运行测试

```bash
python -m unittest labs.l1.minimal_react_agent.test_lab
```

预期结果：

```text
Ran 3 tests in 0.00Xs

OK
```

## 为什么需要 `max_steps`

如果没有 `max_steps`，Agent 可能无限循环，例如：

- 模型不断请求同一个工具；
- 工具输出格式错误；
- planner 永远无法识别 answer 状态；
- 工具不断返回同一个 observation。

最大步数是一个简单但重要的生产 guardrail。

## 真实 Agent 会加什么

真实 Agent 会用模型调用替换 `plan_next_action()`。但即使如此，你仍然需要：

- 结构化 tool call；
- 工具结果校验；
- stop condition；
- 错误处理；
- logging 或 trace；
- 成本和延迟限制。

## 调试问题

如果 Agent 行为异常，问这些问题：

- planner 是否选择了正确动作？
- tool 是否返回了 planner 预期的内容？
- Agent 是否观察到了工具输出？
- stop condition 是否触发？
- tool 是否不在 tool map 中？

## 常见错误

- 没有 stop condition。
- 不校验工具输出就把它当成可信事实。
- 把 observation、planning 和 execution 混成一个黑盒步骤。
- 忽略缺失工具。
- 让循环超过安全上限。

## 自测

1. 最小 Agent 的四个部分是什么？
2. 为什么需要 `max_steps`？
3. 当工具缺失时会发生什么？
4. 当工具输出格式错误时应该发生什么？
5. 如何把这个 fake planner 改成真实 model-backed planner？

## 关联 Lab

阅读 Lab README：[`../../labs/l1/minimal_react_agent/README.md`](../../labs/l1/minimal_react_agent/README.md)。

运行 Lab 测试：

```bash
python -m unittest labs.l1.minimal_react_agent.test_lab
```

## 下一步

继续 [`L2 带 MCP 的可靠单 Agent`](L2-带-MCP-的可靠单-Agent.md)，添加更清晰的工具边界。
