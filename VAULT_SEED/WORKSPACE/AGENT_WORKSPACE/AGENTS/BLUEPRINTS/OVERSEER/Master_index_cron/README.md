---
type: note
scope: BLUEPRINTS/OVERSEER/Master_index_cron
maintained_by: OVERSEER
created: 2026/08/09
review_status: protected
---

# Master index cron — blueprint

Case study for the scheduled job that rebuilds `MASTER_INDEX.md`. Read `0_ORIENTATION` through `3_BUILD` in order.

---

## Dive Card

> Guide: not a walk stop — deliver the fenced block verbatim only when the user takes the dive option at the shelf fork.

```
── Tour Stop — AGENTS/BLUEPRINTS/OVERSEER/Master_index_cron/

This blueprint rebuilds the document index — the file that answers
"where does this live" without anyone opening folders to find out. It
covers why an index kept up by hand always goes stale, what the job
scans and what it deliberately skips, and how it rewrites the rows
without disturbing the descriptions people wrote by hand.

The record of what broke is the part worth reading. One entry is a
trap that has fooled better engineers than this mesh: a test run you
start yourself writes to the same log a scheduled run does, so a job
that has never once succeeded on schedule can show a log full of
successes. The rule that came out of it is that only a real scheduled
tick counts as proof.
```
