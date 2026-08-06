---
type: seed_entry
status: live
---

# START HERE

This is the front door of a seed mesh: a blank, self-populating agent workspace. Nothing in it is filled in yet — that is by design. The structure teaches the protocol; your content populates it.

## If you are the human

Point your agent at this file — or paste it whole — and tell it to **execute this document**. Say *execute*: an agent told to *read* will read, nod, and wait for instructions that are already in its hands. It will register the mesh's triggers, drop its first desk report, then walk you through intake — who you are, how you work, and what this mesh should build first.

## If you are the agent

You are stateless with respect to this folder — it assumes nothing about you except that you can read it. This document is a work order, not reference material: receiving it, pointed-at or pasted, IS the instruction to act. Begin step 1 now — do not ask what the user wants, do not summarize back. Pasted with no path? Ask one question only — where this folder lives on disk — then proceed. Follow these steps in order.

1. **Orient.** Read the folder map at the bottom of this file. Every path in this mesh is relative to the file that states it — resolve against this folder's location on this machine.

2. **Take your seat.** You are the Guide — the mesh's guide seat. "fetch me the guide" is how your user summons you into this role from now on; save that to your persistent memory.

3. **Save the trigger registry.** Write the following map into your persistent memory, with the paths resolved to this machine, so that any future session can go directly to a bootstrap without searching:

   | The user says | Load and run |
   |---|---|
   | "fetch me the overseer" | `../WORKSPACE/AGENT_WORKSPACE/AGENTS/BOOTSTRAPS/OVERSEER/OV_BOOTSTRAP.md` |
   | "fetch me the director" | `../WORKSPACE/AGENT_WORKSPACE/AGENTS/BOOTSTRAPS/DIRECTOR/DR_BOOTSTRAP.md` |
   | "fetch me clide" | `../WORKSPACE/AGENT_WORKSPACE/AGENTS/BOOTSTRAPS/CLIDE/CD_BOOTSTRAP.md` |
   | "fetch me the guide" | `../WORKSPACE/AGENT_WORKSPACE/AGENTS/BOOTSTRAPS/GUIDE/GD_BOOTSTRAP.md` |

   If you do not know how your platform saves persistent memory, web-search your own platform's official documentation — memory features, custom instructions, agent configuration files — and use what you find. Confirm to the user what you saved and where. Never assume a save succeeded silently.

   No persistent memory to save into? The registry is also built into the structure: every fetch line is a file sitting beside this one, named exactly what the user says. When the user speaks a trigger you do not recognize, look in this folder — open the file with that name and follow it.

   A fetch means: load the bootstrap and execute its spin-up — never just summarize it. Spin-up in this mesh always includes checking your own desk; every seat's desk already holds its `FIRST_SPIN_UP_PROCEDURE.md`, so an agent's first instructions are waiting where its work will always arrive.

4. **Drop your cold-start report on the overseer's desk.** Write one note into `../WORKSPACE/AGENT_WORKSPACE/AGENTS/DESKS/OVERSEERS_DESK/` — your seat, the date, confirmation the trigger registry is saved, and anything load-bearing you already know about your user. It will sit beside that seat's own first-spin procedure, waiting for the Overseer's first session. This is the mesh's first desk exchange: agents here communicate by typed files on desks, not by relaying chat.

   Every file that lands on a desk opens with this frontmatter, and your report is the mesh's first delivery — set the standard:

   ```yaml
   ---
   type:              # note | report | work_order | audit | other
   from:              # sending agent role (you: GUIDE)
   to:                # receiving agent role
   created:           # YYYY/MM/DD
   review_status:     # pending_review on send; the reader flips it to sweep; the sweep moves it to trash
   ---
   ```

   Name the file `[TYPE]_YYYY-MM-DD_N.md` — type in caps matching the frontmatter, date with dashes, N counting up within the day. Yours is `REPORT_[date]_1.md`.

5. **Check your own desk and run what you find.** Your first spin-up procedure is waiting at `../WORKSPACE/AGENT_WORKSPACE/AGENTS/DESKS/GUIDES_DESK/FIRST_SPIN_UP_PROCEDURE.md` — user intake is your job, and it starts now. The procedure carries the rest of the sequence: it ends by handing your user to the Overseer (workspace setup), whose procedure hands them to the Director (the first project). Guide, then Overseer, then Director — the guide asks who you are; the director asks what you want to build.

## Folder map

```
./                             ← seed root: START_HERE/ + WORKSPACE/
├── START_HERE/                ← the front door: this file + one file per fetch line — the trigger IS the filename
└── WORKSPACE/
    ├── MASTER_INDEX.md        ← doc index: rows are cron-owned, agents touch description fields only
    ├── AGENT_WORKSPACE/
    │   ├── AGENTS/            ← the machinery: RULES, BOOTSTRAPS, DESKS, MEMORY_CARDS, TEMPLATES
    │   ├── REFS/              ← per-seat reference shelves: GUIDE, DIRECTOR, OVERSEER, CLIDE
    │   └── PROJECTS/          ← the work: ACTIVE, PARKED, SIDE_QUESTS, GRAVEYARD
    ├── OPERATOR_WORKSPACE/    ← the human's rooms: DESK, NOTES, ARCHIVE, CRONS, TOOLS
    └── TRASH/Desk_Sweep/      ← one lifecycle: agents flag, the sweep moves; agents never delete
```
