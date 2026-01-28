from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_db_connection, init_db
from models import TodoCreate, TodoUpdate, TodoResponse
import sqlite3

app = FastAPI()

# Enable CORS for frontend
# Enable CORS for frontend (allow all for dev)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB on startup
init_db()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/todos", response_model=list[TodoResponse])
def get_todos():
    conn = get_db_connection()
    todos = conn.execute("SELECT * FROM todos").fetchall()
    conn.close()
    
    results = []
    for todo in todos:
        t = dict(todo)
        t["is_running"] = t["last_started_at"] is not None
        results.append(t)
        
    return results

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (title, completed) VALUES (?, ?)", (todo.title, todo.completed))
    todo_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {**todo.dict(), "id": todo_id}

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if exists
    existing = cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
    if not existing:
        conn.close()
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # Update fields dynamically
    update_data = todo.model_dump(exclude_unset=True)
    if not update_data:
        conn.close()
        return dict(existing)
        
    query_parts = []
    params = []
    for key, value in update_data.items():
        query_parts.append(f"{key} = ?")
        params.append(value)
    
    params.append(todo_id)
    query = f"UPDATE todos SET {', '.join(query_parts)} WHERE id = ?"
    
    cursor.execute(query, tuple(params))
    conn.commit()
    
    # Fetch updated
    updated = cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
    conn.close()
    return dict(updated)

    return {"message": "Todo deleted"}

@app.post("/todos/{todo_id}/toggle-timer", response_model=TodoResponse)
def toggle_timer(todo_id: int):
    import time
    conn = get_db_connection()
    cursor = conn.cursor()
    
    existing = cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
    if not existing:
        conn.close()
        raise HTTPException(status_code=404, detail="Todo not found")
        
    todo = dict(existing)
    now = time.time()
    
    if todo["last_started_at"]:
        # STOP Timer
        elapsed = int(now - todo["last_started_at"])
        new_time = todo["time_spent"] + elapsed
        cursor.execute("UPDATE todos SET time_spent = ?, last_started_at = NULL WHERE id = ?", (new_time, todo_id))
    else:
        # START Timer
        cursor.execute("UPDATE todos SET last_started_at = ? WHERE id = ?", (now, todo_id))
        
    conn.commit()
    updated = cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
    conn.close()
    
    result = dict(updated)
    result["is_running"] = result["last_started_at"] is not None
    return result
