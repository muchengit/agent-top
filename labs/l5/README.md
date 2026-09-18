---
title: L5 Labs
capability_level: L5
validated_date: 2026-09-18
---

# L5 Labs

## Goal

Create original patterns, reusable catalogs, and multilingual pattern implementations with safety and verification evidence.

## Prerequisites

- L4: productionized Agent systems
- Python 3.10+ (plus Node.js, Rust, Go, or TypeScript for the multilingual Lab)
- Familiarity with pattern-first design and external contribution

## Labs in This Level

- [`custom_pattern_lab`](custom_pattern_lab/README.md): reusable custom pattern with safety and verification.
- [`pattern_catalog`](pattern_catalog/README.md): reusable pattern catalog with readiness checks.
- [`multilingual_pattern_lab`](multilingual_pattern_lab/README.md): one pattern translated across Python, Node.js, Rust, Go, and TypeScript.
- [`pattern_eval_gate`](pattern_eval_gate/README.md): deterministic gate for patterns entering the catalog.

## Run

```bash
python -m unittest discover -s labs/l5 -p "test_*.py"
```

For the multilingual Lab, follow its `README.md` smoke commands per language.

## Common Pitfalls

- Claiming an original pattern without safety and verification evidence.
- Adding patterns to the catalog before readiness checks pass.
- Letting translated implementations drift from the source-of-truth language.

## Self-Check

1. What evidence proves a custom pattern is reusable and safe?
2. When is a pattern ready to enter the catalog?
3. How do you keep multilingual implementations in parity?

