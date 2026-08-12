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

# MASTER_INDEX — spec

> The whole behavioral contract. One self-contained script; the pieces below ship as function groups inside it.

## Ownership

| Rule |
| ---- |
| Sentinels, literal: `<!-- AUTO:INDEX:BEGIN -->` and `<!-- AUTO:INDEX:END -->` — the script owns only the text between them |
| The block opens with a `> Auto-refreshed: YYYY-MM-DD` stamp line naming the ownership split: rows script-owned, Description column agent-editable and preserved |
| The stamp line is excluded from the change comparison — identical body means `no change` logged, no write |

## Root and scope

| Rule |
| ---- |
| The shelf declares its relationship to the root it indexes; the root derives from the installed script's location per that relationship |
| The resolved root is landmark-checked: no index file there — FAIL line, non-zero exit, no write |
| Scan config is declared data at the top of the script: (heading, root-relative path) pairs scanned recursively for `.md`, a separate pair list for project roots summarized one row per folder, an exclude set for trash/log/system dirs, a skip set for non-index files; a missing root is skipped, so the list grows without breaking |

## Description ledger

| Rule |
| ---- |
| Before each rebuild, harvest every `\| path \| description \|` row of the previous index into a path-keyed ledger — first occurrence wins |
| Descriptions are pipe-sanitized and whitespace-collapsed so a cell can never break its row |
| A moved file keeps its description by unique-basename carry: carried only when exactly one dead old path shares the basename — ambiguity means a blank cell, never a guess |
| New files get a blank Description cell an agent fills in place; the next run preserves it |

## Write discipline

| Rule |
| ---- |
| Fail-closed before write-if-changed before write — in that order |
| Every run prints exactly one timestamped log line from a fixed vocabulary: `index refreshed (N descriptions carried)` · `no change` · `FAIL <reason>` — a watcher greps this, never the index |
| Cadence: daily, offset from sibling jobs on the shelf |
