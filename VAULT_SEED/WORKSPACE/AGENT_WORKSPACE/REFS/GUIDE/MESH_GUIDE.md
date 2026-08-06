---
type: reference
scope: GUIDE
maintained_by: GUIDE
created: 2026/08/05
updated: 2026/08/05
review_status: protected
---

# MESH GUIDE

> How this workspace works, in plain language. The Guide answers mesh questions from this doc and keeps it current as the mesh evolves.

## Page Rules

| Rule |
|---|
| Plain language — this doc is for the user, not for agents |
| Update when a seat, channel, or convention changes; stamp `updated` |
| Routing table stays current — a wrong route costs more than a missing one |

---

## What this is

A file-based multi-agent workspace. Each agent ("seat") is spun up by a fetch line, does one kind of work, and communicates with other seats through typed files on desks. Memory lives in files, so any session can pick up where the last one left off.

A fresh mesh opens with three first spin-ups, in order: Guide (who you are), then Overseer (workspace setup), then Director (your first project). Each seat's first procedure waits on its desk and hands you to the next.

## The seats

| Seat       | Fetch line                | What it does                                                                    |
| ---------- | ------------------------- | -------------------------------------------------------------------------------- |
| GUIDE | `fetch me the guide` | Your first stop — the mesh's guide. Explains how things work, routes work to the right seat; ad-hoc help at your direction |
| DIRECTOR   | `fetch me the director`   | Plans project work one step at a time; writes the build prompt CLIde executes    |
| CLIDE      | `fetch me clide`          | Build-side executor. Runs one ACTION_PROMPT in the terminal, with you            |
| OVERSEER   | `fetch me the overseer`   | Workspace keeper. Audits structure, keeps conventions consistent, intake seat    |

## How build work flows

1. **DIRECTOR** discusses one step with you, then writes `ACTION_PROMPT.md` in the project's BUILD folder.
2. You fetch **CLIDE** in a terminal; it executes that prompt with you and hands you a live launch to verify.
3. CLIde writes `ACTION_REPORT.md`; you go back to **DIRECTOR**, who absorbs the result and plans the next step.

One step at a time, verified on your real workflow before it counts.

## Routing — "I want to..."

| Need                                               | Seat       |
| --------------------------------------------------- | ---------- |
| Research something, think out loud, one-off task    | GUIDE |
| Start or continue building a project                | DIRECTOR   |
| Execute the prompt the Director wrote               | CLIDE      |
| Add a seat, fix structure, change a convention      | OVERSEER   |
| Understand how any of this works                    | GUIDE |

## Conventions in one minute

- **Desks** (`../../AGENTS/DESKS/`): typed files are how seats talk. Frontmatter says who it's from, who it's for, and its `review_status`.
- **review_status lifecycle**: `pending_review` (needs the receiver's read) → `sweep` (absorbed, scheduled for removal) → gone. `protected` = permanent fixture, never swept.
- **Memory cards** (`../../AGENTS/MEMORY_CARDS/`): each seat has ACTIVE (standing facts), a session scratch file, and static session cards. CLIde is the exception — its memory is tied to each project.
- **Paths are relative** — every address in every file resolves from that file's location. Nothing machine-specific, so the mesh survives being moved.
- **Agents flag, never delete** — the sweep moves flagged files to TRASH.
- **REFS** (`../[SEAT]/`): each seat's reference shelf for standing docs — like this one.
- **Your rooms** (`../../../OPERATOR_WORKSPACE/`): the human's side of the mesh — your DESK (agents deliver reports to you there), NOTES, ARCHIVE, TOOLS, and CRONS.
- **Automation is yours** — agents stage scripts, you install and own the crontab. Two crons keep house: a daily refresh of the doc index (`../../../MASTER_INDEX.md` — find any doc without remembering the tree) and an hourly desk sweep that moves `sweep`-flagged files to trash.
