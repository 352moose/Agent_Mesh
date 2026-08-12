---
type: project
class: work
state: unflagged
review_status: live
created: 2026/08/12 OV S103
updated: 2026/08/12 OV S103
tags:
  - blueprint
  - build
---

# STEP_3

> Threshold: agent knowledge survives the machine — a description written into the index outlives every refresh and a file move.

| Phase  | DO                | Payload |
| ------ | ----------------- | ------- |
| Load   | Read              | SPEC §Description ledger · STEP_2 landing |
| Work   | Search surfaces   | the previous index body — every table row is a potential (path, description) fact |
| Work   | Establish toolset | harvest replay, read-only: parse the live index, count what a rebuild would carry |
| Work   | Build             | harvest → path-keyed ledger → re-attach on rebuild; unique-basename carry for moved files; ambiguity leaves the cell blank |
| Gate   | Break?            | GOTCHAS → `AGENT/GOTCHAS/[ROOM]/` — at the moment |
| Fork   | Carry forward     | the body is right but the write is still unguarded — STEP_4 = true |
| Report | Landing           | fill one cell, run — the cell survives; move that file, run — the description followed it |
