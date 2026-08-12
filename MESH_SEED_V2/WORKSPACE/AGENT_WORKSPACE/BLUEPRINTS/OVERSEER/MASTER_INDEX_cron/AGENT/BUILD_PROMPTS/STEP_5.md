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

# STEP_5

> Threshold: the job runs without anyone — a real scheduled tick advances the log with no human in the loop.

| Phase  | DO                | Payload |
| ------ | ----------------- | ------- |
| Load   | Read              | DONE.md constraints · SPEC §Write discipline cadence row · STEP_4 landing |
| Work   | Search surfaces   | the scheduled shelf: sibling jobs' tick times, the install file, the log room |
| Work   | Establish toolset | `crontab -l` — the operator owns the crontab; agents stage and verify, never own |
| Work   | Build             | the script seated on the shelf, one crontab line (daily, offset from siblings, stdout+stderr appended to the shelf log), install file regenerated from the LIVE crontab |
| Gate   | Break?            | GOTCHAS → `AGENT/GOTCHAS/[ROOM]/` — at the moment |
| Fork   | Carry forward     | none — read the landing against DONE |
| Report | Landing           | the job is live only when a REAL scheduled tick advances the log — a hand-run proves nothing and masks a dead cron |
