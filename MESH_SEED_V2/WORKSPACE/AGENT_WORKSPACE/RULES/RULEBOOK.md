---
type: Infra
class: canon
state: unflagged
review_status: protected
created: 2026/03/24
updated: 2026/08/10 OV S93
tags:
  - rulebook
  - infra
---

# RULEBOOK

> Mandatory operating rules for every agent.

> Markdown editors (Obsidian and the like) may reformat tables and whitespace on save — this can break edit-tool match strings on subsequent edits. Filename-search tools match glob patterns on filenames only, not file contents.

---

## TOOLS

| Rule                                                           |
| -------------------------------------------------------------- |
| Test your CLI tools first, MCP is a fallback                   |
| `head` / `tail` = partial reads                                |
| `read_multiple_files` = batch reads                            |
| `get_file_info` before reading large or unknown files          |
| use sub agent to scout large docs for line exact block edits   |
| `dryRun: true` = match uniqueness uncertain                    |
| emoji = false                                                  |
| trash = `AGENT_WORKSPACE/TRASH/` — build/use labeled subfolder |
| sweep = AGENT_WORKSPACE/TRASH/Desk_Sweep/[AGENT]/              |
| stasis = `AGENT_WORKSPACE/STASIS/` — frozen agent docs         |

---

## AGENT RULES

| Rule                                                                          |
| ----------------------------------------------------------------------------- |
| Before overwrite show the diff, wait for approval                             |
| Set `review_status: pending_review` on most files sent to a desk              |
| When a silent gate triggers, execute the procedure then report result to user |

---

## NAVIGATION

### Vault Root

The `WORKSPACE/` folder containing `AGENT_WORKSPACE/`. Every path in this vault is relative to the file that states it — no absolute paths, resolve against this folder's location on this machine.

### List_directory on spin up:

- `AGENT_WORKSPACE/`
- `RULES/`
- `AGENTS/`

### MASTER_INDEX

`WORKSPACE/MASTER_INDEX.md` (vault root) — vault-wide doc index.

| Rule                                                                                             |
| ------------------------------------------------------------------------------------------------ |
| Unsure where a doc lives → spin up a sub-agent to search MASTER_INDEX, return path + description |
| Index rows updated by cron only; agents update description fields when touched                   |

---

## PROTOCOLS

`AGENTS/PROTOCOLS/[ROLE]/` — per-seat procedure shelf.

| Rule                                                                                          |
| --------------------------------------------------------------------------------------------- |
| Discover by listing the folder — filenames state purpose — keep list in context at all times |
| Any adjacent overlap with a filename's subject fires that protocol — uncertain = load         |
| Load it in full, never run a protocol from memory                                             |
| Load it before your first action on the work it governs                                       |
| A damage-triggered protocol loads at discovery                                                |

---

## MEMORY PROTOCOL

### Session Memory

File: `AGENT_WORKSPACE/MEMORY_CARDS/SESSION_MEMORY/[ROLE]/CURRENT_SESSION_[ROLE].md`

| Rule                                                                      |
| ------------------------------------------------------------------------- |
| spin up = load session memory, follow page rules                          |
| during session = append → disclose context = N%               |
| session close = clear session memory via page rules and build static card |

### Static Cards

Destination: `AGENT_WORKSPACE/MEMORY_CARDS/STATIC_MEMORY/[ROLE]/`

| Rule                                      |
| ----------------------------------------- |
| Build from own session section at close   |
| Ship with `review_status: pending_review` |

---

## FRONTMATTER

> Every doc carries the 7-field block — every field written out, no eighth field. Values, classes, and reasons: [[PROPERTIES]] at `RULES/PROPERTIES.md`.

```yaml
type:
class:
state:
review_status:
created:
updated:
tags:
```

---

## DELEGATION

Delegation = route the work to the agent built for it instead of doing it yourself.
Escalation = "I'm stuck, someone needs to decide."

| Class | What | Ships as |
|---|---|---|
| Work order | known job for another seat, filed openly | `type: work_order` · `review_status: pending_review` |
| Silent work order | auto-filed on a standing trigger, no operator prompt | `type: work_order` · `review_status: pending_review` until watcher crons run |
| Watcher work order | claimed and pre-investigated by the receiving desk's watcher — roadmapped, cron unimplemented | rail: `watcher_pending` → `watcher_claimed` → `pending_review` brief |

### How to File

| Step | Do                                                                             |
| ---- | ------------------------------------------------------------------------------ |
| 1    | Write the order to the receiving agent's desk using standard format [[PROPERTIES]] |
| 2    | Include: what, exact paths, exact specs, where to put the result               |

### Routing Table

| Situation                            | Route To | Ships as          |
| ------------------------------------ | -------- | ----------------- |
| Stale path found in a doc            | Overseer | silent work order |
| Bootstrap needs overhaul             | Overseer | work order        |
| Cross-agent consistency check needed | Overseer | work order        |

### Notes on Notice

| Rule                                                                                       |
| ------------------------------------------------------------------------------------------ |
| Cross-lane observation → typed note to the owning desk, same session, no operator prompt   |
| Flip the noticed doc's `state` to `flagged`, file the note — don't surface                 |
| Just flag it — the note carries the observation and a pointer, not an investigation result |
| The flag is the handoff: the receiving desk's watcher or next session handles the rest     |
| Telling the user is not delegation — the note still gets filed                             |
| Sent note gone? = absorbed / executed --> marked sweep --> swept by cron                   |

---

## DOCUMENTATION

### Receiving Agent Procedure

| Step | Rule                                                                                               |
| ---- | -------------------------------------------------------------------------------------------------- |
| 1    | Read: mark `review_status: sweep`.                                                                 |
| 2    | on user approval only; log a live, dispatchable follow-up to the receiving desk as a work order |

### Naming

| Rule |
|---|
| Desk files: `[CATEGORY]_YYYY-MM-DD_N.md` |
| CATEGORY in ALL CAPS — matches `type` value |
| Dates: dashes in filenames (`YYYY-MM-DD`), slashes in frontmatter (`YYYY/MM/DD`) |
| Every other doc class carries its own pattern — see the full reference |

> Full reference: [[CONVENTIONS]] at `AGENT_WORKSPACE/RULES/CONVENTIONS.md`.

---

*Last updated: 2026/08/11*
