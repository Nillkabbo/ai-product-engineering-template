AI Product Engineering - GitHub Template Repository

Purpose
This repository is a ready-to-use GitHub template for AI-assisted, production-grade software engineering. It is tool-agnostic and works with any AI assistant.

Core Rules
- Files are the source of truth. Chat history is not the source of truth.
- ARCHITECTURE.md is authoritative and must never be violated.
- One task at a time. One AI session = one task.
- Minimal diff only. No refactors unless explicitly allowed in the task.
- No task file, no AI work.
- Before ending any session, update WORKING_STATE.md.
- Humans own decisions and releases.

Repository Structure
- MASTER_REFERENCE.md: This bundled rules document
- SYSTEM_PROMPT.md: The system prompt to paste into AI tools
- docs/: Product and architecture documentation
- tasks/: Task templates and active tasks
- WORKING_STATE.md: Rolling compressed state for the project
- CHANGELOG.md: Project change log

Workflow (High Level)
1. Read MASTER_REFERENCE.md once.
2. Fill docs/PRODUCT_VISION.md and docs/ARCHITECTURE.md.
3. Create a task file in tasks/ using TASK_TEMPLATE.md.
4. Work only on the active task.
5. Update WORKING_STATE.md before ending.

Task Discipline
- One task = one file under tasks/
- Task file is required before any AI work
- Model choice must be recorded in the task file
- Do not start a new task until the current task is complete

Architecture Discipline
- ARCHITECTURE.md is the single source of truth
- Any change that affects architecture requires an explicit decision
- If architecture must change, update ARCHITECTURE.md first

Minimal Diff Principle
- Make the smallest change necessary to meet the task goal
- Avoid refactors, renames, or reorganizations unless the task requires it
- Preserve existing patterns and style

Human Ownership
- Humans own decisions and releases
- AI can propose, but humans approve
- Release decisions must be documented in RELEASE_CHECKLIST.md
