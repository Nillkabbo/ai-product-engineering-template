# ADR 0004: Use argparse for CLI

## Status
Accepted

## Context
Need CLI parsing. Options: argparse (stdlib), click, typer, docopt.

## Decision
Use argparse (Python stdlib).

## Consequences
**Pros:**
- No external dependencies
- Well-documented
- Sufficient for our simple command structure

**Cons:**
- More verbose than click/typer
- Less modern/elegant API

**Trade-off:**
- Aligns with ARCHITECTURE.md constraint: stdlib only
- Reduces installation complexity

## References
- Related task: tasks/TASK_001_project_setup_core_timer.md
- ARCHITECTURE.md: No external dependencies constraint
