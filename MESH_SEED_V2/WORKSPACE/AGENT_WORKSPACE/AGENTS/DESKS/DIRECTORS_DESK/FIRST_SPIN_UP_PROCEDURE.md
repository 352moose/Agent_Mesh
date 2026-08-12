---
type: work_order
class: work
state: unflagged
review_status: pending_review
created: 2026/08/05
updated: 2026/08/12
tags:
  - spinup
  - director
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
| Work   | Door 1 — the simple build | stand up a fresh side quest, then follow the standard build cycle to help the user understand the flow — Snake is not the deliverable, user familiarity is. (COPY `../../../TEMPLATES/SIDE_QUEST_template/` into `../../../PROJECTS/ACTIVE/` as `Tutorial build/` — CLIde resolves `PROJECTS/ACTIVE/[NAME]/BUILD/ACTION_PROMPT.md`; move it whole to `../../../PROJECTS/SIDE_QUESTS/` after), then run three plain rounds: one prompt out, one report back, one check the user makes themselves. Plain words throughout; name each seat pivot as it happens |
| Work   | Door 2 — new project      | settle it one question at a time: name, goal, what done looks like for a first pass. Work already underway is the same door — the mesh holds it from wherever it currently is, nothing is re-collected. Then stand it up |
| Work   | Door 3 — riff on ideas    | no project is stood up at this door. Think out loud with the user about what they might build, and capture what is worth keeping into `../../../REFS/DIRECTOR/IDEAS.md` per its page rules — during the conversation, never from a recall pass at the end. An idea only becomes a project when the user says so, which is door 2 |
| Work   | Door 4 — security groundwork | ask one question at a time: (1) what surfaces will your projects touch — web, native app, CLI, API, cloud, payments, auth, user data? (2) what codebases and stacks do you prefer? Play the answers back as a list and get a confirm; then search OFFICIAL documentation only — vendor security guides, OWASP (Top 10, ASVS, cheat sheets), official language/framework security pages, no blogs or third-party summaries — and fill the skeleton at `../../../REFS/DIRECTOR/SECURITY_CHECKLIST.md` per its page rules, one section per confirmed surface, stamp `updated`. Walk the user through it section by section and adjust until they approve |
| Gate   | Questionnaire declined    | declining is a route, not a gap — the checklist then fills just in time: the first build step that touches an unmapped surface triggers that surface's research pass before the prompt is written, one surface at a time. Say that when they decline, so the user knows what they chose rather than assuming security was dropped |
| Work   | Stand up — door 2         | COPY `../../../TEMPLATES/PROJECT_template/` into `../../../PROJECTS/ACTIVE/` as `[project]` — never move the template — and fill what intake settled, leaving the rest blank; each fixture's page rules govern from there. Every project stands up the same way, per `../../../PROJECTS/ACTIVE/README.md` |
| Gate   | Re-offer the fork         | a door closes, the others stay on the table — name which are still open and let the user take another or stop. A skipped door is "not now", never "never"; the security checklist in particular is built at whatever point the user wants it, including months later, and fills itself surface by surface in the meantime |
| Work   | Record                    | write the project and where it lives to `../../../MEMORY_CARDS/ACTIVE_MEMORY/DIRECTOR/ACTIVE.md` per its page rules                                                                                                                 |
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

**Where the tour stands.** The tour walks `../../../TEMPLATES/PROJECT_template/` itself — the blank form every project is copied from. Name it as the blank form as you walk it: the user's own project will be a fresh copy of these same rooms, stood up at door 2. The cards live in the template and are read from there; do not copy them anywhere.

| Order | Room | Card |
| ----- | ---- | ---- |
| 1 | the project folder itself | `PROJECT_template/README.md` |
| 2 | `BUILD/` | `PROJECT_template/BUILD/README.md` |
| 3 | `BUILD/CODEBASE/` | `PROJECT_template/BUILD/CODEBASE/README.md` |
| 4 | `CLIDE/` | `PROJECT_template/CLIDE/README.md` |
| 5 | `REFS/` | `PROJECT_template/REFS/README.md` |

| Rule |
| ---- |
| One room per turn — present the room, deliver its card's fenced block verbatim, then offer its docs before the continue ask |
| **The docs are a menu, not a sequence.** List the room's docs numbered, one line each on what the doc is for, with continue as the last option. Discover them by listing the room on disk — never from a list written into this file |
| **The template is the specimen, not live work.** The rooms and docs shown are the blank form's; say so when offering them. Placeholder braces stay visible — the user is meeting the form their project will be stamped from |
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
