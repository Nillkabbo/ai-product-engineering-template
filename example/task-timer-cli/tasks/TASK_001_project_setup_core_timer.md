# Task: Project Setup & Core Timer

## Goal
Set up Python project structure and implement basic start/stop timer functionality.

## Recommended AI Model(s)
- Primary: Claude Sonnet 4
- Fallback: GPT-4
- Why: Structured planning and Python best practices

## Context
This is the first task for the task-timer-cli project. We need to establish the project foundation and implement the core timer logic per ARCHITECTURE.md.

## Constraints
- Minimal diff (new project)
- Follow ARCHITECTURE.md: JSON storage, argparse CLI, stdlib only
- No external dependencies

## Deliverables
- Project structure (src/, README.md, requirements.txt)
- timer.py with start/stop functions
- JSON storage implementation
- Basic CLI with 'start' and 'stop' commands

## Acceptance Criteria
- Can run `python timer.py start "Task name"`
- Can run `python timer.py stop`
- Data saved to ~/.task-timer/data.json
- JSON structure follows architecture spec

## Tests Required
- Start timer without existing data file
- Stop timer with active session
- Verify JSON file created and valid

## AI Session Notes
- Model used: Claude Sonnet 4.5
- Outcome: Completed successfully
- All acceptance criteria met:
  - ✅ Can run `python timer.py start "Task name"`
  - ✅ Can run `python timer.py stop`
  - ✅ Data saved to ~/.task-timer/data.json
  - ✅ JSON structure follows architecture spec
- All tests passed:
  - ✅ Start timer without existing data file
  - ✅ Stop timer with active session
  - ✅ Verified JSON file created and valid

## Human Review Notes
[To be filled after review]
