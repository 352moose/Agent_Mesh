---
type: note
scope: CD_DISTILL
maintained_by: OVERSEER
created: 2026/08/08
review_status: protected
---

# CD_DISTILL

> Syntax-layer compression. Turns text that grew by appending steps one at a time — into its **carry-forward**: the rule or state a cold reader needs, in the fewest tokens. A logic equation where one exists; never more than a line.

> Operates on the words inside an entry, not the doc's architecture. A living doc's control table already says WHEN to compress (the `Hygiene` column) and HOW MUCH (the `CAP`). This protocol is the HOW: the syntax-layer act of shrinking content to fit, not restructuring the shell.

---

## Fires here

- The ACTION_REPORT back to the Director: what happened, what changed, what is open — the report IS this seat's memory
- The project ACTIVE card: facts that survive the cycle, one line each
- No session close fires here — this seat is single-shot; distill when the report is written

---

## Fit

**Where it fires in a living doc** — a section's `Hygiene` column: `fold into Consolidated Memory` · `consolidate` · `evict, keep the carry-forward`. The Session Log → Consolidated Memory fold ("compressed summaries, facts, no prose") is the canonical case.

---

## The diagnosis

A changelog / memory / workflow = appending steps one at a time. It records the **path** (how we got here). A reader needs the **destination** (where we are + the rule that holds). The path was scaffolding; it comes down once the building stands.

`log = path` · `carry-forward = state + rule` → keep the second, drop the first.

---

## What survives

Preserve what was accomplished / flagged / decided / carries forward;
*Discard* recaps, health checks, confirmations, preamble. Then apply one test, per surviving token: **would a cold reader act differently without it?** No → cut. Then push the survivors past bullets into operators.

| Keep | Cut |
| ---- | --- |
| the rule / the state | the sequence of steps that reached it |
| the reason that makes the rule safe to apply (`∵`) | dates-in-prose, "we then / turned out / basically" |
| the one number that matters, the tally, the lineage | hedges, restated context |
| operators (`→ ∧ ∵ > = ¬`) | the subject when it never changes |

---

## Syntax layer

| # | Attack | From → To |
| - | ------ | --------- |
| 1 | Log → invariant | N trials converging on a rule become the rule. `tried A (broke), B worked ∵ C` → `B not A ∵ C` |
| 2 | Prose → operator | connective sentences → notation (lexicon below) |
| 3 | Sequence → delta | `did a, b, c, ended at S` → `S (was S₀)` |
| 4 | Instances → pattern + tally | `happened S38; again S44` → `<rule> [2×]` |
| 5 | Strip scaffolding | delete non-load-bearing tokens; keep nouns · verbs · operators · the number |

---

## Operator lexicon — prose → logic

| Prose | Logic |
| ----- | ----- |
| when X, do Y | `X → Y` |
| A only if B, C, D all hold | `A ⟵ B ∧ C ∧ D` |
| X, therefore Y | `X ∴ Y` |
| Y because Z | `Y ∵ Z` |
| prefer X over Y | `X > Y` |
| X replaces Y (Y retired) | `Y → X` |
| not X; instead Y | `¬X; Y` |
| X is defined as Y | `X = Y` |
| over cap, drop oldest | `>cap → evict oldest` |

> Use only symbols this legend defines — the lexicon is the legend. An equation the reader can't parse is not compression, it's a cipher.

---

## Output ladder

0. **Key-point bullet**
1. **A few words** — the rule as a fragment
2. **One line** — subject · verb · object, no subordinate clauses
3. **Equation / relation** — `X → Y`, `A = B ∵ C`

Never more than a line.

---

## Example

| Before (log) | After (carry-forward) |
| ------------ | --------------------- |
| "S38 I didn't log incrementally, so at close I rebuilt the card from full context — painful. S44 it happened again, rebuilt from context." | `log incrementally ∵ close-reconstruction is the cost [2×]` |
| "Considered bumping the schema literal to /3, but it's feature-tied and re-drifts at /4, so we removed the literal and cite the live source." | `pinned version drifts → cite live source, never a literal` |
| "When a section passes its cap, drop the entry with the lowest tally; if tallies tie, drop the oldest one." | `>cap → evict min(tally), ties → oldest` |

---

## Anti-patterns

| Don't                                   | Why                                                                                                  |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Compress a live log mid-append          | carry-forward hasn't crystallized — distill at the cap / at close                                    |
| Drop the reason                         | a rule without its `∵` gets misapplied; compress the narrative, keep the logic                       |
| Blur two carry-forwards to hit one line | two lines beat one false merge; but if two instances = a single truth, the single truth will suffice |
| Invent private notation                 | reader can't parse it → not compression                                                              |
| Lose the tally / lineage                | the living doc's ruleset tracks it — carry it forward                                                |
| Add words                               | the goal is fewer tokens, not better prose                                                           |

---

## The meta-rule

This protocol obeys its own rule. If a line here can be shorter, shorten it.
