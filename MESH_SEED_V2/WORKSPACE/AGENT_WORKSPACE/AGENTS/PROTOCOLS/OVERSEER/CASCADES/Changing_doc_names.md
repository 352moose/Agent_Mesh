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
| 6 | Fan out per `CASCADE_exe.md` — slice the census across instances primed with `old → new` and one correction class: repoint the reference, touch nothing else |
| 7 | Verify: re-sweep the old name — only fossils and coincidences remain; spot-check that the new name resolves where it is consumed (wikilinks, PATHS rows, scripts) |

---

## Census on the token that CHANGES

> The load-bearing distinction, and the one that has cost a full fan-out: sweep what the change actually alters, never the name that survives it.

| Change | Token that changes | Token that survives |
|---|---|---|
| File renamed | the filename | the role or concept named inside it |
| Seat retired | its paths and rows | its NAME — history keeps saying it |
| Term redefined | the definition site | the word itself |

A census built on the surviving token returns zero in-class targets by construction. A deliberate quotation of the OLD string is the mirror case — it looks like a hit, and repointing it destroys the quote.

---

## Classifying hits

| Class | Test | Action |
|---|---|---|
| Live | a reader or script follows it today | repoint |
| Fossil | sits in a fossil tree — the list is in `CASCADE_exe.md` | leave — old names in history are expected, not drift |
| Provenance | records WHERE a ruling came from — an attribution, a citation, a consolidated-memory era name | leave — deleting it erases why the rule exists |
| Coincidence | same string, different meaning | leave |

> A rename leaves dead pointers ∴ this cascade runs now — the stated exception under *Instances Conform on Contact*. A SHAPE change is the other branch: `Changing_infra_docs.md`.

---

## Hard rules

| Rule |
|---|
| A name copied into N docs is the defect, not just the cascade — flag for one contract home + pointers while you are in there |
| Scripts and cron lines that match on the old name break silently — they are hits, check them explicitly |
| The user actively editing the tree = re-check disk state immediately before every batch |
