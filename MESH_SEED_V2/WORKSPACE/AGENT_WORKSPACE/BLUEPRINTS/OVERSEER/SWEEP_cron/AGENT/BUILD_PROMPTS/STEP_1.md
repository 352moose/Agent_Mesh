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

# STEP_1

> Threshold: the desk pool is knowable without being named — discovery and status read work, proven dry.

| Phase  | DO                | Payload |
| ------ | ----------------- | ------- |
| Load   | Read              | DONE.md · `FOLDER_TREE/MODULES/SWEEP/SPEC.md` §Desk discovery + §Status read |
| Work   | Search surfaces   | the desk room — its `*_DESK` shape, the fixture files on each desk, what frontmatter the desk files actually carry |
| Work   | Establish toolset | `python3` on the scheduled shelf's interpreter — run it live; landmark-check the resolved root against the desk room |
| Work   | Build             | one script on the scheduled shelf: derive the pool from the desk-room shape, read `review_status` tolerantly, `--dry-run` reports every desk, file, and verdict without moving |
| Gate   | Break?            | GOTCHAS → `AGENT/GOTCHAS/[ROOM]/` — at the moment |
| Fork   | Carry forward     | verdicts are right but nothing moves yet — STEP_2 = true |
| Report | Landing           | dry run lists every desk in the room including any it was never told about; a frontmatter-less file skips with its reason, no crash |
