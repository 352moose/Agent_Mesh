---
type: project
class: work
state: unflagged
review_status: live
created: 2026/08/12 OV S103
updated: 2026/08/12 OV S103
tags:
  - blueprint
  - modules
---

# SWEEP — spec

> The whole behavioral contract. One self-contained script; the pieces below ship as function groups inside it.

## Desk discovery

| Rule |
| ---- |
| The folder is the binding: the home-vault pool is DERIVED at run time from every directory matching the desk-room shape (`AGENTS/DESKS/*_DESK`) — a new seat is swept the hour its desk exists, and a parked seat falls out of the pool with no skip-list |
| Never a hardcoded desk list — an enumerated list silently misses live desks and nothing reports it |
| Sweep bucket = seat name derived from the desk name: `[SEAT]S_DESK` yields `[SEAT]`; a desk without that shape buckets under its own full name |
| Destination, always: `TRASH/Desk_Sweep/[SEAT]/` inside that desk's OWN vault |
| A foreign vault cannot self-resolve: its desks are LISTED as (agent, desk path, destination path) against that vault's absolute root — listed, never derived, and zero foreign entries is a valid list |

## Status read

| Rule |
| ---- |
| The control surface is one frontmatter field: `review_status: sweep` moves the file, anything else — including no frontmatter — skips it with the reason recorded |
| Fixture files, `_NAME_` shape, are skipped by name before the frontmatter is ever read |
| A file that cannot be read lands in the errors bucket with the exception text; the pass continues |

## Safe move

| Rule |
| ---- |
| Desk filenames collide by design (per-desk numbering) — a bare move silently overwrites an earlier sweep; on collision, suffix and retry until the name is free |
| The destination folder is created on demand — real runs only; a dry run creates and moves nothing |

## Report

| Rule |
| ---- |
| Each tick emits ONE JSON object: swept, skipped, errors (each entry naming agent, file, and destination or reason), totals, timestamp |
| The report appends to the shelf log via the crontab redirect — a watcher greps the log, never re-walks the desks |
| Cadence: hourly |
