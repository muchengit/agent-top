# How to Use This Book

Agent-Top is organized around an L0-L5 capability model. Work through the chapters in order if you are starting from scratch. If you already have context, use the table of contents to jump to the level you need.

Each chapter is designed to move from concept to action:

1. Read the chapter.
2. Inspect the related Lab or Example.
3. Run the smallest relevant check.
4. Record evidence before moving on.

## Local Checks

Use these commands from the repository root:

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

## Evidence Principle

Keep your notes focused on inputs, decisions, outputs, and checks. A short evidence trail is more useful than a long retrospective.
