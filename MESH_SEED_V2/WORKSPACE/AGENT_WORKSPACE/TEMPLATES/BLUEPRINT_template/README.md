---
type: readme
class: work
state: unflagged
review_status: live
created: 2026/08/12 OV S101
updated: 2026/08/12 OV S103
tags:
  - readme
  - blueprint
---

# BLUEPRINT_template

> A blueprint constrains the build into defined folders so the result stays human-parsable.

----

## Rules

| Rule                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| The template is subtractive just as much as it is additive — scale the stamp to the build                                                             |
| Names + syntax: literal = true                                                                                                                        |
| Build prompts are backwards-built from session logs — the log is evidence used to discover the steps, never the authority that defines their sequence |
| Installation establishes scope — the product declares its relationship to the tree it lives in                                                        |

----

## Separation of duty

> each layer its own shape and instruction tense.

| Layer | Is            | Reader  | Carries                                                               |
| ----- | ------------- | ------- | --------------------------------------------------------------------- |
| L1    | this template | you     | how to stamp a blueprint from the distillation                        |
| L2    | the blueprint | builder | primitive enough for an agent to speed-run its own generative process |


----

## Distillation

> logs → blueprint — stripping away historical vectors until only the irreducible shape of the product remains. Run against a completed software with a vault record.

| Phase  | DO                | Payload                                                               |
| ------ | ----------------- | --------------------------------------------------------------------- |
| Load   | Read              | cross reference project folder with session/legacy memory             |
| Work   | Extract pieces    | the pieces that explain the product, not the pieces found in the source → `FOLDER_TREE/` |
| Work   | Extract done      | output · interface · constraints, from what shipped → `DONE.md`       |
| Work   | Extract breaks    | only breaks still true under a completely different implementation → `GOTCHAS/[ROOM]/` — the break may be invariant, the fix merely one solution |
| Work   | Write steps       | one `STEP_N` per generative threshold — what becomes possible or legible after it, never "what happened next" |
| Gate   | Subtract          | scale the stamp to the build                                          |
| Report | Stamped blueprint | readable cold by a foreign stateless agent                            |

----



## `FOLDER_TREE/`

| Folders     | WHAT                                  | HOW                                                                          |
| ----------- | ------------------------------------- | ---------------------------------------------------------------------------- |
| `MODULES/`  | one folder per piece: spec + manifest | pairs by name with `PACKAGES/`; manifest = whatever form the stack can check |
| `PACKAGES/` | one folder per piece: ALL its code    | pour code only into a piece whose `MODULES/` pair exists                     |
| `APP/`      | the thin binding                      | compose declared pieces only                                                 |
| `BUILD/`    | rebuild script, logs, the product     | break → GOTCHAS filed to `AGENT/GOTCHAS/[ROOM]/`, never at the end           |
| `DATA/`     | one folder per family, self-stamped   | the piece that reads a source owns its pull code                             |

