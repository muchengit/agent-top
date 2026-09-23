# Agent-Top App Tech Implementation Plan

Updated: 2026-09-23

## 1. Goal

Build the first working learning app from the existing Agent-Top content without forcing a premature backend.

The implementation should reuse the current repository structure as the source of truth and add a thin app layer on top.

## 2. Product Goal for v0.1

Deliver a local-first web app that can:

- browse L0-L5 content
- switch between English and Chinese
- open lessons and labs
- search repository content
- persist progress locally
- store simple submission drafts locally
- export a personal progress summary

## 3. Design Principles

- Start with a static app shell, not a full backend.
- Use repository Markdown and JSONL as the content source.
- Keep the app local-first by default.
- Add backend only when user accounts, submissions, or sync are required.
- Reuse the current content quality checks before expanding scope.

## 4. Recommended Stack

### Frontend

- React + TypeScript
- Vite
- React Router
- Tailwind CSS
- Zustand
- TanStack Query
- React Markdown or a lightweight Markdown renderer
- Zod for runtime validation
- Vitest for tests

### Local Data

- localStorage or IndexedDB
- JSONL reader utility
- Markdown parser utility

### Later Backend

- FastAPI or Next.js API routes
- SQLite first, then Postgres
- S3-compatible storage if files become large

## 5. Architecture

### Source of truth

Keep the repository as the canonical content layer:

- `docs/en/` and `docs/zh/`
- `labs/`
- `examples/`
- `templates/`
- `ebook/`

### App layer

The app should not duplicate content manually. It should import or transform repository files at build time.

### Build pipeline

A small build script should normalize repository content into app-friendly JSON:

- course index
- lesson list
- lab list
- search index
- evidence schema hints
- bilingual mapping

## 6. Implementation Phases

### Phase 1: Content Ingestion

Create a small content pipeline that converts the repository into JSON.

Outputs:

- `courses.json`
- `lessons.json`
- `labs.json`
- `search-index.json`

Rules:

- keep source paths in the JSON
- keep language keys for bilingual switching
- preserve level metadata
- keep tested_against / validated_date fields

### Phase 2: App Shell

Build a minimal Vite app with:

- top navigation
- home dashboard
- level overview
- lesson viewer
- lab viewer
- search page
- book / reader page
- progress panel

### Phase 3: Local Persistence

Use browser storage for:

- completed lessons
- bookmarks
- last opened item
- lab submission drafts

### Phase 4: Submission Workspace

Add a simple submission area for labs:

- paste text
- paste JSONL
- upload file name only in local mode
- show validation result
- save draft locally

### Phase 5: Backend Sync

Only after local MVP is stable:

- add user login
- add cloud submission storage
- add syncable progress
- add shareable portfolio links

## 7. Data Contracts

### Course

```ts
type Course = {
  id: string;
  level: 0 | 1 | 2 | 3 | 4 | 5;
  title: string;
  summary: string;
  sourcePath: string;
};
```

### Lesson

```ts
type Lesson = {
  id: string;
  courseId: string;
  title: string;
  language: 'en' | 'zh';
  sourcePath: string;
  summary: string;
  relatedLabId?: string;
};
```

### Lab

```ts
type Lab = {
  id: string;
  title: string;
  level: number;
  sourcePath: string;
  objective: string;
  selfCheck: string[];
  evidenceSchema?: string;
  testedAgainst?: string;
  validatedDate?: string;
};
```

### Progress

```ts
type Progress = {
  lessonId: string;
  labId?: string;
  completed: boolean;
  bookmarked: boolean;
  lastOpenedAt?: string;
};
```

## 8. Repository-to-App Mapping

- `docs/en/*` -> lessons / courses
- `docs/zh/*` -> localized lessons
- `labs/l0`-`labs/l5` -> practice tasks
- `examples/*` -> evidence exercises
- `templates/*` -> user artifacts
- `ebook/*` -> optional reader surface

## 9. Minimal Build Order

1. content pipeline script
2. React app shell
3. course and lesson pages
4. lab page
5. search
6. local progress
7. submission drafts
8. export summary

## 10. Build Validation

Run these checks before expanding features:

- `python scripts/check_repository.py`
- `python -m ruff check .`
- `python -m unittest discover -s tests -p 'test_*.py'`
- `python3 ebook/build_ebook.py`

## 11. Later Enhancements

- streaks and daily reminders
- level certificates
- trace viewer
- eval replay
- portfolio pages
- community submissions
- mobile PWA mode

## 12. Recommendation

Build the app as a local-first learning web app first.

Do not start with user accounts or server infrastructure.

Start with a repository-driven content layer, then add labs, then add evidence validation, then add sync.
