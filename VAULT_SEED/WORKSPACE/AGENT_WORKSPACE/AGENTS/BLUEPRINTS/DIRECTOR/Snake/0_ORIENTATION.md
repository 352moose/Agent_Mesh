---
type: blueprint
name: Snake — tutorial project
version: 1
created: 2026/08/09
updated: 2026/08/09
origin_machine: none — authored, never built
handoffs: 0
review_status: protected
---

# Snake — Tutorial Project Blueprint

> Arrival doc. A blueprint is a case study, not a script — it records what one machine did and why, with enough context that a reasoning agent can translate it to a different machine. Read this tree in numeric order. Nothing runs before `1_AUDIT.md` passes.

---

## What This Builds

A worked demonstration of the Director→CLIde cycle, run three times against real code on the user's own machine.

**The deliverable is the loop, not the program.** What a completed run leaves behind is three `ACTION_PROMPT`s, three `ACTION_REPORT`s, a `STATE.md` that moved, and a user who has checked a report against reality three times and knows what that feels like. Snake is the vehicle. It was chosen because a game is the one artifact nobody needs a report to evaluate — the user can tell in four seconds whether the cycle delivered what it claimed.

The consequence is worth stating plainly, because it inverts the usual measure of success:

| Run | Verdict |
| --- | ------- |
| Broken game, accurate report the user caught the problem from | **Succeeded** — the loop did its job and the user exercised the check |
| Working game, report nobody read | **Failed** — the demonstration did not happen, and nothing in the mesh will say so |

Do not close a cycle on a working program. Close it on a verified report.

---

## Read This First — This Blueprint Runs Backwards

Every other blueprint in this mesh was written after the build, from a machine where the thing already runs. This one was written before. Nothing here has been built yet, and both evidence registers are deliberately empty:

| Register | State | What fills it |
| -------- | ----- | ------------- |
| `3_BUILD/GOTCHAS.md` | empty | the first thing that breaks, written the moment it breaks |
| `3_BUILD/MACHINES.md` | empty | the first machine to complete a cycle |

That is not a defect to correct before shipping. It is the point of siting the tutorial here: the user's own run is what turns this into a case study, on a build where nothing is at stake if it goes wrong. A user who finishes the three cycles has also filled in their first blueprint without being asked to do paperwork.

Treat an empty register as *untested*, never as *clean*.

---

## Origin

| Field | Value |
| ---------------- | ----------------------------------------- |
| Authored on | macOS 15, Apple Silicon |
| Authored by | OVERSEER |
| First written | 2026/08/09 |
| Machines run on | 0 — `3_BUILD/MACHINES.md` is empty |

---

## Context Budget

| CAP       | Behavior                                    | Hygiene                              |
| --------- | ------------------------------------------- | ------------------------------------ |
| ≤ 8 lines | overwrite — one row per file in this tree   | re-measured when a file's cap changes |

> Cost to read, not order to read — the numbering carries the order. Measure against the receiving agent's window, not the sender's.

| File | ~Context % | Required |
| ------------------------- | ---- | ------------------------------------------ |
| `1_AUDIT.md`              | <1   | yes |
| `2_TEACH.md`              | 1    | yes — unless the user waives at the stop |
| `3_BUILD/PROCEDURE.md`    | 2    | yes |
| `3_BUILD/GOTCHAS.md`      | <1   | yes — empty, and reading it is how you learn it is empty |
| `3_BUILD/MACHINES.md`     | <1   | yes on this blueprint — no gate has evidence behind it yet |
