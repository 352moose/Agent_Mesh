---
type: Infra
class: canon
state: unflagged
review_status: protected
created: 2026/08/09
updated: 2026/08/11 OV S99
tags:
  - protocol
  - overseer
---

# FORMATTING CHANGE CASCADE

> Fires when the SHAPE of a doc class changes — a frontmatter field, a table layout, a naming pattern, a section structure. One doc changing shape is an edit; a class changing shape is a cascade, and it lands template-first. Never patch instances one by one and let the template drift.

---

## The walk

| Step | Do |
|---|---|
| 1 | Freeze — name the change and the doc class it touches in one line, confirm with the user |
| 2 | Find the governing template — the change lands THERE first. No template governs the class = stop and settle that with the user (build one, or rule it a one-off with no cascade) |
| 3 | Land the change in the template, walking the user through the standard as you go — flexible on the change itself, rigid on propagation |
| 4 | Census the class: every live instance carrying the shape, listed by filename. Fossils are ignored — they keep the old shape |
| 5 | Fan out per `CASCADE_exe.md` — slice the census across instances primed with the NEW template, one correction class named. Never walk the class yourself file by file |
| 6 | Review the returned diffs before they stand — sections or rows the user deliberately cut from an instance stay cut; a relay pass never re-adds them |
| 7 | Verify: conformance sweep across the class. Frontmatter is the likeliest victim — check it field by field; any field automation consumes must be present and typed, never prose |

---

## Propagate now, or let it heal?

Not every shape change earns a cascade. Classify the drift before spending one.

| Drift | Cost of leaving it | Handling |
|---|---|---|
| A dead POINTER — path, name, or doc that no longer exists | it misleads whoever reads it | cascade now |
| A SHAPE difference — column renamed, row added, order changed | nothing breaks; the instance still works | **let it heal on contact** — the template is the source, instances conform next time they are touched |

> Operator ruling: *"if the template is updated, the agents will get their updates next time they get an update. it will heal itself with friction."* A propagation machine built where contact would do is waste.

> Anchored by *Instances Conform on Contact*.

---

## The correction class

Name ONE per fan-out. A class that is really three gets three passes, not one instance told to fix everything.

| Class | The instance corrects |
|---|---|
| Frontmatter | the block's fields against the template — correct fields only, body untouched |
| Table shape | column set, header row, alignment — cell content untouched |
| Section structure | headings present, ordered, nested as the template has them |

> Frontmatter is the likeliest victim of a shape change and the one automation actually reads — a sweep, sentinel, or watcher that consumes a field finds it missing or untyped and fails silently. Run it first, verify it hardest.

---

## Verifying a table-shape change

| Rule |
|---|
| Count columns per table INCLUDING the separator row — a checker that skips a row class is blind to damage in that class |
| Scope a repair regex to one table; `re.M` across a whole file hits every table sharing the shape |
| A column identical on every row is documentation of a standard, not data — the change may be to drop it |

---

## Hard rules

| Rule |
|---|
| Template-first is the law even for a one-field change — an instance patched ahead of its template is drift you authored |
| A reference cascade (repointing stale pointers) is NOT a pattern migration (reshaping sibling fixtures) — reshaping siblings that still conform is scope creep, stop at the ask |
| The user actively editing the class = re-check disk state immediately before every batch |
