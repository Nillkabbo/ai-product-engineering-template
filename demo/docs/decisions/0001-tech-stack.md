# 1. Use FastAPI and React

Date: 2026-01-27

## Status

Proposed

## Context

We need to build a simple MVP To-Do List application. The goal is to have a working prototype quickly while using modern, maintainable technologies. The system should be split into a frontend and backend to demonstrate a standard web application architecture.

## Decision

We will use **FastAPI (Python)** for the backend and **React (Vite)** for the frontend.

### Backend: FastAPI
- **Fast**: High performance, comparable to NodeJS and Go (thanks to Starlette and Pydantic).
- **Easy**: Automatic interactive API documentation (Swagger UI).
- **Modern**: Native implementation of Python type hints.

### Frontend: React (Vite)
- **Standard**: Industry standard for building user interfaces.
- **Vite**: Ultra-fast build tool and dev server.
- **Ecosystem**: Vast ecosystem of libraries and tools (though we will keep dependencies minimal).

### Database: SQLite
- **Simple**: Serverless, zero-configuration configuration.
- **Portable**: Database is a single file on disk.
- **Sufficient**: More than capable of handling the data requirements for a single-user MVP.

## Consequences

- We will need Python 3.9+ installed.
- We will need Node.js installed for the frontend build.
- Deployment is slightly more complex than a static site or monolithic Django app, but separation of concerns is better.
