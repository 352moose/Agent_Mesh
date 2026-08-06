---
type: agent_bootstrap_template
created: 2026/08/05
maintained_by: OVERSEER
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
- CORE LOOP is optional — only for agents with repeating work cycles. Single-shot agents skip it.
- Every path relative to the boot file's own location — never absolute, never machine-specific

---

## Frontmatter

> Every shipped boot opens with this block, filled — a copied boot still carrying `agent_bootstrap_template` in `type` is a defect.

```yaml
---
type: agent_bootstrap
role:              # ROLE
trigger:           # fetch me the [role]
created:           # YYYY/MM/DD
review_status: protected
---
```

---

# [ROLE] BOOTSTRAP

> [One line: what this agent is and does.]

---

## PROPERTIES

| Field   | Value                 |
|---------|-----------------------|
| Role    | [ROLE]                |
| Trigger | `fetch me the [role]` |
| Toolset | [probe on first run — never assume cross-machine] |
| Scope   | [what this agent owns] |

---

## AGENT RULES

### Constraint

| Do not [x] | Do [x] |
| ---------- | ------ |
|            |        |

### Directive

| Mode [x]                    | Write [x]                   | Execute [x]                 |
|-----------------------------|-----------------------------|-----------------------------|
|                             |                             |                             |

### Infrastructure

| Doc [x]  | WHEN                          | WHAT             | WHY                       | HOW                    |
|----------|-------------------------------|------------------|---------------------------|------------------------|
|          | [trigger/cadence, ON DEMAND?] | [what the doc is]| [its purpose in the role] | [how the agent engages]|

---

## PATHS

> Every path relative to THIS FILE — resolve from its location.

| Item                | Path                                                                |
|---------------------|---------------------------------------------------------------------|
| Own desk            | `../../DESKS/[ROLE]S_DESK/`                                         |
| All desks           | `../../DESKS/`                                                      |
| RULEBOOK            | `../../RULES/RULEBOOK.md`                                           |
| ACTIVE              | `../../MEMORY_CARDS/ACTIVE_MEMORY/[ROLE]/ACTIVE.md`                 |
| Session file        | `../../MEMORY_CARDS/SESSION_MEMORY/[ROLE]/CURRENT_SESSION_[ROLE].md` |
| Static memory       | `../../MEMORY_CARDS/STATIC_MEMORY/[ROLE]/`                          |
| [Role-specific doc] | `[path]`                                                            |

---

## [ROLE-SPECIFIC SECTIONS]

> Role-specific operational sections go here — between PATHS and SPIN UP. Only include sections the agent actually needs. Do not pad.

---

## SPIN UP
> For all agents preparing for work.

| Phase  | DO               | Interrogatives                                                                 |
| ------ | ---------------- | ------------------------------------------------------------------------------ |
| Load   | RULEBOOK         | `../../RULES/RULEBOOK.md`                                                      |
| Work   | Memory protocol  | follow RULEBOOK — load session file, page rules                                |
| Load   | ACTIVE           | `../../MEMORY_CARDS/ACTIVE_MEMORY/[ROLE]/ACTIVE.md`                            |
| Load   | Last static card | most recent in `../../MEMORY_CARDS/STATIC_MEMORY/[ROLE]/`; none = first run    |
| Work   | Check desk       | read every file on own desk, oldest first, frontmatter first                   |
| Gate   | First run        | `FIRST_SPIN_UP_PROCEDURE.md` on desk = run it now                              |
| Report | Status           | *[Role] online. [N] desk items, open work, context %.*                         |
| Fork   | Await direction  | do not begin work until user gives direction                                   |

---

## CORE LOOP
context < 75%
> For agents with repeating work cycles.

| Phase   | DO                    | Interrogatives                                             |
| ------- | --------------------- | ---------------------------------------------------------- |
| Prepare | Read work inputs      | plan, desk item, request — whatever this cycle acts on     |
| Prepare | Assess state          | what's done, what's next, any blockers                     |
| Work    | [Role-specific steps] | numbered and sequenced per bootstrap                       |
| Work    | Teach before acting   | what will change and why — user-facing agents              |
| Work    | Deliver output        | prompt, plan, analysis — role's primary product            |
| Work    | Test output           | eval, stress test, push back, or challenge output          |
| Gate    | Pass/fail             | explicit user signal — pass proceeds, fail returns to Work |
| Work    | Update session memory | per RULEBOOK memory protocol                               |
| Gate    | Context gate          | under 75% = next task; at/over = recommend close           |
| Fork    | Await direction       | next task or session close                                 |

---

## SESSION CLOSE
context > 75%
> For all agents ending a session.

| Phase        | DO                       | Interrogatives                                                       |
| ------------ | ------------------------ | -------------------------------------------------------------------- |
| Confirmation | Session close            | user has confirmed "session close"                                   |
| Gate         | Role-specific pre-close  | specific needs before close can continue                             |
| Work         | Update ACTIVE            | log entry + working notes if new patterns found — per doc rules      |
| Work         | Desk hygiene             | flip absorbed desk files to `review_status: sweep`                   |
| Work         | RULEBOOK memory protocol | build static card from session, clear session file                   |
| Report       | Summary                  | work done, findings, open items. End with *"Session closed."*        |
