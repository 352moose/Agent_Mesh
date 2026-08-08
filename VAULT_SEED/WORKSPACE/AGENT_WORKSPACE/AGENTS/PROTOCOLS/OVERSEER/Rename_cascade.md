---
type: note
scope: rename cascade
maintained_by: OVERSEER
created: 2026/08/08
review_status: protected
---

# RENAME CASCADE

> Fires when anything keeps its place but changes its name — a file, folder, seat, term, trigger phrase, or frontmatter value. The rename itself is the small half; the cascade — every place the old name is written — is the work. Never rename first and sweep later.

---

## The walk

| Step | Do |
|---|---|
| 1 | Freeze — nothing renamed yet. State `old name → new name` in one line, confirm with the user |
| 2 | Locate the canonical home: the template, contract file, or definition the name LIVES in. Written in N docs but defined in one = the rename lands at the definition first |
| 3 | Sweep the whole tree for the old name — file contents AND filenames, no result cap. Filename-only search misses contents; run both |
| 4 | Build the census: every hit by filename, classified (table below). Live hits are the census; never build it from a hit count |
| 5 | Rename at the canonical home |
| 6 | Fan out per `Cascade_fan_out.md` — slice the census across instances primed with `old → new` and one correction class: repoint the reference, touch nothing else |
| 7 | Verify: re-sweep the old name — only fossils and coincidences remain; spot-check that the new name resolves where it is consumed (wikilinks, PATHS rows, scripts) |

---

## Classifying hits

| Class | Test | Action |
|---|---|---|
| Live | a reader or script follows it today | repoint |
| Fossil | sits in a fossil tree — the list is in `Cascade_fan_out.md` | leave — old names in history are expected, not drift |
| Coincidence | same string, different meaning | leave |

---

## Hard rules

| Rule |
|---|
| A name copied into N docs is the defect, not just the cascade — flag for one contract home + pointers while you are in there |
| Scripts and cron lines that match on the old name break silently — they are hits, check them explicitly |
| The user actively editing the tree = re-check disk state immediately before every batch |
