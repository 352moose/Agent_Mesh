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

# STEP_4

> Threshold: the write can be trusted unattended — every failure mode exits without touching the file, every run leaves one grep-able line.

| Phase  | DO                | Payload |
| ------ | ----------------- | ------- |
| Load   | Read              | SPEC §Write discipline · STEP_3 landing |
| Work   | Search surfaces   | the failure modes: missing index, missing sentinel, inverted sentinels, wrong resolved root, unchanged body |
| Work   | Establish toolset | a scratch copy of the index to break on purpose |
| Work   | Build             | fail-closed guards, write-if-changed with the stamp line excluded from compare, the fixed three-line log vocabulary |
| Gate   | Break?            | GOTCHAS → `AGENT/GOTCHAS/[ROOM]/` — at the moment |
| Fork   | Carry forward     | the script is correct but nothing schedules it — STEP_5 = true |
| Report | Landing           | each broken scratch copy exits non-zero with a FAIL line and writes nothing; the healthy run logs exactly one line |
