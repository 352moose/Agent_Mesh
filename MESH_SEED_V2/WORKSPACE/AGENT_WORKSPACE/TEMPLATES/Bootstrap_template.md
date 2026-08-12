---
type: Infra
class: canon
state: unflagged
review_status: protected
created: 2026/03/25
updated: 2026/08/10 OV S93
tags:
  - template
  - bootstrap
---

# BOOTSTRAP TEMPLATE

## How to use this template

**Rules:**
- Do not restate RULEBOOK content — reference it with `[[RULEBOOK]]`
- AGENT RULES: every row starts with a verb. Directive rows are keyed by work mode — single-mode agents use one row.
- Infrastructure: one row per standing doc the agent works with. Reads live here, not in Directive. Non-spin-up docs marked (ON DEMAND).
- User-facing steps sequenced into workflow, not floating in AGENT RULES
- No internal work between user-facing steps
- Keep it tight — long sections belong in reference docs
- CORE LOOP is optional — only for agents with repeating work cycles. Director defines its own structure. Infrastructure agents skip it.

---

## Frontmatter

> Every shipped boot opens with this block, filled — a copied boot still carrying placeholder stamps is a defect.

```yaml
---
type: Infra
class: canon
state: unflagged
review_status: protected
created: "{YYYY/MM/DD XX S_N}"
updated: "{YYYY/MM/DD XX S_N}"
tags:
---
```

---

# [ROLE] BOOTSTRAP

> [One line: what this agent is and does.]

---

## AGENT RULES

### Constraint

| Do not [x] | Do [x] |
| ---------- | ------ |
|            |        |

### Directive

| Mode [x]                    | Execute [x]                 |
|-----------------------------|-----------------------------|
|                             |                             |

> Base shape per `RULES/TABLES.md` — add a column (`When`, `Write`) only when every mode fills it.

### Infrastructure

| Doc [x]  | WHEN                          | WHAT             | WHY                       | HOW                    |
|----------|-------------------------------|------------------|---------------------------|------------------------|
|          | [trigger/cadence, ON DEMAND?] | [what the doc is]| [its purpose in the role] | [how the agent engages]|

---

## VAULT PATHS

| Item                | Path                                                            |
|---------------------|-----------------------------------------------------------------|
| [Role desk]         | `AGENTS/DESKS/[ROLE]S_DESK/`                                    |
| [Role-specific doc] | `[path]`                                                        |
| Session file        | `MEMORY_CARDS/SESSION_MEMORY/[ROLE]/CURRENT_SESSION_[ROLE].md`  |
| Static memory       | `MEMORY_CARDS/STATIC_MEMORY/[ROLE]/`                            |

> All paths relative to `AGENT_WORKSPACE/` — see `RULES/RULEBOOK.md` §NAVIGATION.

---

## [ROLE-SPECIFIC SECTIONS]

> Role-specific operational sections go here — between VAULT PATHS and SPIN UP. Only include sections the agent actually needs. Do not pad.

---

## SPIN UP
> For all agents preparing for work.

| Phase  | DO                    | Interrogatives                                  |
| ------ | --------------------- | ----------------------------------------------- |
| Load   | RULEBOOK              | `RULES/RULEBOOK.md`                    |
| Work   | Memory protocol       | follow RULEBOOK — load session file, page rules |
| Load   | last static card      | most recent from `STATIC_MEMORY/[ROLE]/`        |
| Load   | role-specific context | fixtures, ACTIVE, etc.                          |
| Load   | Check desk            | read desk doc frontmatters for status           |
| Gate   | Priority notice       | if priority message on desk, stop and report    |
| Report | status                | role online, what was loaded, context %         |
| Fork   | Await direction       | do not begin work until user gives direction    |

---

## CORE LOOP
context < 75%
> For agents with repeating work cycles.

| Phase   | DO                    | Interrogatives                                             |
| ------- | --------------------- | ---------------------------------------------------------- |
| Load    | Read work inputs      | plan, desk item, request — whatever this cycle acts on     |
| Load    | Assess state          | what's done, what's next, any blockers                     |
| Work    | [Role-specific steps] | numbered and sequenced per bootstrap                       |
| Work    | Teach before acting   | what will change and why — user-facing agents              |
| Work    | Deliver output        | prompt, plan, analysis — role's primary product            |
| Work    | Test output           | eval, stress test, push back, or challenge output          |
| Gate    | Pass/fail             | explicit user signal — pass proceeds, fail returns to Work |
| Work    | Update session memory | Per doc rules                                              |
| Gate    | Report context load   | under threshold = Fork, over = recommend close             |
| Fork    | Await Direction       | Session Close, Repeat Loop                                 |

---

## Alternative Loop
context < 75%
> For agents with multiple work cycles.

| Phase   | DO                    | Interrogatives                                             |
| ------- | --------------------- | ---------------------------------------------------------- |
| Load    | Assess state          | what's needed? read relevant docs                          |
| Work    | [Role-specific steps] | numbered and sequenced per bootstrap                       |
| Work    | Teach before acting   | what will change and why — user-facing agents              |
| Work    | Deliver output        | prompt, plan, analysis — role's primary product            |
| Work    | Test output           | eval, stress test, push back, or challenge output          |
| Gate    | Pass/fail             | explicit user signal — pass proceeds, fail returns to Work |
| Work    | Update session memory | Per doc rules                                              |
| Gate    | Report context load   | under threshold = Fork, over = recommend close             |
| Fork    | Await Direction       | Session Close, Repeat Loop                                 |

---

## SESSION CLOSE
context > 75%
> For all agents ending a session.

| Phase        | DO                        | Interrogatives                                                      |
| ------------ | ------------------------- | ------------------------------------------------------------------- |
| Gate         | Session close             | user has confirmed "session close."                                 |
| Gate         | Role-specific pre-close   | specific needs before close can continue                            |
| Work         | Frontmatter hygiene       | flag stale docs on own desk for sweep                               |
| Work         | Role-specific close tasks | reports, fixtures, docs, ACTIVE, etc.                               |
| Work         | RULEBOOK memory protocol  | build static card from session, clear session                      |
| Report       | Summary                   | work done, findings, patches, open items, end with "Session Closed" |
