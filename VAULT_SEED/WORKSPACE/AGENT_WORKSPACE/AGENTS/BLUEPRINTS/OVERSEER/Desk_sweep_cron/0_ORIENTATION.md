---
type: blueprint
name: Desk sweep cron
version: 1
created: 2026/08/08
updated: 2026/08/08
origin_machine: macOS 15 (Darwin 25.5), Apple Silicon
handoffs: 0
review_status: protected
---

# Desk Sweep Cron — Blueprint

> Arrival doc. A blueprint is a case study, not a script — it records what one machine did and why, with enough context that a reasoning agent can translate it to a different machine. Read this tree in numeric order. Nothing runs before `1_AUDIT.md` passes.

---

## What This Builds

A scheduled script that checks every agent desk each hour and moves any file marked `review_status: sweep` into the trash tree, filed under the desk it came from.

---

## Origin

| Field | Value |
| ---------------- | ----------------------------------------- |
| Built on | macOS 15, Apple Silicon, python3 3.9 (system) |
| Built by | OVERSEER |
| First built | 2026/07 — moved from launchd to cron 2026/08/05 |
| Machines run on | 1 — recorded in `3_BUILD/MACHINES.md` |

> Live on the origin machine, hourly. Covers two separate vaults on that machine from one script.

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
| `3_BUILD/GOTCHAS.md`      | 1    | yes |
| `3_BUILD/MACHINES.md`     | <1   | only when no gate matches this machine |
