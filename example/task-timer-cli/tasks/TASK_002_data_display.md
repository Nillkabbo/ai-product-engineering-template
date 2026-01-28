# Task: Data Display

## Goal
Implement functionality to list all recorded time entries and view details of specific entries.

## Recommended AI Model(s)
- Primary: Claude 3.5 Sonnet
- Fallback: GPT-4o
- Why: Simple logic, requires clean formatting of output.

## Context
Phase 2 of the Execution Plan. We need to allow users to see their time history.

## Constraints
- Minimal diff
- Follow ARCHITECTURE.md
- Use standard libraries only (no external table printer, just f-strings/formatting)

## Deliverables
- [x] `list` command in `timer.py`
- [x] `view` command in `timer.py`

## Acceptance Criteria
- `python timer.py list` shows a table of all entries with Index, Date, Task, Duration.
- `python timer.py view <N>` shows full details for entry N.
- Handles empty data gracefully.
- Handles invalid indices gracefully.

## Tests Required
- Manual verification:
    1. Start/stop a task.
    2. Run `list` and verify output.
    3. Run `view 0` and verify output.
    4. Run `view 999` and verify error message.

## AI Session Notes
- Model used: Gemini 2.0 Flash
- Outcome: Successfully implemented `list` and `view` commands. Verified manually with positive results.

## Human Review Notes
