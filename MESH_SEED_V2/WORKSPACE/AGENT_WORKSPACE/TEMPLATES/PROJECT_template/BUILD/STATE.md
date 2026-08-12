---
type: project
class: work
state: unflagged
review_status: live
created: "{YYYY/MM/DD XX S_N}"
updated: "{YYYY/MM/DD XX S_N}"
tags:
  - build
  - state
---

## Reading List

| CAP        | Behavior                                        | Hygiene                      |
| ---------- | ----------------------------------------------- | ---------------------------- |
| ≤ 15 lines | overwrite — read order after this doc, top-down | rotate; triage by importance |

> Ordered by priority; label each with ~context %
> Docs the bootstrap already loads get no row — the list starts where the boot stops.

| #   | Document             | Path                                           | ~Context % |
| --- | -------------------- | ---------------------------------------------- | ---------- |
| 1   | Action Prompt        | `PROJECTS/ACTIVE/[PROJECT]/…/ACTION_PROMPT.md` |            |



## Patterns / Anti-Patterns

| CAP                  | Behavior                                | Hygiene                              |
| -------------------- | --------------------------------------- | ------------------------------------ |
| ≤ 10 lines each list | fluid — one line + tally, cross-session | highest tally promotes to convention |

> Tally increments each re-flag. High tally = proven pattern / recurring trap

### Patterns
- **[N]x** — {pattern}

### Anti-Patterns
- **[N]x** — {anti-pattern}

----

## Conventions

| CAP        | Behavior                                                                                         | Hygiene                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| ≤ 20 lines | fluid — one line per convention, added by pattern promotion; tally increments each time it bites | over cap → lowest tally folds into its parent or retires first; a superseded convention retires outright at any tally |


> One line per convention: the standing rule + why;
>  Tally = times it actually bound work (shaped a prompt, blocked a drift, settled a call) — sharpen on contact

| Tally | Convention    | Why                                      |
| ----- | ------------- | ---------------------------------------- |
| [1]x  | {do X with Y} | {The project's standards and principals} |
