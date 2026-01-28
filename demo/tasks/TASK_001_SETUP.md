# Task: Project Setup

## Goal
Initialize the repository integrity and set up the foundation for both Backend (FastAPI) and Frontend (React+Vite).

## AI Model Selection
- **Primary Model**: [Gemini]
- **Fallback Model**: [Gemini 1.5 Flash]
- **Rationale**: [Standard scaffolding work, high speed and good code generation for boilerplate]
- **Task Complexity**: [Low]
- **Task Type**: [DevOps/Setup]

### Approval
- **Reviewer**: User
- **Date**: 2026-01-27
- **Status**: ✅ Approved (Self-verified setup)

## Context
We are starting a fresh project. We need a backend folder and a frontend folder.

## Constraints
- Follow ARCHITECTURE.md strictly
- Backend: FastAPI, using `uv` or `pip` (standard `requirements.txt`)
- Frontend: React + Vite + Vanilla CSS
- No user authentication system

## Deliverables
- `backend/` directory with `main.py` and `requirements.txt`
- `frontend/` directory with a running React app
- `README.md` updated with how to run both
- `.gitignore` configured for both python and node

## Acceptance Criteria
- [ ] Backend responds to `GET /` with `{"message": "Hello World"}`
- [ ] Frontend displays a "Hello World" page at localhost:3000
- [ ] Both can run concurrently

## Tests Required
- [ ] `curl http://localhost:8000/` returns 200 OK
- [ ] Browser visits `http://localhost:3000/` and sees the app
