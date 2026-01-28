# Architecture

## 1. System Overview
A simple web-based To-Do List application consisting of a frontend for user interaction and a backend for data persistence. The system is designed for simplicity, speed, and ease of use.

## 2. Technology Stack

### Frontend
- **Framework**: React (via Vite)
- **Styling**: Vanilla CSS (scoped/modules) per template guidelines
- **State Management**: React Context / Local State (Keep it simple)

### Backend
- **Language**: Python
- **Framework**: FastAPI (lightweight, fast, easy to document)
- **Database**: SQLite (embedded, zero config for MVP)

## 3. Architecture Patterns
- **Client-Server**: Distinct separation between frontend UI and backend API.
- **RESTful API**: Standard HTTP methods for CRUD operations.
- **Repository Pattern**: Abstraction layer for database interactions to keep business logic clean.

## 4. Constraint Checklist
- [ ] **No User Auth**: Single-user mode for MVP.
- [ ] **Local Execution**: Must run easily on localhost.
- [ ] **Minimal Dependencies**: Stick to standard libraries where possible.

## 5. Directory Structure
```
/
├── frontend/          # React App
├── backend/           # FastAPI App
│   ├── main.py        # App entry point
│   ├── models.py      # Pydantic & DB models
│   ├── database.py    # DB connection
│   └── routers/       # API endpoints
├── docs/              # Documentation
└── scripts/           # Utility scripts
```

## 6. Implementation Guidelines
- **Frontend**: Components should be small and functional. Use `fetch` for API calls.
- **Backend**: Use Pydantic for validation. Ensure strict type hinting.
- **Error Handling**: Graceful error messages for UI.

## Design Phase Approval
**Reviewer**: User
**Date**: 2026-01-27
**Status**: ✅ Approved

**Notes**: Architecture is sound. Ready to proceed to planning phase.
