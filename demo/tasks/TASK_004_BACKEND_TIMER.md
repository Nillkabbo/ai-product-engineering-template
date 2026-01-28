# Task: Backend Timer Logic

## Goal
Update database schema and API to support tracking time spent on tasks.

## AI Model Selection
- **Primary Model**: [Gemini]
- **Fallback Model**: [Gemini 1.5 Flash]
- **Rationale**: [Backend logic implementation]
- **Task Complexity**: [Medium]
- **Task Type**: [Backend]

## Context
We need to persist how long a task has been worked on.

## Constraints
- Minimal diff.
- Use `sqlite3` migration manually (since we don't have Alembic set up yet).

## Deliverables
- `backend/models.py`: Add `time_spent` (int) and `last_started_at` (float/int).
- `backend/database.py`: Update schema creation.
- `backend/main.py`: Add toggle endpoint.

## Acceptance Criteria
- [ ] Toggle endpoint switches state between running/stopped.
- [ ] Stopping updates the `time_spent` accumulator.
- [ ] Getting todos returns current `time_spent`.

## Tests Required
- [ ] Test script to verify timer calculation logic.
