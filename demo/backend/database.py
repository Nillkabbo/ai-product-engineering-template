import sqlite3
from typing import Generator

DB_NAME = "todo.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0,
        time_spent INTEGER NOT NULL DEFAULT 0,
        last_started_at REAL
    )
    """)
    
    # Simple migration for existing tables (idempotent)
    try:
        conn.execute("ALTER TABLE todos ADD COLUMN time_spent INTEGER NOT NULL DEFAULT 0")
    except sqlite3.OperationalError:
        pass # Column likely exists
        
    try:
        conn.execute("ALTER TABLE todos ADD COLUMN last_started_at REAL")
    except sqlite3.OperationalError:
        pass # Column likely exists

    conn.commit()
    conn.close()

# Initialize API on module import (simple for MVP)
init_db()
