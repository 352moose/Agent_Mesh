---
type: note
title: Mesh Master Index
created: 2026/08/05
maintained_by: OPERATOR_WORKSPACE/CRONS/SCRIPTS/master_index.py
review_status: protected
---

# Mesh Master Index

> A table of contents for the mesh — every knowledge doc with its path and a one-line description, so you can find where information lives without remembering the folder tree.
>
> **Scope:** the agent system (bootstraps, rules, templates, refs) and the work (projects, one line per project). **Excluded:** memory cards, agent desks, and trash.
>
> Script-owned: `OPERATOR_WORKSPACE/CRONS/SCRIPTS/master_index.py` refreshes the rows daily (user-owned cron). The **Description column is agent-editable** — add or fix a description in place and the script preserves it across refreshes, including file moves. Blank descriptions stay blank until an agent fills them.

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
maintain it. A scheduled script rebuilds the rows every day, catching
new files and moved files on its own, and the agents fill in the
descriptions as they work. Right now it's mostly empty shelves — as
your workspace grows, this page grows with it. When you're looking
for something and don't know where to start, start here.
```
