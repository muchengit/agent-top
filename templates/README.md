---
title: Templates Index
validated_date: 2026-09-18
---

# Templates

Templates define the standard structure for Agent-Top contributions. This index covers all 34 template files in `templates/` (35 files including this `README.md`, which is only the index).

## Templates

### Bilingual Pairs (12 pairs / 24 files)

Each pair contains an English source and its Chinese mirror of the same artefact; both sides must stay in sync.

- **Design review workshop** — [`design-review-workshop-template.md`](design-review-workshop-template.md) (EN) ↔ [`Agent设计审查Workshop模板.md`](Agent设计审查Workshop模板.md) (CN)
- **Design review example** — [`design-review-example.md`](design-review-example.md) (EN) ↔ [`Agent设计审查范例.md`](Agent设计审查范例.md) (CN)
- **Case study template** — [`case-study-template.md`](case-study-template.md) (EN) ↔ [`案例研究模板.md`](案例研究模板.md) (CN)
- **Case study writing guide** — [`case-study-writing-guide.md`](case-study-writing-guide.md) (EN) ↔ [`案例研究写作指南.md`](案例研究写作指南.md) (CN)
- **Paper reading session** — [`paper-reading-session-template.md`](paper-reading-session-template.md) (EN) ↔ [`paper-reading-session-template.zh-CN.md`](paper-reading-session-template.zh-CN.md) (CN)
- **Technical talk outline** — [`technical-talk-outline-template.md`](technical-talk-outline-template.md) (EN) ↔ [`technical-talk-outline-template.zh-CN.md`](technical-talk-outline-template.zh-CN.md) (CN)
- **Employee work charter** — [`employee-work-charter.md`](employee-work-charter.md) (EN) ↔ [`员工工作章程.md`](员工工作章程.md) (CN)
- **Main agent rework log** — [`main-agent-rework-log.md`](main-agent-rework-log.md) (EN) ↔ [`主Agent返工日志.md`](主Agent返工日志.md) (CN)
- **L5 expert evidence** — [`l5-expert-evidence-template.md`](l5-expert-evidence-template.md) (EN) ↔ [`L5专家证据模板.md`](L5专家证据模板.md) (CN)
- **Observability trace** — [`observability-trace-template.md`](observability-trace-template.md) (EN) ↔ [`可观测性Trace模板.md`](可观测性Trace模板.md) (CN)
- **Eval and trace replay** — [`eval-trace-replay-template.md`](eval-trace-replay-template.md) (EN) ↔ [`可回放Eval和Trace模板.md`](可回放Eval和Trace模板.md) (CN)
- **Agent skill card** — [`agent-skill-card-template.md`](agent-skill-card-template.md) (EN) ↔ [`Agent技能卡模板.md`](Agent技能卡模板.md) (CN)

### English-Only Templates (9 files)

Single-language templates with no Chinese mirror yet; localized versions should be added as a new pair per the sync rules below.

- [`article-template.md`](article-template.md)
- [`lab-template.md`](lab-template.md)
- [`interview-question-template.md`](interview-question-template.md)
- [`postmortem-template.md`](postmortem-template.md)
- [`eval-report-template.md`](eval-report-template.md)
- [`agent-design-template.md`](agent-design-template.md)
- [`project-dispatch-plan.md`](project-dispatch-plan.md)
- [`community-lab-template.md`](community-lab-template.md)
- [`monthly-contributor-report.md`](monthly-contributor-report.md)

### English-Only Guide (1 file)

- [`contribution-checklist.md`](contribution-checklist.md) — pre-PR verification checklist (no Chinese mirror yet).

## When to Use Each

- **Article**: new concepts, tutorials, or framework explanations.
- **Lab**: runnable code with deterministic tests.
- **Interview question**: concept, implementation, debugging, or design question.
- **Postmortem**: production or learning incident with action items.
- **Eval report**: measured evaluation results for a change with pass/fail evidence.
- **Agent design**: reusable one-page design review and interview artifact.
- **Design review workshop**: structured group review notes with decision record (EN/CN pair).
- **Design review example**: completed review output for customer refund assistant (EN/CN pair).
- **Case study**: scenario-backed pattern lesson with failure modes and evidence (EN/CN pair).
- **Case study writing guide**: how to write a strong case study (EN/CN pair).
- **Paper reading session**: research digest with claim, reproduction notes, Lab connection, questions, and follow-up (EN/CN pair).
- **Technical talk outline**: reusable talk plan with audience, demo, trade-offs, Q&A risks, and follow-up owner (EN/CN pair).
- **Agent skill card**: compact skill definition for the L0–L5 learning path (EN/CN pair).
- **Employee work charter**: mandatory per-employee objective, expected output, acceptance criteria, rework rules, and main-agent review fields (EN/CN pair).
- **Main agent rework log**: rejection reason, evidence, required fixes, rework SLA, and re-review outcome (EN/CN pair).
- **Project dispatch plan**: main-agent dispatch queue with employee assignments, expected files, gates, and merge decision.
- **Contribution checklist**: pre-PR verification for docs, Labs, Examples, translation, and safety.
- **L5 expert evidence**: packaged expert-level evidence for pattern quality, governance, influence, rubric scores, and final decision (EN/CN pair).
- **Eval and trace replay**: replay commands, expected stdout, required artifacts, and exit criteria for eval/trace evidence (EN/CN pair).
- **Observability trace**: request, evidence, tool calls, guardrails, memory, runtime cost, and incident follow-up for replayable Agent behavior (EN/CN pair).
- **Community Lab**: group session notes and follow-up artifacts.
- **Monthly contributor report**: contribution review and recognition.

## Usage and Bilingual Sync

- Choose the file matching the contribution type and audience: English readers use the English source; Chinese readers use the CN mirror. For pairs, the English file is the canonical source.
- Bilingual templates are mirrors of one artefact, not independent templates. Structural changes must be applied to both sides in the same change, and both sides validated before the PR.
- When adding a new template, ship it as a pair (English source + Chinese mirror) following the existing naming convention: English file name, plus either a `.zh-CN.md` suffix or a fully localized Chinese file name.
- Language pairing is determined by file name and content; most templates carry no frontmatter `i18n-key`, so do not rely on frontmatter to identify mirrors.

## Review Checklist

- Is the goal clear?
- Are prerequisites listed?
- Is there a runnable command or expected output where relevant?
- Are failure modes documented?
- Does the artifact have owner, due date, or follow-up if applicable?
