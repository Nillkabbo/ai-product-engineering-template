# Task: Backend API Implementation

## Goal
Implement the SQLite database models, Pydantic schemas, and CRUD API endpoints for To-Do items.

## AI Model Selection
- **Primary Model**: [Gemini]
- **Fallback Model**: [Gemini 1.5 Flash]
- **Rationale**: [Strong Python/FastAPI capabilities]
- **Task Complexity**: [Medium]
- **Task Type**: [Backend]

### Approval
- **Reviewer**: User
- **Date**: 2026-01-27
- **Status**: ✅ Approved (Self-verified API)

## Context
The project foundation exists. Now we need the data layer and API.

## Constraints
- Use SQLite (sqlitedict or sqlalchemy is fine, keep it simple. `sqlite3` driver directly is also fine for MVP).
- RESTful conventions.
- Enable CORS for localhost:3000.

## Deliverables
- `backend/models.py` (Pydantic models)
- `backend/database.py` (DB connection)
- `backend/main.py` (Updated with endpoints)

## Acceptance Criteria
- [ ] `POST /todos` creates a item
- [ ] `GET /todos` returns list of items
- [ ] `PUT /todos/{id}` updates status/title
- [ ] `DELETE /todos/{id}` removes item
- [ ] Data persists after server restart

## Tests Required
- [ ] Run `pytest` on API endpoints (or manual curl script)
