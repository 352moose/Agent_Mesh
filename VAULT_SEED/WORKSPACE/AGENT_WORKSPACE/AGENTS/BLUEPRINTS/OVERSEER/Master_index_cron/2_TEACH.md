---
type: blueprint_teach
name: Master index refresh cron
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

- The vault has an index file listing what lives where. Without help it goes out of date the first time anyone adds a file.
- This job rewrites that list once a day, on its own, so nobody has to remember to.
- It only rewrites the part of the file between two invisible markers. Anything written above them is yours and is never touched.
- The list has a description column. Those descriptions are written by people and agents, not by this job — the job carries them forward every time it rebuilds, including for files that moved.
- It runs on a schedule set by the operating system, not by the mesh. Nothing runs until the schedule is installed, and installing it is a separate step the user does with the agent.
- Adding the schedule means giving the system permission to read the vault folder. On macOS that is a settings screen, walked click by click.
- The job is silent when nothing changed. It rewrites the file only when the content actually differs, which keeps sync and backup tools quiet.

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
