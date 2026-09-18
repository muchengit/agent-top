---
title: Agent-Top Glossary
validated_date: 2026-09-18
i18n-key: community-glossary
last-synced: 2026-09-18
---

# Glossary

## Agent

A system that uses an LLM plus tools, memory, planning, and control loops to accomplish tasks.

## Context Window

The maximum amount of text a model can process in one request, measured in tokens.

## MCP

Model Context Protocol. A standard way for LLM applications to connect to MCP servers that expose tools, resources, prompts, schemas, and external context.

## ReAct

A pattern that interleaves reasoning and action steps until a task is complete.

## RAG

Retrieval-Augmented Generation. A pattern that retrieves relevant external information before generating an answer.

## Tool Use

A mechanism where an agent calls external functions or services to gather data, execute actions, or verify results.

## Eval Set

A curated set of prompts, expected outcomes, and scoring criteria used to measure agent quality.

## Postmortem

A structured review of a production incident focused on root cause and prevention.

## Contract

A documented input, output, failure mode, and verification agreement for an Agent or tool.

## Handoff

Passing task state, evidence, and next responsibility between agents or stages.

## Guardrail

A rule, check, or approval step that prevents unsafe or irreversible behavior.

## Verifier

A component or agent that checks evidence and recommendations before the final answer.

## Memory

Information retained across turns or sessions that informs an agent's behavior.

## Trace

A record of prompts, tool calls, decisions, and results for a single run or task.

## Rollback

A path that restores a system to a known safe state after a failure.

## Human-in-the-loop

A process in which high-risk steps require human approval or review.

## Fail Closed

Failing by stopping or denying rather than continuing on unsafe assumptions.

## Regression Gate

A release gate that blocks unsafe behavior from shipping.

## Blast Radius

The scope of data or systems affected by a failure.

## Contributor

A person who contributes docs, translations, labs, issues, or reviews.

## Maintainer

A person responsible for architecture, security, and reviewing sensitive release changes.

## Reviewer

A person responsible for reviewing regular docs, labs, and glossary consistency.

## Translation Needed

A label for a stable EN source whose ZH mirror still needs updating.

## Sync Required

A label for EN/ZH content drift or an expired last-synced date.

## Tested Against

The framework, SDK, or runtime version that an example was tested against.

## Validated Date

The date on which a doc or example was checked.

## Good First Issue

A small-scope, testable, independently reviewable entry-level issue.

## Hallucination

Model output that is plausible but factually incorrect or unsupported.

## Prompt

The input given to a model that specifies the task or desired response.

## Multi-Agent

A design where multiple agents collaborate or coordinate to complete a task.

## Supervisor

An agent or component that coordinates and oversees other agents.

## RAG Evaluation

The process of measuring the quality of a RAG system's retrieval and generation.
