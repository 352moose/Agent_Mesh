---
type: Infra
class: canon
state: unflagged
review_status: protected
created: 2026/03/31
updated: 2026/08/10 OV S93
tags:
  - template
  - memory
  - session
---

# Session Memory Template

---

## Rules

| Rule                                                                         |
| ---------------------------------------------------------------------------- |
| Create on spin up — today's date + one-line goal                             |
| Write below the separator — the blocks above it are fixture                  |
| If content already exists, follow Parallel Session Protocol below            |
| Update incrementally as events happen — do not batch                         |
| Log: decisions, findings, approval outcomes, files written, patches applied  |
| Keep entries concise — one or two lines per event                            |
| Never overwrite prior session data — append only                             |
| At close, build static card from your section, then clear your section       |
| static card: session date, key decisions, open items, reference docs touched |
| Last instance out clears the entire file back to blank template              |

## Parallel Session Protocol

| Rule                                                                                   |
| -------------------------------------------------------------------------------------- |
| On spin up, add a section header: `## [ROLE] — Instance [A/B]` — inform the user another instance is present |
| Append only to your own section                                                         |
| At close, clear your own section only                                                   |
| Before clearing, check other sections. If all empty → you are last out, clear entire file to blank template |

## Custom Instructions

> The role owns everything between the markers. No other agent edits inside them.

| Rule                                                                                    |
| --------------------------------------------------------------------------------------- |
| Role-specific standing instructions only — never restate Rules, Parallel Session Protocol or RULEBOOK |
| Empty is the default state — an empty region is correct, not a gap                      |
| Markers stay even when empty                                                            |

<!-- CUSTOM:BEGIN -->
<!-- CUSTOM:END -->

---

## Template

> A live file carries this frontmatter, then the three blocks above verbatim — markers included — then the separator and this scaffold. Rows clear at close; the table stays.

```markdown
---
type: Infra
class: work
state: unflagged
review_status: live
created: "{YYYY/MM/DD XX S_N}"
updated: "{YYYY/MM/DD XX S_N}"
tags:
---

**Goal:**

| Type | Entry |
| ---- | ----- |
```
