---
title: Multilingual Pattern Lab
capability_level: L5
validated_date: 2026-09-17
tested_against: "python 3.10+, node 20+, rust 1.58+, go 1.21+, typescript 7.0.2"
---

# L5 Lab: Multilingual Pattern

## Goal

Translate one stable L5 Agent pattern into five language implementations: Python, Node.js, Rust, Go, and TypeScript.

## Prerequisites

- L5 custom pattern concepts.
- One local language runtime where relevant.

## Run

Python is always available through the repository test suite:

```bash
python -m unittest labs.l5.multilingual_pattern_lab.test_lab
```

Install the local TypeScript compiler used by the smoke runner:

```bash
npm ci
```

Cross-language smoke checks:

```bash
python scripts/smoke_multilingual_labs.py
```

Expected smoke branches include Python, Node.js, Rust, Go, and TypeScript when the local runtime and compiler are available.


## Maintenance Contract

For every non-Python Lab, maintain these fields in the Lab README or in the Lab owner's PR notes:

- Source of truth: the canonical pattern contract or upstream Lab.
- Owner: the language maintainer responsible for parity and staleness fixes.
- Toolchain: package manager, compiler, runtime, and compiler flags used for validation.
- Validation: exact local command and expected output shape.
- Parity: accepted differences from Python behavior and why they are intentional.

A multilingual Lab is not complete when only syntax ports exist. It is complete only after a maintainer can rerun the checks from a clean checkout and explain any behavioral difference.

## What This Lab Teaches

- Language syntax differs; the pattern contract should stay stable.
- Every implementation must show `clarify`, `execute`, and `verify`.
- Every implementation must stop before execution when a safety rule matches.

## Common Pitfalls

- Copying framework-specific Agent code instead of the reusable pattern.
- Using different output shapes across languages without documenting the reason.
- Treating TypeScript syntax in a JS file as valid Node.js runtime code.

## Self-Check

1. What invariants must survive translation across languages?
2. Why should blocked safety checks return no plan steps?
3. How would you extend this pattern to another Lab without changing its contract?
