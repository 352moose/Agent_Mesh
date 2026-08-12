---
type: project
class: work
state: unflagged
review_status: live
created: 2026/08/12 OV S103
updated: 2026/08/12 OV S103
tags:
  - blueprint
  - done
---

# DONE — MASTER_INDEX cron

> What does done look like?

| Field       | Entry |
| ----------- | ----- |
| output      | The AUTO block of the tree root's `MASTER_INDEX.md`, rebuilt daily by an unattended job: a linked contents list, one `Path` / `Description` table per directory under each declared scan root, a one-row-per-folder Projects overview, every agent-written description re-attached; exactly one timestamped log line per run |
| Interface   | The index itself, read in Obsidian — curated head above the sentinels is human-owned and never touched; the Description column is agent-editable in place and survives every refresh and file move; the crontab line and the shelf log tail are the only other surfaces |
| constraints | Standard library only, one self-contained script. Owns ONLY the text between the AUTO sentinels. Fail-closed: missing index, missing or inverted sentinels — non-zero exit, no write. Write-if-changed: an identical body is never rewritten. Description-agnostic: the script never authors a description. Installation establishes scope: the shelf declares its relationship to the root it indexes, the root derives from the installed script's location per that relationship, and the resolved root is landmark-checked — no index file there means fail-closed, never a write into the wrong tree. The operator owns the crontab. The job is live only when a REAL scheduled tick advances its log |
