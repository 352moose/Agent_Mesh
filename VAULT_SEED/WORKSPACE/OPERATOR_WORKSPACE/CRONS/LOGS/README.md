---
type: note
created: 2026/08/05
review_status: protected
title: Cron logs
---

# Logs

> Every script run writes here — a dated stamp per run, success or failure, errors in full. One log file per cron. A job is verified live only when a REAL scheduled tick advances its stamp; interactive runs don't count.
>
> **Script-owned.** The scripts populate these files — agents and users read, never write.
