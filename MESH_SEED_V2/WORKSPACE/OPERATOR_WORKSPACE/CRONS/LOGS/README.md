---
type: readme
class: work
state: unflagged
review_status: live
created: 2026/08/05
updated: 2026/08/11
tags:
  - readme
  - logs
---

# Logs

> Every script run writes here — a dated stamp per run, success or failure, errors in full. One log file per cron. A job is verified live only when a REAL scheduled tick advances its stamp; interactive runs don't count.
>
> **Script-owned.** The scripts populate these files — agents and users read, never write.

---

## Dive Card

> Guide: not a walk stop — deliver the fenced block verbatim only when the user takes the dive option at the shelf fork.

```
── Tour Stop — WORKSPACE/OPERATOR_WORKSPACE/CRONS/LOGS/

Every scheduled run leaves its record here — one log file per cron, a
dated stamp for each run, success or failure, errors written out in
full. The scripts write these themselves; you and the agents only read.
The folder starts empty, and its first entry is a small milestone: a
job counts as live only once a real scheduled tick lands a stamp, so
after install this is where the mesh looks to confirm your crons are
actually running. When something breaks, the full story is in here.
```
