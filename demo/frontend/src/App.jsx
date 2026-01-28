import { useState, useEffect } from 'react'
import './index.css'

const API_URL = 'http://localhost:8000/todos';

function App() {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    try {
      const res = await fetch(API_URL);
      if (!res.ok) throw new Error('Failed to fetch');
      const data = await res.json();
      setTodos(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const addTodo = async (e) => {
    e.preventDefault();
    if (!inputValue.trim()) return;

    try {
      const res = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: inputValue })
      });
      const newTodo = await res.json();
      setTodos([...todos, newTodo]);
      setInputValue('');
    } catch (err) {
      console.error('Error adding todo:', err);
    }
  };

  const toggleTodo = async (id, currentStatus) => {
    try {
      const res = await fetch(`${API_URL}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed: !currentStatus })
      });
      const updated = await res.json();
      setTodos(todos.map(t => t.id === id ? updated : t));
    } catch (err) {
      console.error('Error updating todo:', err);
    }
  };

  const toggleTimer = async (id) => {
    try {
      const res = await fetch(`${API_URL}/${id}/toggle-timer`, {
        method: 'POST'
      });
      const updated = await res.json();
      setTodos(todos.map(t => t.id === id ? updated : t));
    } catch (err) {
      console.error('Error toggling timer:', err);
    }
  };

  // Local ticker for running timers
  useEffect(() => {
    const interval = setInterval(() => {
      setTodos(currentTodos =>
        currentTodos.map(t => {
          if (t.is_running) {
            // Optimistic update for display only
            return { ...t, time_spent: t.time_spent + 1 };
          }
          return t;
        })
      );
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const deleteTodo = async (id) => {
    try {
      await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
      setTodos(todos.filter(t => t.id !== id));
    } catch (err) {
      console.error('Error deleting todo:', err);
    }
  };

  if (loading) return <div className="loading">Loading tasks...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="app-container">
      <h1>My Tasks</h1>

      <form onSubmit={addTodo} className="input-group">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="What needs to be done?"
          autoFocus
        />
        <button type="submit" className="add-btn">Add</button>
      </form>

      <ul className="todo-list">
        {todos.map(todo => (
          <li key={todo.id} className="todo-item">
            <div
              className={`checkbox ${todo.completed ? 'completed' : ''}`}
              onClick={() => toggleTodo(todo.id, todo.completed)}
            />
            <span
              className={`todo-text ${todo.completed ? 'completed' : ''}`}
              onClick={() => toggleTodo(todo.id, todo.completed)}
            >
              {todo.title}
            </span>

            <div className="timer-controls">
              <span className="time-display">{formatTime(todo.time_spent)}</span>
              <button
                className={`timer-btn ${todo.is_running ? 'running' : ''}`}
                onClick={() => toggleTimer(todo.id)}
              >
                {todo.is_running ? '⏸' : '▶'}
              </button>
            </div>

            <button
              className="delete-btn"
              onClick={(e) => {
                e.stopPropagation();
                deleteTodo(todo.id);
              }}
            >
              ×
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
