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
