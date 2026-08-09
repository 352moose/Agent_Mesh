---
type: blueprint_procedure
name: Snake — tutorial project
created: 2026/08/09
updated: 2026/08/09
review_status: protected
---

# Procedure — Gates, Forks, and Why

> Three Director→CLIde cycles. The Director never writes the game; it writes one `ACTION_PROMPT` per cycle, reads the `ACTION_REPORT` that comes back, and lets the user's own play decide whether the cycle closed.

---

## How to Read a Step

| Element          | Meaning                                                                      |
| ---------------- | ---------------------------------------------------------------------------- |
| Gate             | a question about THIS machine — answer it before continuing                  |
| Fork             | the branch taken for one answer; each fork carries its own steps             |
| Step             | what was done, and the reason it was done that way                           |
| No matching fork | reason it out, build it, then author the gate here        |

> Every fork below is **authored and unproven** — `MACHINES.md` is empty. Whichever one you take, you are the first, and recording it is part of the build.

---

## Gates

### Gate 1 — What stack does the user actually want?

| Fork | Condition | Machines run | Steps |
| ---- | --------- | ------------ | ----- |
| A | The user has a stated language or framework preference | 0 | below |
| B | No stated preference | 0 | below |

**Fork A**

| # | Do | Why |
| - | --- | --- |
| 1 | Build on their stack, and translate every cycle's acceptance below into that stack's equivalent | The tutorial's job is to teach the workflow, not a language. A user watching the loop run in a stack they already read is learning one thing instead of two |
| 2 | If the stack has no GUI path on this machine, say so before starting and offer fork B | A tutorial that cannot open a window loses the property that makes it a good tutorial |

**Fork B**

| # | Do | Why |
| - | --- | --- |
| 1 | Use `python3` with the Tk toolkit from the standard library | Both ship with the interpreter on macOS and most Linux desktops, so nothing is installed and the audit's "no remote code" result stays true |
| 2 | Confirm a window can actually open before cycle 1 — a headless or SSH-only session cannot run this | Discovering this in cycle 1 costs the user their first impression of the loop |

### Gate 2 — Where does the project folder live?

| Fork | Condition | Machines run | Steps |
| ---- | --------- | ------------ | ----- |
| A | First spin-up — the pre-placed project folder is still unclaimed | 0 | below |
| B | Any later run | 0 | below |

**Fork A**

| # | Do | Why |
| - | --- | --- |
| 1 | Rename `PROJECTS/ACTIVE/First Project (overwrite in place)/` and fill it in place | The seed pre-copied it for exactly this. Copying the template again would leave an unclaimed folder sitting in ACTIVE forever |

**Fork B**

| # | Do | Why |
| - | --- | --- |
| 1 | Copy `AGENTS/TEMPLATES/PROJECT_template/` into `PROJECTS/ACTIVE/`, never move it | Moving the template removes the shape every future project is stamped from |

---

## The Three Cycles

> One `ACTION_PROMPT` per cycle. The user's play is the acceptance test — never the report.

| Cycle | CLIde builds | The user's check | Why this cut |
| ----- | ------------ | ---------------- | ------------ |
| 1 | A window opens; a snake moves under the arrow keys. No food, no score, no death | Launch it, steer it, report back | The smallest thing that is unmistakably alive. If the loop is broken, the user finds out on the cheapest possible cycle |
| 2 | Food, growth, a visible score, and death on self-collision | Play a round, report | This is the cycle where the game becomes a game. It is also the first one with a rule that can be subtly wrong, so the user's play catches what a report would not |
| 3 | Polish the user directs — speed curve, colors, game-over screen — plus a high score persisted to a file in the project folder | Play, beat the score, relaunch, see it remembered | The user sets the scope for the first time. Relaunching to check the score survived is the first thing they verify that a screenshot could not prove |

---

## Acceptance

| Rule |
| ---- |
| A cycle closes when the user has played it, not when the report says it works |
| Every cycle ends with the game in a launchable state — never a half-built cycle left overnight |
| `ACTION_REPORT` records what actually happened, including anything that did not work; a report that matches the prompt exactly every time is a report nobody is reading |
| The first thing that breaks goes into `GOTCHAS.md` the moment it breaks, and the machine goes into `MACHINES.md` when cycle 1 completes |
