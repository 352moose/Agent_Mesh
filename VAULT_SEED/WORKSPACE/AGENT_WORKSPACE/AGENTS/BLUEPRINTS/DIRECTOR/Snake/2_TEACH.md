---
type: blueprint_teach
name: Snake — tutorial project
created: 2026/08/09
updated: 2026/08/09
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

- This builds a small game you can play. Classic Snake: a line that grows as it eats, and dies if it hits itself.
- The game is real. It is not a demo or a mock-up, and it runs on your machine when it is done.
- It takes three rounds. Each round ends with you playing what was just built and saying whether it works.
- Round one is a window with a snake that moves when you press the arrow keys. Nothing else.
- Round two adds food, growth, and a score you can see.
- Round three is whatever you want polished, plus a high score the game remembers after you close it.
- The reason for building a game rather than something useful is that you can tell instantly whether it worked. No report can convince you a game is fun to play.
- The workflow is the actual lesson. The Director writes one instruction at a time, the building seat does exactly that and reports back, and you check the result before anything else happens.
- That loop is what every later project runs on. This is the cheapest place to learn what it feels like when it goes right, and what a report looks like when it goes wrong.
- Nothing is installed. Nothing leaves your machine. The game has no internet access and the only files written are inside the project folder.
- If you stop after round one, you still have a window with a moving snake and you have seen one full cycle. Stopping early is a fine outcome.

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

- None yet — this blueprint has never been built. The first user to misunderstand something writes the first line here.
