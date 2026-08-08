---
type: note
scope: formatting change cascade
maintained_by: OVERSEER
created: 2026/08/08
review_status: protected
---

# FORMATTING CHANGE CASCADE

> Fires when the SHAPE of a doc class changes — a frontmatter field, a table layout, a naming pattern, a section structure. One doc changing shape is an edit; a class changing shape is a cascade, and it lands template-first. Never patch instances one by one and let the template drift.

---

## The walk

| Step | Do |
|---|---|
| 1 | Freeze — name the change and the doc class it touches in one line, confirm with the user |
| 2 | Find the governing template — the change lands THERE first. No template governs the class = stop and settle that with the user (build one, or rule it a one-off with no cascade) |
| 3 | Census the class: every live instance carrying the shape. List by filename and eyeball — never bulk-edit from a grep count |
| 4 | Land the change in the template, walking the user through the standard as you go — flexible on the change itself, rigid on propagation |
| 5 | Relay template → instances in batches, diffing each batch. Sections or rows the user deliberately cut from an instance stay cut — a relay pass never re-adds them |
| 6 | Fossil exemption: ARCHIVE, BACKUPS, TRASH, PARKED, GRAVEYARD, static cards keep the old shape |
| 7 | Verify: conformance sweep across the class; any field automation consumes (sweep, sentinel, watcher) must be present and typed in frontmatter — never prose |

---

## Hard rules

| Rule |
|---|
| Template-first is the law even for a one-field change — an instance patched ahead of its template is drift you authored |
| A reference cascade (repointing stale pointers) is NOT a pattern migration (reshaping sibling fixtures) — reshaping siblings that still conform is scope creep, stop at the ask |
| The user actively editing the class = re-check disk state immediately before every batch |
