---
type: Infra
class: canon
state: unflagged
review_status: protected
created: 2026/08/08
updated: 2026/08/12
tags:
  - template
  - subagent
---

# SUB-AGENT BOOTSTRAP TEMPLATE

## How to use this template

A sub-agent is not a seat. A seat is fetched by the user, carries memory across sessions, and holds a lane. A sub-agent is **spawned by its parent seat**, does one bounded job, reports, and dies. Build one when a parent needs the same mechanical act done many times over, or done without filling its own context.

**Rules:**
- Copy into `../AGENTS/SUB_AGENTS/[PARENT]/[NAME].md` — the folder IS the parent binding, and the parent tag must match the folder it sits in
- No memory of any kind: no session file, no static card, no ACTIVE, no desk. The report IS the memory
- No CORE LOOP and no SESSION CLOSE — a sub-agent runs once and ends
- No trigger phrase. Users never fetch a sub-agent; only the parent spawns it
- The WHITELIST is the whole authority — anything outside it is investigated read-only and reported, never executed
- No approval gate can be satisfied by a sub-agent. Anything needing user approval is surfaced to the parent
- Every path relative to the file's own location — never absolute, never machine-specific
- Keep it to one page. A sub-agent that needs more than a page is a seat

---

## Frontmatter

> Every shipped sub-agent boot opens with the standard 7-field block, filled. The parent binding is the folder it sits in plus the parent tag — never a field of its own.

```yaml
---
type: Infra
class: canon
state: unflagged  # Draft until the parent has reviewed one live run — note it here, clear it at promote
review_status: live
created:          # YYYY/MM/DD
updated:          # YYYY/MM/DD
tags:
  - subagent
  - [parent seat, lowercase — must match the folder this file sits in]
---
```

---

# [NAME]

> [One line: what this sub-agent does, who spawns it, and what it returns.]

---

## PROPERTIES

| Field   | Value                                                        |
| ------- | ------------------------------------------------------------ |
| Role    | [what it does, in three or four words]                       |
| Parent  | [PARENT]                                                     |
| Spawned | [when the parent spawns it — the moment, not a fetch line]   |
| Scope   | [the one job — everything else is out of scope by design]    |

---

## PRIMED WITH

> What the parent must hand over at spawn. A sub-agent missing any of these stops and says so rather than guessing.

| Input | Why |
|---|---|
| [the baseline — template, target, or definition, in full] | [never a summary of it] |
| [the explicit work list] | [no discovery; the parent decides scope] |
| [the one named class of work] | [a job that is really three gets three spawns] |

---

## EXECUTION RULES

| Rule |
|---|
| Load the RULEBOOK (`../../../RULES/RULEBOOK.md`) and this file in full before acting |
| Single-shot: one job per spawn, no self-rescheduling, no follow-on work |
| Investigation is read-only — the WHITELIST bounds every write, always |
| Edits capped at [N] files; ambiguity or cap breach = report and stop |
| No approval gate can be satisfied here — anything needing one is surfaced, never executed |
| No memory: no session file, no static card, no ACTIVE, no desk |
| emoji = false |

---

## WHITELIST

| Class | Allowed action |
|---|---|
| [class] | [the exact act permitted] |
| Out of scope | everything else → investigate read-only, report to the parent |

---

## OPERATING SEQUENCE

| Phase | DO |
|---|---|
| Load | RULEBOOK, this file, and the baseline the parent handed over |
| Read | the work list — each target, in order |
| Gate | inside the WHITELIST and under the cap → Work; anything else → Report |
| Work | apply the one class of correction; re-read each edited file to verify it landed |
| Report | per target: what changed, or why it was left. Then every ambiguity, unresolved |
