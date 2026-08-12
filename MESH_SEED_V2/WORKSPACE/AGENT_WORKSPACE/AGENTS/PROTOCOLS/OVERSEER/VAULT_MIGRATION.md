---
type: Infra
class: canon
state: unflagged
review_status: protected
created: 2026/08/12 OV S106
updated: 2026/08/12 OV S106
tags:
  - protocol
  - overseer
---

# VAULT MIGRATION

> Migrates an older install (any prior seed version) onto this one. Load in full when an update is the work — the operator points at the old install, this protocol governs everything after.

> **The old install is read-only for the entire protocol.** Every carry is a COPY out of it; nothing in it is edited, moved, or deleted. It stays whole until the operator retires it themselves. This is the law the whole protocol exists to enforce — working docs survive the update because the update cannot touch them.

> Not `CASCADES/Moving_docs.md` — that moves docs inside one live tree. This pulls docs across trees, old install to new.

---

## What carries, what doesn't

| Class | Verdict |
|---|---|
| MEMORY_CARDS — static, active, session | carries — the mesh's memory is the operator's work |
| PROJECTS — active, parked, side quests, graveyard | carries whole, folder per folder |
| Desk contents — notes, work orders, open jobs | carries |
| OPERATOR_WORKSPACE — archive, notes, desk, tools | carries |
| REFS content the operator authored | carries |
| Boots, RULES, TEMPLATES, PROTOCOLS, SUB_AGENTS, cron scripts | **never** — the new seed's versions are the point of updating |

A doc that mixes classes (operator writing inside a canon fixture) is not obvious — it quarantines.

---

## The procedure

| Step | Do |
|---|---|
| 1 | Stand the new seed up fresh, beside the old install — never over it. Both trees exist in full before any carry |
| 2 | Census the old install: walk its whole tree, list every doc in the carries classes above. The census count is the number every later step reconciles against |
| 3 | Create `AGENT_WORKSPACE/UPDATE_INTAKE/` in the new tree, with `LEDGER.md` inside — one row per quarantined doc: origin path · why unsure |
| 4 | Place the obvious: a doc whose V2 home is unambiguous copies to that address and heals on contact — 7-field frontmatter, re-anchored paths, current vocabulary. Content is never rewritten, only conformed |
| 5 | Quarantine the rest: any doc whose home, class, or liveness is uncertain copies WHOLE into `UPDATE_INTAKE/` — no conforming, no renaming, ledger row filed. Unsure is a verdict, not a failure |
| 6 | Reconcile: placed + quarantined = census count. A doc unaccounted for is a stop, not a footnote |
| 7 | Verify the old install is byte-identical to its pre-update state, and report: census count · placed · quarantined with ledger · old install untouched |
| 8 | Hand over. The operator empties `UPDATE_INTAKE/` at their own pace — each doc placed or trashed by their hand. Empty intake = update complete. Retiring the old install is theirs alone |

---

## Hard rules

| Rule |
|---|
| Copy, never move — the old install is not a source that drains, it is a record that persists |
| Unsure is never guessed — a wrong placement corrupts the new tree, a quarantined doc costs one operator minute |
| Nothing silently dropped — every censused doc lands placed or in the ledger; the reconcile proves it |
| Canon never carries — an old boot or rule imported over a new one reintroduces the version being escaped |
| The intake folder is emptied by the operator only — an agent placing FROM quarantine defeats the quarantine |
| Old install retirement is an operator act, on their word, after the intake is empty — never part of this protocol |
