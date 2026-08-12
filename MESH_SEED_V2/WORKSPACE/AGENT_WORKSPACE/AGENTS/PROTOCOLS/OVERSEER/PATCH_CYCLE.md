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

# PATCH CYCLE

> The loop for every patch on a file the operator will edit: stage a copy, hand it over, diff what comes back, promote on their word, verify the write. Load it when the patch STARTS — not when damage appears.

> Assume no undo. The staged copy IS the undo, and it has to exist before the write.

> Not `CASCADES/Changing_infra_docs.md` — that propagates a deliberate shape change across a doc class. This is one file, one patch, one operator.

---

## The cycle

| Step | Do |
|---|---|
| 1 | Read the target in full before staging. A damage class you have not seen cannot be separated from intent |
| 2 | Stage `[FILENAME]_PATCH.md` beside the original — the baseline every later diff is taken against |
| 3 | Hand it over. The operator edits the patch directly; expect content changes and editor damage in the same pass |
| 4 | On return, classify every difference: operator intent, or editor damage. Ambiguous = ask, never guess |
| 5 | Diff staged against original and show it **before** any overwrite |
| 6 | Report: damage fixed · content preserved · anything ambiguous and how it was handled |
| 7 | On the operator's word, overwrite the original. Protected fixtures promote here and nowhere earlier |
| 8 | Verify the write — re-run the damage sweep on the RESULT, not on the staged copy |

---

## Damage classes — check on the return leg

Markdown editors (Obsidian and the like) reflow tables and whitespace on save. Operator edits arrive mixed with these.

| Damage | What it looks like |
|---|---|
| Emptied rows | cells blanked, row kept — `\| \|` or `\| \| \|` between real rows. Sweep with `grep -E '^\|( +\|)+$'` |
| Phantom column | an extra `\| \|` appended to every row of one table |
| Truncated separator | the `\| --- \|` row carries fewer columns than the header — invisible when rendered, breaks the table |
| Collapsed divider | `---` jammed against content with no blank line |
| Mangled whitespace | indentation stripped or added, blank lines removed |
| Dangling clause | a deletion leaves its punctuation — an orphan `(`, a half-sentence, a trailing conjunction |

---

## Verification

| Rule |
|---|
| State the checker's scope as what the CONSUMER parses, never as what you edited — the fence that follows a card heading, not every fence in the file; the full row set, not the rows you touched |
| Count columns per table **including the separator row** — a checker that skips a row class is blind to damage in that class |
| Match the threshold to the spec's own words — a hard limit tested against a soft `~` figure manufactures findings |
| A name matched anywhere is not a name matched somewhere — resolve a relative token against its own parent before claiming a hit |
| A repair regex is scoped to one table; `re.M` across a whole file hits every table that shares the shape |
| Restoring from a pre-edit copy re-creates the defect you were fixing — restore the untouched rows, not the damaged one |
| A promoted file carries no `_PATCH` scaffolding: patch-notes blocks and `status: test_patch` come off at step 7 |

---

## Hard rules

| Rule |
|---|
| Never change the operator's content — formatting only |
| Cannot tell damage from intent → ask |
| Show the diff before overwriting, always |
| Target has a JSON mirror or companion doc → update it after approval |
| Edits alternate — exactly one editor in the file at any moment; the other's hands stay off until "done" |
| One contiguous pass per doc, announce done, stay out — edit → wander → return is the clobber shape; re-enter only on a fresh go |
