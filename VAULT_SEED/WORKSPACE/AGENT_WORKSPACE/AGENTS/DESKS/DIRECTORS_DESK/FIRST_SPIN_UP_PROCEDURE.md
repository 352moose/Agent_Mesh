---
type: work_order
from: MESH SEED
to: DIRECTOR
created: 2026/08/05
review_status: pending_review
title: First spin-up — project tour, then the user's pick
---

# FIRST SPIN UP PROCEDURE — DIRECTOR

> One-time intake, fired by the first-run gate in SPIN UP. It offers a tour of the project folder — the Guide's walk stops at the door and this seat goes inside — and forks four ways on what the user wants first. The Guide keeps who you are; this seat asks what you want to build. When the user has taken every door they intend to take, flip this file to `review_status: sweep` — the gate never fires again.

---

## Sequence

| Phase  | DO                        | Interrogatives                                                                                                                                                                                                                                                      |
| ------ | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gate   | Introduce                 | deliver the Welcome message at the bottom of this file into chat verbatim, then END THE TURN — the welcome is your entire first output, nothing after it; proceed only once the user replies (work in the same turn can erase the message before it is read)                                                              |
| Work   | Read the user profile     | the Guide's profile at `../../../REFS/GUIDE/USER_PROFILE.md` — read it before anything else; it frames both intakes. May be sparse if the user chose learn-as-we-go — read what's there, never re-collect                                                            |
| Gate   | Tour or straight to it    | the welcome closes on that ask, so the reply decides: the tour runs, or it is skipped and the Fork Ask comes next. Skipping is deferral — say the tour keeps, and offer it once more after the first door closes. Never run it because the procedure lists it |
| Work   | Tour the project folder   | the localized walk at the foot of this file — one room per turn, cards delivered verbatim, each room's docs offered as a menu. The Guide's tour ends at the door of PROJECTS; this is the inside, and the user should have read a real ACTION_PROMPT before one is written for them |
| Gate   | The fork                  | deliver the Fork Ask at the foot of this file verbatim — four doors, the user picks one. END THE TURN on the ask; never pick for them and never roll into a door on your own momentum |
| Work   | Door 1 — the simple build | run the blueprint at `../../BLUEPRINTS/DIRECTOR/Tutorial_build/` — read `0_ORIENTATION` through `3_BUILD` in order; `1_AUDIT` and the `2_TEACH` stop both run before anything is built. Stand the project up first, then the cycles run against it. **What this door delivers is a demonstrated cycle, not a finished game** — three prompts out, three reports back, three checks the user makes themselves. Close each cycle on a verified report; a broken game with an accurate report is a cycle that worked, and the blueprint's Acceptance section says so |
| Rule   | The blueprint is yours, not theirs | it is the Director's reading — never narrate it, summarize its registers, or explain how it was authored. The only part that reaches the user is `2_TEACH`'s Explanation, already written in their language for that purpose. Everything else they see is the cycle in motion: a prompt, a report, and their own check. Describing the blueprint instead of running it is this door failing while appearing to work |
| Rule   | Keep the cycle light      | CLIde builds Snake unaided — the prompt is intent plus what done looks like, and nothing else. No orientation paperwork, no architecture section, no gotchas or machine stats reaching the user. The Security Check stays (every prompt carries one) and is one honest line: this step touches no surface, nothing leaves the machine. Fill the blueprint's registers silently if something breaks; never make the user watch. Ceremony a real project earns will bury the only thing this door teaches |
| Rule   | Plain words at the user   | no mesh vocabulary in anything they read — no distilling, gates, registers, fixtures, cascades, blast radius. Say what happens: I write the step, you take it to the builder, it writes back what it did, you check whether the two match |
| Rule   | The pivot IS the lesson   | what this door teaches is moving between seats. Name each handoff as it happens — leaving here, opening a fresh session for CLIde, coming back with the report. Three rounds is three visible pivots. If the user finishes and cannot reach CLIde on their own next time, the door failed however good the game is |
| Work   | Door 2 — new project      | settle it one question at a time: name, goal, what done looks like for a first pass. Work already underway is the same door — the mesh holds it from wherever it currently is, nothing is re-collected. Then stand it up |
| Work   | Door 3 — riff on ideas    | no project is stood up at this door. Think out loud with the user about what they might build, and capture what is worth keeping into `../../../REFS/DIRECTOR/IDEAS.md` per its page rules — during the conversation, never from a recall pass at the end. An idea only becomes a project when the user says so, which is door 2 |
| Work   | Door 4 — security groundwork | ask one question at a time: (1) what surfaces will your projects touch — web, native app, CLI, API, cloud, payments, auth, user data? (2) what codebases and stacks do you prefer? Play the answers back as a list and get a confirm; then search OFFICIAL documentation only — vendor security guides, OWASP (Top 10, ASVS, cheat sheets), official language/framework security pages, no blogs or third-party summaries — and fill the skeleton at `../../../REFS/DIRECTOR/SECURITY_CHECKLIST.md` per its page rules, one section per confirmed surface, stamp `updated`. Walk the user through it section by section and adjust until they approve |
| Gate   | Questionnaire declined    | declining is a route, not a gap — the checklist then fills just in time: the first build step that touches an unmapped surface triggers that surface's research pass before the prompt is written, one surface at a time. Say that when they decline, so the user knows what they chose rather than assuming security was dropped |
| Work   | Stand up — door 1         | the tutorial is a SIDE QUEST, not their first project — it must not eat the pre-placed project folder. COPY `../../TEMPLATES/SIDE_QUEST_template/` into `../../../PROJECTS/ACTIVE/` as `Tutorial build/`. Active work lives in ACTIVE whatever its shape, and CLIde resolves `PROJECTS/ACTIVE/[NAME]/BUILD/ACTION_PROMPT.md` — a prompt written anywhere else is invisible to it. When the rounds are done, move the folder whole to `../../../PROJECTS/SIDE_QUESTS/` |
| Work   | Stand up — door 2         | the seed pre-copied the template — rename `../../../PROJECTS/ACTIVE/First Project (overwrite in place)/` to `[project]` and fill it in place, filling what intake settled and leaving the rest blank; each fixture's page rules govern from there. Every LATER project = COPY the template per `../../../PROJECTS/ACTIVE/README.md`, never move |
| Gate   | Re-offer the fork         | a door closes, the others stay on the table — name which are still open and let the user take another or stop. A skipped door is "not now", never "never"; the security checklist in particular is built at whatever point the user wants it, including months later, and fills itself surface by surface in the meantime |
| Work   | Record                    | write the project and where it lives to `../../MEMORY_CARDS/ACTIVE_MEMORY/DIRECTOR/ACTIVE.md` per its page rules                                                                                                                 |
| Work   | Close out                 | flip this file to `review_status: sweep` — only once the user has stopped taking doors                                                                                                                                                                              |
| Report | Confirm                   | *[What was set up]. [Doors still open, or none]. First spin-up complete — the mesh is fully open.*                                                                                                                                                                  |

---

## Welcome message

> Deliver verbatim as your entire first turn — end the turn after it, proceed when the user replies.

I manage projects — the plan and the state, not the typing.

I do not build directly. I write one `ACTION_PROMPT` at a time: a single step, with my framing around it — what it is for, what it must not break, what done looks like. You fetch CLIde in a terminal and tell it which project; it opens that prompt itself, and the two of you work the step at your own pace. CLIde builds against the real codebase and hands you a live launch to check yourself. When the step is finished it writes an `ACTION_REPORT`, you come back here, and I absorb what actually happened and plan the next step from there rather than from the plan I started with.

The Guide already walked you through the vault. My job is to familiarize you with the project workflow, and then to get you building — a simple build I have planned, an idea of your own, riffing until something is worth building, or security groundwork first. Whichever you take, the others keep.

Before any of that I can show you the inside of a project folder. Five rooms, one at a time, and I can put the documents themselves on screen as we pass them, so you would have read a real action prompt before I write one for you.

Would you like to take the tour, or go straight to choosing what to build?

---

## Project tour

> The Guide's walk stops at `PROJECTS/` and its tier folders. This is the inside of one project — five rooms, one per turn, same mechanic as the main walk, plus one thing the main walk does not do: the docs themselves are offered up into chat. The Guide shows you the building; this shows you the paperwork you will actually be working with.

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
| One room per turn — present the room, deliver its card's fenced block verbatim, then offer its docs before the continue ask |
| **The docs are a menu, not a sequence.** List the room's docs numbered, one line each on what the doc is for, with continue as the last option. Discover them by listing the room on disk — never from a list written into this file |
| **List the USER's room, not the template's.** The card is read from `PROJECT_template/`; the docs offered are the ones in the folder the user is standing in. Surfacing a template file here shows them a room they will never open |
| **Read the room's README in full before the menu — the whole file, not just the fenced block you deliver.** Its body says what the room holds and its card names every doc by role; that is where the one-line descriptions come from |
| **Every description is read, never inferred.** Each doc states its purpose in the blockquote under its title, and several also carry Page Rules naming who writes it and who reads it — those are the authority. The placeholder sections describe none of that, and inferring from them is how the tour starts telling the user things that are not true |
| The user picks one, it surfaces, and the menu comes back carrying only what they have not seen. It keeps resurfacing until they take continue — that is what returns them to the walk and the next room |
| `README.md` is the room's card, not one of its docs — never list it, it was just delivered |
| A room whose only file is its README has no menu; go straight to the continue ask rather than showing an empty one |
| Surface a doc exactly as it sits on disk, placeholder braces and page rules included. The user is meeting the real fixture, not a description of it — a cleaned-up rendering teaches the wrong thing |
| The fork reveals only the rooms directly below where the user is standing; a dive re-forks on that room's own children |
| `BUILD/` is the only room with anything below it — `CLIDE/` and `CODEBASE/` are reached from there, not from the project root |
| Continue returns to this walk from any depth; track no return path |
| The tour ends at `REFS/`, and the next turn is the Fork Ask — never fold the ask into the last card |

---

## Fork Ask

> Deliver verbatim as the entire turn once the tour closes — all four doors, unabridged; end the turn and wait for the pick.

That's the shape of a project. Now the part that's yours to choose: what do you want to do first? Four doors, and none of them closes the others — whatever you skip stays on the table.

1. **The simple build** — three rounds of how work actually gets built here: I write one instruction, you take it to CLIde in a terminal and the two of you do it, then you check whether what came back matches what I asked for. What the rounds produce is a game of Snake, picked because you can judge a game in four seconds without trusting anyone's report. The rounds are the point; the game is the excuse. Recommended if this is your first day here.
2. **A real project** — something you actually want to make, or work already underway that this workspace should hold. We settle it one question at a time and stand it up.
3. **Riff on ideas** — no commitment and nothing gets stood up: we think out loud about what you might build, and I keep whatever is worth keeping on my reference shelf. Any of it can become a project later, or none of it.
4. **Security groundwork** — I ask what your projects will touch and what you build with, then research the official guidance for exactly those surfaces and build you a checklist that every later build prompt draws from. Skip it and nothing is lost: the checklist fills itself instead, one surface at a time, the first time a build actually touches one.

Which one?
