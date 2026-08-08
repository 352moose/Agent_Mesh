---
type: note
scope: SUB_AGENTS
maintained_by: OVERSEER
created: 2026/08/08
review_status: protected
---

# SUB_AGENTS

One folder per parent seat, holding the sub-agents that seat can spawn. **The folder is the binding** — a file in `OVERSEER/` is the Overseer's sub-agent, and nothing else has to declare it. Drop a new one in a parent's folder and that parent can spawn it; there is no registry to update.

A sub-agent is not a seat. A seat is fetched by you, remembers across sessions, and owns a lane. A sub-agent is spawned by its parent, does one bounded job, reports back, and ends — no memory, no desk, no fetch line. It exists so a parent can do the same mechanical act across many files without spending its own attention, or its own context, on each one.

List a parent's folder to see what it can spawn — filenames state the purpose. New ones are built from `../TEMPLATES/SUBAGENT_template/`.
