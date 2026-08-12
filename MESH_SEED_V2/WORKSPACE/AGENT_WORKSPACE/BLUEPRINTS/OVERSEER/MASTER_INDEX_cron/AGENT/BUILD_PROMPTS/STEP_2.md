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

# STEP_2

> Threshold: the tree is legible as one page — the scanner derives the whole body from the tree alone.

| Phase  | DO                | Payload |
| ------ | ----------------- | ------- |
| Load   | Read              | DONE.md · SPEC §Root and scope · STEP_1 landing |
| Work   | Search surfaces   | this tree — choose the scan roots that explain it, the project roots, and the dirs that must never appear (trash, logs, system) |
| Work   | Establish toolset | recursive walk from the resolved root — landmark-check it first, live |
| Work   | Build             | one script on the scheduled shelf whose run fills the sentinel block: contents list, one table per directory, one row per project folder, blank Description cells |
| Gate   | Break?            | GOTCHAS → `AGENT/GOTCHAS/[ROOM]/` — at the moment |
| Fork   | Carry forward     | the body regenerates but a filled Description cell does not yet survive a refresh — STEP_3 = true |
| Report | Landing           | run twice: second run reports `no change`; remove one sentinel on a scratch copy — non-zero exit, no write |
