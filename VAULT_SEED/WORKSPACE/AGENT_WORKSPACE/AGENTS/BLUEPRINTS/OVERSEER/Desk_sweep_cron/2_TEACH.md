---
type: blueprint_teach
name: Desk sweep cron
created: 2026/08/08
updated: 2026/08/08
review_status: protected
---

# Teach — Before the Build, Not During It

> A blueprint lands on a stranger, not only a strange machine. They did not have the conversation that produced it and do not know why the gates are there. The audit is the machine half of trust; this is the human half. Nothing is written during this phase.

---

## The Explanation

| CAP        | Behavior                                                | Hygiene                                                                       |
| ---------- | ------------------------------------------------------- | ----------------------------------------------------------------------------- |
| ≤ 20 lines | fluid — plain language, one idea per line, no jargon    | absorbs entries from Did Not Land; drop a line no build has needed in 3 handoffs |

> What the user needs in order to judge whether this is a build they want. Not how it works — what it is, and what it changes on their machine.

- Agents leave files on each other's desks. Once a file has been read and absorbed, someone marks it as finished.
- This job checks the desks every hour and carries the finished ones to the trash tree, filed under the desk they came from.
- It moves, it never deletes. Nothing is destroyed and everything stays findable.
- A file is only touched if it carries the finished mark. An unmarked file is invisible to this job no matter how old it is.
- Desks stay clear on their own, so an agent starting a session reads only what is actually waiting for it.
- It runs on a schedule set by the operating system. Nothing runs until the schedule is installed, and that is a separate step done with the agent.
- On macOS the schedule needs permission to read your folders, granted once in a settings screen, walked click by click.
- The job can be run once in a preview mode that reports what it would move without moving anything. Worth doing the first time.

---

## The Stop

| Phase | DO      | Interrogatives                                                            |
| ----- | ------- | ------------------------------------------------------------------------- |
| Gate  | Ask     | is the picture clear — answer questions, introduce nothing new            |
| Gate  | Confirm | the user confirms before the build starts; no confirm, no build           |
| Fork  | Waive   | a user who already knows says so, and the stop costs one turn             |

> The stop is self-sizing, which is why it is unconditional. Someone who knows this build answers in a sentence. Someone who does not gets the explanation they needed.

---

## Did Not Land

| CAP        | Behavior                                                                  | Hygiene                                  |
| ---------- | ------------------------------------------------------------------------- | ---------------------------------------- |
| ≤ 10 lines | fluid — one line per build that failed on something the user misunderstood | folded into The Explanation, then removed |

> A failed build routes here when the failure was comprehension. Environment failures route to `3_BUILD/GOTCHAS.md` instead — the two registers are separate on purpose, and both are why a blueprint gets smarter with age.

- None yet — this blueprint has been built once, by its author.
