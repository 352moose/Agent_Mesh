---
type: protocol
class: canon
state: unflagged
review_status: live
created: 2026/08/09
updated: 2026/08/12
tags:
  - protocol
  - tour
---

# TOUR STOPS

> The walk, in order. The Guide loads this before giving the tour, to know which rooms are stops, what each room's fork reveals, and which rooms are covered by a parent card.

> The walk table is the order; the folder map below is the territory — the mesh's one copy. `START_HERE.md` (Mesh root) points here, it does not repeat it.

---

## Folder map

```
./                             ← Mesh root — its README carries the stop-1 card
├── START_HERE.md              ← the entry work order, carried out on day one
├── README.md                  ← the root tour card
└── WORKSPACE/
    ├── MASTER_INDEX.md        ← doc index: rows are cron-owned, agents touch description fields only
    ├── AGENT_WORKSPACE/       ← the engine room: the agent team lives and works in here
    │   ├── AGENTS/            ← the seat machinery, four shelves
    │   │   ├── BOOTSTRAPS/    ← one startup file per seat
    │   │   ├── DESKS/         ← one inbox per seat, and the sweep that clears them
    │   │   ├── PROTOCOLS/     ← per-seat procedure shelves, run on demand
    │   │   └── SUB_AGENTS/    ← the single-shot hands a seat can spawn
    │   ├── RULES/             ← the rulebook every seat loads at spin-up
    │   ├── MEMORY_CARDS/      ← what a seat carries between sessions: ACTIVE, SESSION, STATIC
    │   ├── TEMPLATES/         ← the blank forms everything new is stamped from
    │   ├── BLUEPRINTS/        ← build molds — the folder shape each machine is poured into
    │   ├── REFS/              ← per-seat reference shelves: GUIDE, DIRECTOR, OVERSEER, CLIDE
    │   ├── PROJECTS/          ← the work: ACTIVE, PARKED, SIDE_QUESTS, GRAVEYARD
    │   ├── TRASH/Desk_Sweep/  ← one lifecycle: agents flag, the sweep moves; agents never delete
    │   └── STASIS/            ← the freezer: suspended docs and retired seats, kept not deleted
    └── OPERATOR_WORKSPACE/    ← the human's rooms: DESK, NOTES, ARCHIVE, CRONS, TOOLS
```

---

## The walk — 11 stops

| # | Stop | Fork reveals | Covers |
|---|---|---|---|
| 1 | `./` (Mesh root) | — | — |
| 2 | `WORKSPACE/AGENT_WORKSPACE/` | — | _containers_ `WORKSPACE/` `AGENTS/` · `STASIS/` |
| 3 | `AGENTS/BOOTSTRAPS/` | `RULES/` · `BOOTSTRAPS/CLIDE/` · `BOOTSTRAPS/DIRECTOR/` · `BOOTSTRAPS/GUIDE/` · `BOOTSTRAPS/OVERSEER/` · `AGENTS/SUB_AGENTS/` | — |
| 4 | `AGENTS/DESKS/` | `DESKS/DIRECTORS_DESK/` · `DESKS/GUIDES_DESK/` · `DESKS/OVERSEERS_DESK/` · `TRASH/Desk_Sweep/` | _container_ `TRASH/` |
| 5 | `MEMORY_CARDS/` | `MEMORY_CARDS/ACTIVE_MEMORY/` · `MEMORY_CARDS/SESSION_MEMORY/` · `MEMORY_CARDS/STATIC_MEMORY/` | — |
| 6 | `TEMPLATES/` | `TEMPLATES/Memory_templates/` · `TEMPLATES/PROJECT_template/` · `TEMPLATES/SIDE_QUEST_template/` · `TEMPLATES/BLUEPRINT_template/` | — |
| 7 | `AGENTS/PROTOCOLS/` | `PROTOCOLS/CLIDE/` · `PROTOCOLS/DIRECTOR/` · `PROTOCOLS/GUIDE/` · `PROTOCOLS/OVERSEER/` · `BLUEPRINTS/` | — |
| 8 | `REFS/` | `REFS/GUIDE/` · `REFS/DIRECTOR/` · `REFS/OVERSEER/` · `REFS/CLIDE/` | — |
| 9 | `PROJECTS/` | `PROJECTS/ACTIVE/` · `PROJECTS/PARKED/` · `PROJECTS/SIDE_QUESTS/` · `PROJECTS/GRAVEYARD/` | — |
| 10 | `OPERATOR_WORKSPACE/` | `OPERATOR_WORKSPACE/DESK/` · `OPERATOR_WORKSPACE/NOTES/` · `OPERATOR_WORKSPACE/ARCHIVE/` · `OPERATOR_WORKSPACE/CRONS/` · `OPERATOR_WORKSPACE/TOOLS/` | — |
| 11 | `WORKSPACE/MASTER_INDEX.md` | — | — |

---

## The dives — 58 rooms

> Reached only by taking a fork. Every row states the room it is reached from, so a dive card is never delivered out of place.

### Off stop 3 — `AGENTS/BOOTSTRAPS/`

| Room | Reached from | Fork reveals |
|---|---|---|
| `RULES/` | stop 3 | — |
| `BOOTSTRAPS/CLIDE/` | stop 3 | — |
| `BOOTSTRAPS/DIRECTOR/` | stop 3 | — |
| `BOOTSTRAPS/GUIDE/` | stop 3 | — |
| `BOOTSTRAPS/OVERSEER/` | stop 3 | — |
| `AGENTS/SUB_AGENTS/` | stop 3 | `SUB_AGENTS/OVERSEER/` |
| `SUB_AGENTS/OVERSEER/` | `AGENTS/SUB_AGENTS/` | — |

### Off stop 4 — `AGENTS/DESKS/`

| Room | Reached from | Fork reveals |
|---|---|---|
| `DESKS/DIRECTORS_DESK/` | stop 4 | — |
| `DESKS/GUIDES_DESK/` | stop 4 | — |
| `DESKS/OVERSEERS_DESK/` | stop 4 | — |
| `TRASH/Desk_Sweep/` | stop 4 | — |

### Off stop 5 — `MEMORY_CARDS/`

| Room | Reached from | Fork reveals |
|---|---|---|
| `MEMORY_CARDS/ACTIVE_MEMORY/` | stop 5 | `ACTIVE_MEMORY/GUIDE/` · `ACTIVE_MEMORY/DIRECTOR/` · `ACTIVE_MEMORY/OVERSEER/` |
| `ACTIVE_MEMORY/GUIDE/` | `MEMORY_CARDS/ACTIVE_MEMORY/` | — |
| `ACTIVE_MEMORY/DIRECTOR/` | `MEMORY_CARDS/ACTIVE_MEMORY/` | — |
| `ACTIVE_MEMORY/OVERSEER/` | `MEMORY_CARDS/ACTIVE_MEMORY/` | — |
| `MEMORY_CARDS/SESSION_MEMORY/` | stop 5 | `SESSION_MEMORY/GUIDE/` · `SESSION_MEMORY/DIRECTOR/` · `SESSION_MEMORY/OVERSEER/` |
| `SESSION_MEMORY/GUIDE/` | `MEMORY_CARDS/SESSION_MEMORY/` | — |
| `SESSION_MEMORY/DIRECTOR/` | `MEMORY_CARDS/SESSION_MEMORY/` | — |
| `SESSION_MEMORY/OVERSEER/` | `MEMORY_CARDS/SESSION_MEMORY/` | — |
| `MEMORY_CARDS/STATIC_MEMORY/` | stop 5 | `STATIC_MEMORY/GUIDE/` · `STATIC_MEMORY/DIRECTOR/` · `STATIC_MEMORY/OVERSEER/` |
| `STATIC_MEMORY/GUIDE/` | `MEMORY_CARDS/STATIC_MEMORY/` | — |
| `STATIC_MEMORY/DIRECTOR/` | `MEMORY_CARDS/STATIC_MEMORY/` | — |
| `STATIC_MEMORY/OVERSEER/` | `MEMORY_CARDS/STATIC_MEMORY/` | — |

### Off stop 6 — `TEMPLATES/`

| Room | Reached from | Fork reveals |
|---|---|---|
| `TEMPLATES/Memory_templates/` | stop 6 | — |
| `TEMPLATES/SIDE_QUEST_template/` | stop 6 | — |
| `TEMPLATES/BLUEPRINT_template/` | stop 6 | — |
| `TEMPLATES/PROJECT_template/` | stop 6 | `PROJECT_template/BUILD/` · `PROJECT_template/CLIDE/` · `PROJECT_template/REFS/` |
| `PROJECT_template/BUILD/` | `TEMPLATES/PROJECT_template/` | `PROJECT_template/BUILD/CODEBASE/` |
| `PROJECT_template/BUILD/CODEBASE/` | `PROJECT_template/BUILD/` | — |
| `PROJECT_template/CLIDE/` | `TEMPLATES/PROJECT_template/` | — |
| `PROJECT_template/REFS/` | `TEMPLATES/PROJECT_template/` | — |

### Off stop 7 — `AGENTS/PROTOCOLS/`

| Room | Reached from | Fork reveals | Covers |
|---|---|---|---|
| `PROTOCOLS/CLIDE/` | stop 7 | — | — |
| `PROTOCOLS/DIRECTOR/` | stop 7 | — | — |
| `PROTOCOLS/GUIDE/` | stop 7 | — | — |
| `PROTOCOLS/OVERSEER/` | stop 7 | — | — |
| `BLUEPRINTS/` | stop 7 | — | _container_ `BLUEPRINTS/OVERSEER/` |

### Off stop 8 — `REFS/`

| Room | Reached from | Fork reveals |
|---|---|---|
| `REFS/GUIDE/` | stop 8 | — |
| `REFS/DIRECTOR/` | stop 8 | — |
| `REFS/OVERSEER/` | stop 8 | — |
| `REFS/CLIDE/` | stop 8 | — |

### Off stop 9 — `PROJECTS/`

| Room | Reached from | Fork reveals |
|---|---|---|
| `PROJECTS/ACTIVE/` | stop 9 | — |
| `PROJECTS/PARKED/` | stop 9 | — |
| `PROJECTS/SIDE_QUESTS/` | stop 9 | — |
| `PROJECTS/GRAVEYARD/` | stop 9 | — |

### Off stop 10 — `OPERATOR_WORKSPACE/`

| Room | Reached from | Fork reveals |
|---|---|---|
| `OPERATOR_WORKSPACE/DESK/` | stop 10 | — |
| `OPERATOR_WORKSPACE/NOTES/` | stop 10 | — |
| `OPERATOR_WORKSPACE/ARCHIVE/` | stop 10 | `ARCHIVE/BACKUPS/` · `ARCHIVE/HISTORY/` · `ARCHIVE/REFS/` · `ARCHIVE/RESEARCH/` |
| `ARCHIVE/BACKUPS/` | `OPERATOR_WORKSPACE/ARCHIVE/` | — |
| `ARCHIVE/HISTORY/` | `OPERATOR_WORKSPACE/ARCHIVE/` | — |
| `ARCHIVE/REFS/` | `OPERATOR_WORKSPACE/ARCHIVE/` | — |
| `ARCHIVE/RESEARCH/` | `OPERATOR_WORKSPACE/ARCHIVE/` | — |
| `OPERATOR_WORKSPACE/CRONS/` | stop 10 | `CRONS/HEALTH/` · `CRONS/LOGS/` · `CRONS/SCRIPTS/` |
| `CRONS/HEALTH/` | `OPERATOR_WORKSPACE/CRONS/` | — |
| `CRONS/LOGS/` | `OPERATOR_WORKSPACE/CRONS/` | — |
| `CRONS/SCRIPTS/` | `OPERATOR_WORKSPACE/CRONS/` | — |
| `OPERATOR_WORKSPACE/TOOLS/` | stop 10 | `TOOLS/COMMANDS/` · `TOOLS/SCRIPTS/` |
| `TOOLS/COMMANDS/` | `OPERATOR_WORKSPACE/TOOLS/` | — |
| `TOOLS/SCRIPTS/` | `OPERATOR_WORKSPACE/TOOLS/` | — |

---

## Reading it

| Column | Means |
|---|---|
| Stop | a room on the main walk; its `README.md` carries a Tour Card, delivered verbatim |
| Room (dives table) | a room off the walk; its `README.md` carries a Dive Card, delivered only when the user takes that fork |
| Reached from | the room whose fork offers this one — a stop number, or the parent dive's path |
| Fork reveals | what this room's fork offers next. `—` means the fork offers continue only |
| Covers | rooms with no card of their own, spoken for by this one — not gaps |
| Covers — _container_ | a pass-through folder holding only other rooms; no card owed |

> One layer at a time. A stop's fork lists the rooms it covers; taking one of those dives delivers that card and forks again on the rooms below it. Continue always returns to the main walk, from any depth — the Guide holds no return path.

---

## Keeping it true

| Rule |
|---|
| A new room is a dive of the room above it unless it is promoted to a stop — add the row when the room is built, not later |
| A room with no card is a known gap, not a decision — it reads as unfinished until it has a card or a Covers entry |
| Order comes from the walk table; a room absent from the folder map above is invisible to the tour however good its card |
| The map above is the mesh's ONE copy — every other doc points here, never repeats it |
| Every path is written from a root the reader can resolve — never a bare leaf name, and never an abbreviation of a folder written in full elsewhere |
| Coverage is checkable: every folder in the seed appears here exactly once, as a stop, a dive, or inside a Covers cell |
| Promoting or demoting a room is not a header flip — any walk-order sentence in the parent card goes false the moment its children stop being stops |
