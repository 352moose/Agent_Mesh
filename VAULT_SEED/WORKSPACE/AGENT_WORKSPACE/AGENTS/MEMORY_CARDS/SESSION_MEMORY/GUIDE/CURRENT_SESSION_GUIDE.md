---
type: session_memory
role: GUIDE
session: S0
created: 2026/08/05
---

## Rules

| Rule                                                                         |
| ---------------------------------------------------------------------------- |
| Create on spin up — today's date + one-line goal                             |
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
