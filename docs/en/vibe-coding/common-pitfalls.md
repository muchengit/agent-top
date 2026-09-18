---
title: Common Pitfalls
validated_date: 2026-09-18
i18n-key: vibe-coding-pitfalls
last-synced: 2026-09-18
---

# Common Pitfalls

## Pitfall 1: Vague Prompts

Symptom: "make it better" prompts; the diff grows with every round.

Fix: write the spec first. If the goal cannot be stated, research, do not prompt.

## Pitfall 2: Skipping the Diff Review

Symptom: the assistant "fixed" unrelated files, changed permissions, or added dependencies.

Fix: review the full diff before running anything; revert scope creep.

## Pitfall 3: Trusting "Should Work"

Symptom: no run, no test, "looks correct."

Fix: grep for the acceptance command; if it is absent, the change is unverified.

## Pitfall 4: Loop Without Evidence

Symptom: many iterations, no record of what failed or what the final check output was.

Fix: save the error output and the final green output; paste real errors in the next prompt.

## Pitfall 5: Overfitting to One Input

Symptom: the fix passes the one failing case and breaks everything else.

Fix: after green, run the full suite and add a regression case for the failure.

## Pitfall 6: Ignoring Bilingual Mirrors

Symptom: EN docs updated, ZH mirror stale, `last-synced` untouched.

Fix: in Agent-Top, update both sides or flag `sync-required`; the repository check blocks unpaired keys.

## Self-Check

1. Can you state the goal and acceptance check in one sentence?
2. Did you review the diff before running anything?
3. Does the acceptance command exist in the change and pass?
4. Did you preserve or add evidence (test, trace, eval)?
5. Are the bilingual mirrors in sync or explicitly flagged?
