---
type: note
created: 2026/08/05
review_status: protected
title: Desk sweep destination
---

# Desk Sweep

> Sweep destination. The desk-sweep cron moves files flagged `review_status: sweep` here, one subfolder per seat. Agents flag, the sweep moves — agents never delete. Build instructions for the cron: `../../OPERATOR_WORKSPACE/CRONS/README.md`.

---

## Tour Card

> Guide: deliver the fenced block verbatim at this tour stop.

```
This is where desk mail ends up. When a seat finishes with a file, it
never deletes it — it flips the file's review_status to sweep and
leaves it on the desk. An hourly cron, which you install and own during
workspace setup, does the actual moving: it collects every
sweep-flagged file from all the desks — yours included — and files it
here, one subfolder per seat. Nothing is destroyed along the way;
agents flag, the sweep moves, and only you ever delete. If a file has
vanished from a desk, this is the first place to look.
```
