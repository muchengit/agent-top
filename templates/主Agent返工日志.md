---
title: 主 Agent 返工日志模板
validated_date: 2026-09-17
---

# 主 Agent 返工日志

当主 Agent 退回或拒绝员工工作时，使用这份日志。

## 决策摘要

- Date:
- Dispatch cycle:
- Employee ID:
- Employee name:
- Main agent decision: request changes | reject | escalate to maintainer
- Risk level: low | medium | high

## 退回原因

勾选适用项：

- [ ] 没有明确 expected files。
- [ ] 没有可测试 acceptance criteria。
- [ ] 第二员工无法复现结果。
- [ ] 文档、测试、示例不一致。
- [ ] 安全敏感操作缺确认或 rollback。
- [ ] 双语 metadata 或中文命名错误。
- [ ] 结论缺本地检查或公开证据。
- [ ] 工作增加 maintainer 负担但未减少歧义。
- [ ] 其他：

## 证据

- Relevant files:
- Commands run:
- Failed checks:
- Missing artifacts:
- Public/source evidence:

## 必改项

1. 
2. 
3. 

## 返工 SLA

- Expected rework owner:
- Backup owner:
- Due date:
- Main-agent follow-up date:

## 复审结果

- Re-review date:
- Decision: accept | request changes | reject | escalate
- Reason:
- Follow-up owner:
