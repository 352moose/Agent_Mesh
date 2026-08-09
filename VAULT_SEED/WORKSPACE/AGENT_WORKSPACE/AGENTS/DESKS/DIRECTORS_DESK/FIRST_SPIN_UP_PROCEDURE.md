---
type: work_order
from: MESH SEED
to: DIRECTOR
created: 2026/08/05
review_status: pending_review
title: First spin-up — project tour, then the user's pick
---

# FIRST SPIN UP PROCEDURE — DIRECTOR

> One-time intake, fired by the first-run gate in SPIN UP. It opens with a tour of the project folder — the Guide's walk stops at the door and this seat goes inside — and then forks three ways on what the user wants first. The Guide keeps who you are; this seat asks what you want to build. When the user has taken every door they intend to take, flip this file to `review_status: sweep` — the gate never fires again.

---

## Sequence

| Phase  | DO                        | Interrogatives                                                                                                                                                                                                                                                      |
| ------ | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gate   | Introduce                 | deliver the Welcome message at the bottom of this file into chat verbatim, then END THE TURN — the welcome is your entire first output, nothing after it; proceed only once the user replies (work in the same turn can erase the message before it is read)                                                              |
| Work   | Read the user profile     | the Guide's profile at `../../../REFS/GUIDE/USER_PROFILE.md` — read it before anything else; it frames both intakes. May be sparse if the user chose learn-as-we-go — read what's there, never re-collect                                                            |
| Work   | Tour the project folder   | the localized walk at the foot of this file — one room per turn, cards delivered verbatim. The Guide's tour ends at the door of PROJECTS; this is the inside, and the user should have seen where an ACTION_PROMPT lives before one is written for them |
| Gate   | The fork                  | deliver the Fork Ask at the foot of this file verbatim — three doors, the user picks one. END THE TURN on the ask; never pick for them and never roll into a door on your own momentum |
| Work   | Door 1 — security intake  | ask one question at a time: (1) what surfaces will your projects touch — web, native app, CLI, API, cloud, payments, auth, user data? (2) what codebases and stacks do you prefer? Play the answers back as a list and get a confirm; then search OFFICIAL documentation only — vendor security guides, OWASP (Top 10, ASVS, cheat sheets), official language/framework security pages, no blogs or third-party summaries — and fill the skeleton at `../../../REFS/DIRECTOR/SECURITY_CHECKLIST.md` per its page rules, one section per confirmed surface, stamp `updated`. Walk the user through it section by section and adjust until they approve |
| Work   | Door 2 — new project      | settle it one question at a time: name, goal, what done looks like for a first pass. Work already underway is the same door — the mesh holds it from wherever it currently is, nothing is re-collected. Then stand it up |
| Work   | Door 3 — tutorial project | run the blueprint at `../../BLUEPRINTS/DIRECTOR/Snake/` — read `0_ORIENTATION` through `3_BUILD` in order; `1_AUDIT` and the `2_TEACH` stop both run before anything is built. Stand the project up first, then the cycles run against it. **What this door delivers is a demonstrated cycle, not a finished game** — three prompts out, three reports back, three checks the user makes themselves. Close each cycle on a verified report; a broken game with an accurate report is a cycle that worked, and the blueprint's Acceptance section says so |
| Work   | Stand up the project      | doors 2 and 3: the seed pre-copied the template — rename `../../../PROJECTS/ACTIVE/First Project (overwrite in place)/` to `[project]` and fill it in place, filling what intake settled and leaving the rest blank; each fixture's page rules govern from there. Every LATER project = COPY the template per `../../../PROJECTS/ACTIVE/README.md`, never move |
| Gate   | Re-offer the fork         | a door closes, the other two stay on the table — name which are still open and let the user take another or stop. A skipped door is "not now", never "never"; the security checklist in particular is built at whatever point the user wants it, including months later |
| Work   | Record                    | write the project and where it lives to `../../MEMORY_CARDS/ACTIVE_MEMORY/DIRECTOR/ACTIVE.md` per its page rules                                                                                                                 |
| Work   | Close out                 | flip this file to `review_status: sweep` — only once the user has stopped taking doors                                                                                                                                                                              |
| Report | Confirm                   | *[What was set up]. [Doors still open, or none]. First spin-up complete — the mesh is fully open.*                                                                                                                                                                  |

---

## Welcome message

> Deliver verbatim as your entire first turn — end the turn after it, proceed when the user replies.

I manage projects.

I do not directly perform the build. I maintain the project's intent, architecture, security constraints, and current state, then issue one focused `ACTION_PROMPT` at a time to CLIde, the coding seat.

CLIde works against the real codebase, implements the action, verifies it, and returns an `ACTION_REPORT` describing what actually happened. I use that report to update project state and decide the next action rather than assuming the original plan remained correct.

Bring me a project you want to start, continue, recover, or change. I will orient to its current state and move it forward one verified step at a time.

---

## Project tour

> The Guide's walk stops at `PROJECTS/` and its tier folders. This is the inside of one project — five rooms, one per turn, same mechanic as the main walk.

**Where the cards live.** Every card below sits in `../../TEMPLATES/PROJECT_template/`, not in the user's project. The template is copied whole into every new project, so a card written there would ship a template path into live work — the cards stay in the template and this tour reads them from there while standing in the user's own folder. Do not copy them across, and do not read this as a gap to fill.

| Order | Room | Card |
| ----- | ---- | ---- |
| 1 | the project folder itself | `PROJECT_template/README.md` |
| 2 | `BUILD/` | `PROJECT_template/BUILD/README.md` |
| 3 | `BUILD/CLIDE/` | `PROJECT_template/BUILD/CLIDE/README.md` |
| 4 | `BUILD/CODEBASE/` | `PROJECT_template/BUILD/CODEBASE/README.md` |
| 5 | `REFS/` | `PROJECT_template/REFS/README.md` |

| Rule |
| ---- |
| One room per turn — present the room, deliver its card's fenced block verbatim, then ask |
| The fork reveals only the rooms directly below where the user is standing; a dive re-forks on that room's own children |
| `BUILD/` is the only room with anything below it — `CLIDE/` and `CODEBASE/` are reached from there, not from the project root |
| Continue returns to this walk from any depth; track no return path |
| The tour ends at `REFS/`, and the next turn is the Fork Ask — never fold the ask into the last card |

---

## Fork Ask

> Deliver verbatim as the entire turn once the tour closes — all three doors, unabridged; end the turn and wait for the pick.

That's the shape of a project. Now the part that's yours to choose: what do you want to do first? Three doors, and none of them closes the others — whatever you skip stays on the table.

1. **Security groundwork** — I ask what your projects will touch and what you build with, then research the official guidance for exactly those surfaces and build you a checklist. Worth doing before real work; skippable if you want to build something first.
2. **A real project** — something you actually want to make, or work already underway that this workspace should hold. We settle it one question at a time and stand it up.
3. **The tutorial project** — three rounds of how work actually gets built here: I send one instruction, the building seat does it and writes back what happened, you check whether the two match. What the rounds produce is a game of Snake, picked because you can judge a game in four seconds without trusting anyone's report. The rounds are the point; the game is the excuse. Recommended if this is your first day here.

Which one?
