---
type: Index
class: work
state: unflagged
review_status: protected
created: 2026/08/05
updated: 2026/08/11
tags:
  - index
  - mesh
---

# Mesh Master Index

> A table of contents for the mesh — every knowledge doc with its path and a one-line description, so you can find where information lives without remembering the folder tree.
>
> **Scope:** the agent system (bootstraps, rules, templates, refs) and the work (projects, one line per project). **Excluded:** memory cards, agent desks, and trash.
>
> Script-owned: `OPERATOR_WORKSPACE/CRONS/SCRIPTS/master_index.py` refreshes the rows daily once installed (user-owned cron, staged during the Overseer's first setup session). The **Description column is agent-editable** — add or fix a description in place and the script preserves it across refreshes, including file moves. Blank descriptions stay blank until an agent fills them.

<!-- AUTO:INDEX:BEGIN -->
> Auto-refreshed: — rows are script-owned; the Description column is agent-editable and preserved across refreshes.

## Contents

- [Agent System — Rules](#agent-system-rules)
- [Agent System — Bootstraps](#agent-system-bootstraps)
- [Agent System — Templates](#agent-system-templates)
- [REFS](#refs)
- [Operator Workspace](#operator-workspace)
- [Projects (Overview)](#projects-overview)

---

## Agent System — Rules

| Path | Description |
|---|---|

## Agent System — Bootstraps

| Path | Description |
|---|---|

## Agent System — Templates

| Path | Description |
|---|---|

## REFS

| Path | Description |
|---|---|

## Operator Workspace

| Path | Description |
|---|---|

## Projects (Overview)

| Path | Description |
|---|---|

<!-- AUTO:INDEX:END -->

---

## Tour Card

> Guide: deliver the fenced block verbatim at this tour stop.

```
── Tour Stop — WORKSPACE/MASTER_INDEX.md

This is the master index — the table of contents for everything the
workspace knows. Every knowledge doc gets a row: its path and a
one-line description, so you can ask "where does that live?" and get
an answer without memorizing the folder tree. The best part: you never
maintain it. Once the Overseer's first setup session installs the
little script that runs it, the rows rebuild themselves every day —
new files and moved files caught on their own — and the agents fill
in the descriptions as they work. Right now it's mostly empty shelves — as
your workspace grows, this page grows with it. When you're looking
for something and don't know where to start, start here.
```
