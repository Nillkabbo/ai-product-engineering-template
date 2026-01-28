# 2. Task Timer Implementation

Date: 2026-01-27

## Status

Proposed

## Context

Users want to track how much time they spend on each task. This requires a way to "Start" and "Stop" a timer for a specific task and persist the elapsed duration.

## Decision

We will add a `time_spent` (integer, seconds) and `is_running` (boolean) field to the `todos` table.

### Backend Changes
- **Database**: Add `time_spent` (default 0) and `last_started_at` (datetime, nullable).
- **API**: Add endpoints or update commands to toggle timer state.
  - When `start` is called: Update `last_started_at` to current timestamp.
  - When `stop` is called: Calculate delta (now - last_started_at), add to `time_spent`, and clear `last_started_at`.

### Frontend Changes
- **UI**: Display time formatted as `MM:SS`.
- **Interactions**: Add a "Play/Pause" button next to each task.
- **Logic**: If a task `is_running`, the frontend should auto-increment the display every second (optimistic update), but rely on backend for truth on stop.

## Consequences

- Requires a database migration (or schema update for SQLite).
- Frontend needs a `setInterval` to handle active timers.
- Simple implementation: Does not handle time tracking across multiple devices if the browser is closed while running (for MVP, we will just count time while the backend knows it's running, but calculating "offline" time requires the `last_started_at` logic).
