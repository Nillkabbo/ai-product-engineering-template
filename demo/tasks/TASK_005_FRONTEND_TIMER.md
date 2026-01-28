# Task: Frontend Timer UI

## Goal
Add visual timer controls to the To-Do list.

## AI Model Selection
- **Primary Model**: [Gemini]
- **Fallback Model**: [Gemini 1.5 Flash]
- **Rationale**: [React state management for timers]
- **Task Complexity**: [Medium]
- **Task Type**: [Frontend]

## Context
Backend now supports timing. Frontend needs to visualize it.

## Constraints
- Use `setInterval` for ticking UI when active.
- Format time as `mm:ss` or `hh:mm:ss`.

## Deliverables
- `frontend/src/components/TodoItem.jsx` (Update).
- `frontend/src/App.jsx` (Handle toggle action).

## Acceptance Criteria
- [ ] Play/Pause button toggles icon.
- [ ] Timer increments every second when running.
- [ ] Page reload shows correct accumulated time.

## Tests Required
- [ ] Manual verification.
