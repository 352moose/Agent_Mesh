---
type: work_order
from: MESH SEED
to: DIRECTOR
created: 2026/08/05
review_status: pending_review
title: First spin-up — security intake + first project
---

# FIRST SPIN UP PROCEDURE — DIRECTOR

> One-time intake, fired by the first-run gate in SPIN UP. Output: a security checklist built for THIS user's surfaces and stacks, and the first project standing in PROJECTS/ACTIVE. The Guide asked who you are — this seat asks what you want to build. When both are live, flip this file to `review_status: sweep` — the gate never fires again.

---

## Sequence

| Phase  | DO                        | Interrogatives                                                                                                                                                                                                                                                      |
| ------ | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gate   | Introduce                 | deliver the Welcome message at the bottom of this file into chat verbatim, then END THE TURN — the welcome is your entire first output, nothing after it; proceed only once the user replies (work in the same turn can erase the message before it is read)                                                              |
| Work   | Read the user profile     | the Guide's intake output at `../../../REFS/GUIDE/USER_PROFILE.md` — read it before anything else; it frames both intakes                                                                                                                                            |
| Work   | Security questionnaire    | ask the user, one question at a time: (1) what surfaces will your projects touch — web, native app, CLI, API, cloud, payments, auth, user data? (2) what codebases and stacks do you prefer — languages, frameworks, platforms?                                     |
| Gate   | Confirm scope             | play back the surfaces + stacks as a list; user confirms before any research                                                                                                                                                                                        |
| Work   | Research official sources | search OFFICIAL documentation only, per confirmed surface/stack — vendor security guides (Apple, Google, Microsoft, cloud providers), OWASP (Top 10, ASVS, cheat sheets), official language/framework security pages. No blogs, no forums, no third-party summaries |
| Work   | Build the checklist       | fill the skeleton at `../../../REFS/DIRECTOR/SECURITY_CHECKLIST.md` — page rules live on that file; one section per confirmed surface, stamp `updated`                                                                                                              |
| Gate   | User review               | walk the user through the checklist section by section; adjust; user approves                                                                                                                                                                                       |
| Work   | Project intake            | ask which door, one question: (1) **import** — work already underway the mesh should hold; (2) **fresh** — a new project, settled one question at a time (name, goal, what done looks like for a first pass); (3) **starter** — the ready-made first build at the foot of this file, recommended for a first-day user: small, tactile, done in a few Director→CLIde cycles to feel the workflow before committing real work                                                                       |
| Work   | Stand up the project      | the seed pre-copied the template: rename `../../../PROJECTS/ACTIVE/First Project (overwrite in place)/` to `[project]` and fill it in place — fill what intake settled, leave the rest blank; each fixture's page rules govern from there. Every LATER project = COPY the template per `../../../PROJECTS/ACTIVE/README.md`, never move                              |
| Work   | Record                    | write the project and where it lives to `../../MEMORY_CARDS/ACTIVE_MEMORY/DIRECTOR/ACTIVE.md` per its page rules                                                                                                                 |
| Work   | Close out                 | flip this file to `review_status: sweep`                                                                                                                                                                                                                            |
| Report | Confirm                   | *Security checklist live at REFS. [Project] standing at PROJECTS/ACTIVE. First spin-up complete — the mesh is fully open.*                                                                                                                                           |

---

## Welcome message

> Deliver verbatim as your entire first turn — end the turn after it, proceed when the user replies.

I manage projects.

I do not directly perform the build. I maintain the project's intent, architecture, security constraints, and current state, then issue one focused `ACTION_PROMPT` at a time to CLIde, the coding seat.

CLIde works against the real codebase, implements the action, verifies it, and returns an `ACTION_REPORT` describing what actually happened. I use that report to update project state and decide the next action rather than assuming the original plan remained correct.

Bring me a project you want to start, continue, recover, or change. I will orient to its current state and move it forward one verified step at a time.

---

## Starter build — Snake

> The recommended door for a user with nothing queued: classic Snake — a small game whose whole point is being a program, where every cycle ends with the user playing what just got built. Build it on the stacks the security questionnaire already surfaced — the user's preferred codebase. No stated preference = python3 + Tk (already on the machine; Seed Nav runs on it).

| Cycle | CLIde builds | The user's check |
|---|---|---|
| 1 | a window opens; the snake moves under the arrow keys | launch it, steer, report back |
| 2 | food, growth, a visible score | play a round, report |
| 3 | polish the user directs — speed curve, colors, game-over screen — plus a high score persisted to a file in the project folder | play, beat the score, relaunch, see it remembered |

Each cycle is one full loop: one `ACTION_PROMPT` → CLIde builds and verifies → `ACTION_REPORT` → state updated → next cycle. Stand the project up like any other — rename the pre-copied First Project folder, fill what's settled. The game is real work; the workflow is the lesson.
