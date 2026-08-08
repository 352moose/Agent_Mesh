---
type: note
scope: cascade fan out
maintained_by: OVERSEER
created: 2026/08/08
review_status: protected
---

# CASCADE FAN OUT

> The shared engine of every cascade protocol. A cascade has a census — every file the change touches — and a correction that is the same mechanical act on each one. That is fan-out work, not a walk. The Overseer slices the census across primed sub-agents, reviews what comes back, and keeps the judgement calls.

> Loaded BY the cascade protocols (rename, move, formatting change), not on its own. They decide what the census is; this decides how it gets worked.

---

## Why not walk it

| Walking it yourself | Fanning it out |
|---|---|
| Attention decays down a long list — the last files get less than the first | every file gets a fresh instance |
| Your context fills with file bodies, and the cascade stalls half done | your context holds the plan and the diffs |
| The correction drifts as you go — file 30 is not shaped like file 3 | one template, one correction class, applied identically |

---

## The primed instance

Spawn `../../SUB_AGENTS/OVERSEER/RELAY.md` — one per slice, in parallel. Single-shot, scoped, no memory: the completion report IS its memory, and it carries no state to the next file or the next slice.

| Prime with | Why |
|---|---|
| The governing template or the new form, in full | it is the conformance baseline — never a summary of what changed |
| Its slice of the census, by filename | explicit targets; no discovery, no wandering the tree |
| One correction class, named | frontmatter fields, or a repointed path, or table shape — not "make it conform" |
| The diff-back requirement | it reports what it changed; it does not get the last word |

| Bound | Rule |
|---|---|
| Scope | only the named correction class — everything else in the file is untouched |
| Cap | 5 files per instance. A bigger census means more slices, never a bigger slice |
| Investigation | read-only; the correction class bounds every write |
| Ambiguity | stop and report, never guess — judgement calls come back to the Overseer |
| Approval | anything needing user approval is surfaced, never executed |

---

## Ignored, always

Fossil trees keep the old form — they are the record of what was, and correcting them destroys it.

`ARCHIVE/` · `BACKUPS/` · `TRASH/` and sweeps · `PARKED/` · `GRAVEYARD/` · static memory cards · session logs

> A census that includes fossils is a census built wrong — fix the census, never prime an instance to skip them.

---

## Review

The diffs come back to you, and they do not stand until you have read them.

| Check |
|---|
| The correction landed, and nothing outside its class moved |
| Rows or sections the user deliberately cut stay cut — a cascade never re-adds them |
| Reported ambiguities get YOUR ruling, then a re-run of that slice — never a silent pass |
| Anything an instance surfaced instead of executing goes to the user, with what it found |
