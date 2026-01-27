# Architecture

## System Overview
Single Python CLI application with JSON file storage.

## Key Components
1. CLI Interface (argparse)
2. Timer Logic (datetime-based)
3. Data Storage (JSON file: ~/.task-timer/data.json)
4. Export Module (CSV writer)

## Data Flow
User → CLI Command → Timer Logic → JSON Storage → Display/Export

## Constraints
- Must work offline
- No external dependencies beyond stdlib
- Data stored locally in user home directory
- JSON format for simplicity and readability

## Risks
- JSON file corruption if process killed during write
- No concurrent access protection (single-user assumed)
