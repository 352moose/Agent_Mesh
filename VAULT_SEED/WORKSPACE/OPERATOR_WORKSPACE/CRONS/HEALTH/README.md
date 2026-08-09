---
type: note
created: 2026/08/05
review_status: protected
title: Cron health board
---

# Health

> Status board, written by the scripts themselves — one line per cron: `OK` or `NOT OK`, stamped with the last run. On `NOT OK`, append a one-liner naming the blocker if the script can tell (permission denied, path missing, target unwritable); otherwise point to the log. Read this first, dig in `../LOGS/` second.
>
> **Script-owned.** The scripts populate this board — agents and users read, never write.

---

## Dive Card

> Guide: not a walk stop — deliver the fenced block verbatim only when the user takes the dive option at the shelf fork.

```
── Tour Stop — WORKSPACE/OPERATOR_WORKSPACE/CRONS/HEALTH/

This is the status board for your crons — the quick read before anyone
opens a log. The scripts keep it themselves: one line per job, OK or
NOT OK, stamped with the last run, plus a one-liner naming the blocker
when a script can tell what went wrong. You and the agents read it,
never write it. It starts empty and comes alive once the crons are
installed and ticking; after that, a glance here tells you whether the
automation is healthy, and LOGS next door holds the detail.
```
