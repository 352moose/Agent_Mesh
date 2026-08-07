---
type: rulebook
created: 2026/08/05
review_status: protected
---

# RULEBOOK

> Standing rules for every seat in this mesh. Small by design: most protocol is taught where it is first used — this page holds only the invariants every seat must share.

---

## PATHS

| Rule |
|---|
| Every address in every mesh file is relative to the file that states it — resolve from that file's location |
| Never write an absolute or machine-specific path into a mesh file |

---

## DESK PROTOCOL

> Agents communicate by typed files on desks — never by relaying chat. Desks live at `../DESKS/[ROLE]S_DESK/`; the human's desk is `../../../OPERATOR_WORKSPACE/DESK/`.

### Frontmatter — every file sent to a desk

```yaml
---
type:              # note | report | work_order | audit | other
from:              # sending seat
to:                # receiving seat
created:           # YYYY/MM/DD
review_status:     # see lifecycle below
---
```

Permanent desk fixtures — READMEs and `_OPEN_JOBS_` — are furniture, not deliveries: they carry `scope` + `maintained_by` in place of `from`/`to`, and `review_status: protected`.

### Naming

| Rule |
|---|
| Pattern: `[TYPE]_YYYY-MM-DD_N.md` — type in caps matching frontmatter, date with dashes, N counting up within the day |
| Dates: dashes in filenames (`YYYY-MM-DD`), slashes in frontmatter (`YYYY/MM/DD`) |

### review_status lifecycle

| Value | Meaning | Set by |
|---|---|---|
| `pending_review` | Needs the receiver's read | Sending seat |
| `sweep` | Absorbed — scheduled for removal | Receiving seat |
| `protected` | Permanent fixture — never swept | Owner |

| Rule |
|---|
| Receiving a file = read it, act on it, flip it to `review_status: sweep` |
| Agents flag, never delete — the sweep moves flagged files to `../../../TRASH/Desk_Sweep/` |

---

## MEMORY PROTOCOL

> Each seat owns three cards under `../MEMORY_CARDS/`. CLIde is the exception: single-shot executor, no seat cards — its memory is project-tied (`../../PROJECTS/ACTIVE/[PROJECT]/BUILD/CLIDE/ACTIVE.md`).

| Card | Path pattern | Discipline |
|---|---|---|
| ACTIVE | `ACTIVE_MEMORY/[ROLE]/ACTIVE.md` | Living doc — section caps and rotation per the control tables on the card. Read at every spin-up, updated before close |
| Session | `SESSION_MEMORY/[ROLE]/CURRENT_SESSION_[ROLE].md` | Running scratch — append during the session, never overwrite prior entries |
| Static | `STATIC_MEMORY/[ROLE]/[ROLE]_SESSION_YYYY-MM-DD_N.md` | At close: distill the session file into one static card, then reset the session file to empty |

---

## WRITE DISCIPLINE

| Rule |
|---|
| A seat maintains its own cards, its own desk, and the `protected` fixtures it owns directly; anything owned by another seat = show the diff, wait for user approval |
| Unsettled decisions land as open items in the owning doc — never guessed prose |
| Automation is staged by agents but installed and owned by the user, in `../../../OPERATOR_WORKSPACE/` (CRONS, TOOLS) — agents never own scheduled execution |
