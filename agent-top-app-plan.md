# Agent-Top App Plan

Updated: 2026-09-23

## 1. Goal

Turn Agent-Top from a documentation and ebook repository into a structured learning app for LLM Agent development.

The product should help users do three things:

1. Learn the Agent curriculum step by step.
2. Practice with executable labs and evidence-based exercises.
3. Prove progress with saved work, checks, and portfolio output.

## 2. Reference Apps

The best pattern is a mix of learning platforms, coding labs, and portfolio tools.

| Reference | What to copy | What to adapt |
| --- | --- | --- |
| Duolingo | Levels, streaks, quests, clear next step | Replace language lessons with L0-L5 Agent tracks |
| Codeacademy | Interactive walkthroughs and terminal-style practice | Keep content repo-driven and Markdown-first |
| DataCamp | Skills map and guided exercises | Map exercises to labs and examples |
| Coursera | Progress tracking and certificates | Make it lightweight and local-first first |
| Notion | Workspace for notes and templates | Make notes attach to lessons and labs |
| GitHub Learning Lab | Guided real-world tasks | Reuse evidence files and templates |
| Replit / ChatGPT Canvas | Inline practice and review | Add code review and submission checks |

## 3. Core Product Idea

Agent-Top App should feel like a guided Agent training workspace, not a plain docs site.

Each learning unit should have:

- a learning objective
- a prerequisite
- a practice task
- a self-check
- a saved evidence artifact
- a completion state

## 4. Information Architecture

### Primary navigation

1. Learn
2. Practice
3. Evidence
4. Portfolio
5. Search
6. Book

### Learn

- L0-L5 course path
- lesson list
- lesson progress
- bilingual content
- bookmarks

### Practice

- lab task center
- runnable exercise cards
- exercise instructions
- code snippets
- self-check questions

### Evidence

- trace files
- eval files
- JSONL evidence
- release gate files
- validation status

### Portfolio

- completed courses
- completed labs
- exported certificates
- public share links

## 5. User Journey

### Beginner path

1. Start from L0.
2. Read one lesson.
3. Run one lab.
4. Submit evidence.
5. Unlock the next level.

### Practitioner path

1. Jump to a topic, for example RAG or MCP.
2. Review the lesson.
3. Open the matching lab.
4. Save the trace or evaluation file.
5. Build a portfolio entry.

## 6. Feature Plan

### MVP 1: Learning Workspace

- course navigator
- lesson reader
- bilingual switching
- progress bar
- bookmarks
- search

### MVP 2: Lab Workspace

- lab cards
- exercise steps
- code blocks
- self-check questions
- file upload or paste area
- JSONL validation

### MVP 3: Evidence System

- trace viewer
- eval result viewer
- release gate viewer
- validation summary
- evidence export

### MVP 4: Portfolio Mode

- personal dashboard
- completion badges
- certificate export
- shareable summary
- history timeline

### MVP 5: Community Mode

- contributor tasks
- review tasks
- translation tasks
- discussion threads
- pattern contributions

## 7. Recommended Stack

### Frontend

- React + TypeScript
- Vite
- Tailwind CSS
- TanStack Query
- React Router
- Zustand for local state

### Content layer

- Markdown renderer
- JSONL parser
- JSON schema validator
- Markdown AST extractor for lessons and labs

### Backend

- FastAPI or Next.js API routes
- SQLite first, then Postgres
- local file storage or S3-compatible storage later

## 8. Data Model

### Course

- id
- level
- title
- language
- source_path
- summary
- prerequisites
- duration_minutes
- tags

### Lesson

- id
- course_id
- title
- source_path
- language
- summary
- prerequisites
- related_lab_id

### Lab

- id
- title
- level
- source_path
- objective
- steps
- self_check
- evidence_schema
- tested_against
- validated_date

### Submission

- user_id
- lab_id
- submitted_at
- content
- attachments
- trace_files
- validation_status
- score
- feedback

### Progress

- user_id
- course_id
- lesson_id
- lab_id
- status
- completed_at
- bookmarked
- last_read_at

## 9. Validation Ideas

Because Agent-Top already has evidence files, the app can be more useful than a normal course app.

Suggested checks:

- valid JSONL
- required fields present
- timestamps parseable
- trace IDs consistent
- model gateway evidence complete
- release gate decisions complete

## 10. Roadmap

### Phase 1

Build a static learning web app with docs, labs, examples, templates, search, and progress tracking.

### Phase 2

Add lab submissions and evidence validation.

### Phase 3

Add accounts, saved progress, and portfolio export.

### Phase 4

Add reviewable submissions and teacher-like feedback.

### Phase 5

Add community workflows, contributor tasks, and open-source contribution prompts.

## 11. Success Metrics

- lessons started
- lessons completed
- labs completed
- evidence submissions accepted
- time to first completed lab
- repeat visits
- completion rate by level

## 12. Recommended Next Step

Start with a web MVP that turns the existing Markdown content into a guided learning app, then add evidence validation once the navigation and content structure are solid.
