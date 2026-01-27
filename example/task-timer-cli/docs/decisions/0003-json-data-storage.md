# ADR 0003: Use JSON for Data Storage

## Status
Accepted

## Context
Need to choose storage format for time entries. Options: JSON, SQLite, CSV, pickle.

## Decision
Use JSON file at ~/.task-timer/data.json.

## Consequences
**Pros:**
- Human-readable
- Easy to edit manually
- No external dependencies
- Portable across systems

**Cons:**
- Not suitable for large datasets (>1000 entries)
- No concurrent access safety
- Slower than binary formats

**Mitigation:**
- Target use case is personal time tracking (<1000 entries)
- Single-user assumption documented in ARCHITECTURE.md

## References
- Related task: tasks/TASK_001_project_setup_core_timer.md
- ARCHITECTURE.md: Constraints section
