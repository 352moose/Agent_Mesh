---
type: blueprint_teach
name: Tutorial build
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

- This shows you how work gets built here, by doing it three times on something small.
- Each round is the same exchange: I write one instruction, the building seat does exactly that and writes back what actually happened, and you check whether the two match.
- That exchange is the thing you are here to see. It is what every real project in this workspace runs on.
- What the rounds happen to produce is a game of Snake — a line that grows as it eats and dies if it hits itself.
- The game is real and it runs on your machine, but it is the excuse, not the goal. It was picked because a game is the one thing you can judge in four seconds without trusting anybody's report.
- Round one is a window with a snake that moves when you press the arrow keys. Round two adds food, growth, and a score. Round three is whatever you want polished, plus a high score that survives closing the game.
- The part that matters is what you do at the end of each round: play it, then read what the report claimed, and see whether it told you the truth.
- A round where the game came out broken and the report said so is a round that went well. That is the loop working.
- A round where the game came out fine and you never read the report is a round that taught you nothing, and nothing here will warn you about that.
- Nothing is installed. Nothing leaves your machine. There is no internet access and the only files written are inside the project folder.
- If you stop after round one you have still seen one full exchange, which is most of the point. Stopping early is a fine outcome.

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
