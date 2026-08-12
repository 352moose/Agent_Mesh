---
type: Infra
class: canon
state: unflagged
review_status: protected
created: 2026/03/22
updated: 2026/08/12 OV S105
tags:
  - conventions
  - infra
---

# Conventions

---

## Rules

- **Filename format** — each doc class carries its own; the tables below govern — ordered sequences, sent docs, fixtures, memory cards
- **Dates** — dashes in filenames (`YYYY-MM-DD`), slashes in frontmatter (`YYYY/MM/DD`)
- **Sequence numbers** (`_N`) — appended when multiple files of the same type and date exist
- **Casing** — ALL CAPS for folder names. Existing folders get updated at the point of edit or friction
- **Separators** — underscores between segments, dashes only inside dates
- **Numeric prefixes** — `N_NAME.md`, `N_FOLDER/`; ascending integers, no zero-padding; `0_` is the arrival/orientation slot, steps run from `1_`
- **READMEs** — `type: readme` carries `class: work` + `review_status: live`; folder orientation heals on contact, no review cycle

---

## Loop Phases

> The phase vocabulary for every bootstrap loop table.
> `TABLES.md` carries the skeleton.

| Phase     | Means                                                            |
| --------- | ---------------------------------------------------------------- |
| `Load`    | gather or assess before acting — list, check, read               |
| `Work`    | act — produce, change, or write something                        |
| `Gate`    | STOP; user confirmation                                          |
| `Report`  | surface a defined line to the user                               |
| `Fork`    | branch point ending the sequence — await direction, never assume |

---

## Permanent Fixtures

below are relative to AGENT_WORKSPACE/

### `AGENTS/BOOTSTRAPS/`

| Doc            | Pattern                                    | Location                      |
| -------------- | ------------------------------------------ | ----------------------------- |
| Seat bootstrap | `[XX]_BOOTSTRAP.md` — two-letter role code | `AGENTS/BOOTSTRAPS/[ROLE]/`   |
| Sub-agent      | `[NAME].md` — bare name, no suffix         | `AGENTS/SUB_AGENTS/[PARENT]/` |

### `MEMORY_CARDS/`

| Tier    | Location                 | Pattern                           | Rotated By                        |
| ------- | ------------------------ | --------------------------------- | --------------------------------- |
| Session | `SESSION_MEMORY/[ROLE]/` | `CURRENT_SESSION_[ROLE].md`       | Agent — cleared to blank at close |
| Static  | `STATIC_MEMORY/[ROLE]/`  | `[TAG]_S[N]_STATIC_YYYY-MM-DD.md` | Never rotated further             |
| Active  | `ACTIVE_MEMORY/[ROLE]/`  | `ACTIVE.md`                       | Never                             |

`[TAG]` = the role's boot code (`OV_BOOTSTRAP.md` → `OV`). `S[N]` = the session number the card closes, taken from the session file — never a per-day counter. Shape: `TEMPLATES/Memory_templates/Static_Card_template.md`.

### `PROJECTS/ACTIVE/[PROJECT]/`

Shape set by `TEMPLATES/PROJECT_template/` — folders: `BUILD/`, `CLIDE/`, `REFS/` (finished and superseded project docs rest in `REFS/ARCHIVE/`).

| Doc           | Pattern            | Location                                                          |
| ------------- | ------------------ | ----------------------------------------------------------------- |
| State         | `STATE.md`         | `BUILD/` — re-entry doc; carries the reading list, patterns, and §Conventions |
| Action Prompt | `ACTION_PROMPT.md` | `BUILD/` — single-step dispatch                                   |
| Action Report | `ACTION_REPORT.md` | `BUILD/` — session debrief, overwritten per step                  |
| Codebase maps | `BUGS.md` · `FEATURES.md` · `TWEAKS.md` | `BUILD/CODEBASE/` — bug ledger + parking lots |
| Executor card | `ACTIVE.md`        | `CLIDE/` — project-tied executor memory, not the house card       |
| PRD           | `PRD.md`           | `REFS/`                                                           |

---

*Last updated: 2026/08/12*
