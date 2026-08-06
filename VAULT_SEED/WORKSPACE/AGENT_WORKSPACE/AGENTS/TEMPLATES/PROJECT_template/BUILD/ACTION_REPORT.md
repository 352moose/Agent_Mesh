---
type: action_report
project: {PROJECT_NAME}
step: {STEP_ID}
updated: {YYYY/MM/DD}
maintained_by: CLIDE
review_status: protected
sender_assessment: {pass | fail | partial}
---

## Page Rules

| Rule           | Value                                                                     |
| -------------- | -------------------------------------------------------------------------- |
| Who writes     | CLIDE — at spindown, after the live-launch gate                            |
| Who reads      | DIRECTOR — adjudicates pass/fail and plans the next step from it           |
| Write model    | overwrite the entire doc each step — preserve this heading skeleton        |
| Update trigger | spindown, after the operator has run the live launch                       |
| Size cap       | none — one step's worth of content                                         |

---

# Action Report — {PROJECT_NAME}

## Status: {PASS | FAIL | PARTIAL}

## Step Executed

{STEP_ID} — {step title from the ACTION_PROMPT}

## What Was Done

{Plain-language summary — what changed, what was added, how it works. No code blocks; enough for the Director to understand the delta without reading code.}

## Files Changed

| File | Change |
|---|---|
| {path} | {Added / Modified / Deleted — brief note} |

**Total: {N} source files** ({+N added, -N deleted, N modified})

## Verification

{Self-checks (compile / type-check / lint — necessary, not sufficient) and operator-run verification (name the command or launch) — kept separate. State outcomes plainly: passed / failed / skipped.}

## Deviations from Plan

- {what the prompt said, what was done instead, why — "None" if none}

## Director Notes

- {flags, scope observations, stale docs — CLIde's channel to the next plan}
