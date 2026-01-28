
import subprocess
import time
import requests
import sys

# Start server in background
process = subprocess.Popen(
    ["uvicorn", "main:app", "--port", "8002"], 
    cwd="backend",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print("Starting backend for timer test...")
time.sleep(3)

try:
    base_url = "http://localhost:8002"
    
    # 1. Create Todo
    res = requests.post(f"{base_url}/todos", json={"title": "Timer Test"})
    assert res.status_code == 200
    todo_id = res.json()["id"]
    print("✅ Created Todo")

    # 2. Start Timer
    res = requests.post(f"{base_url}/todos/{todo_id}/toggle-timer")
    assert res.status_code == 200
    data = res.json()
    assert data["is_running"] is True
    print("✅ Started Timer")
    
    print("⏳ Waiting 2 seconds...")
    time.sleep(2)
    
    # 3. Stop Timer
    res = requests.post(f"{base_url}/todos/{todo_id}/toggle-timer")
    assert res.status_code == 200
    data = res.json()
    assert data["is_running"] is False
    assert data["time_spent"] >= 2
    print(f"✅ Stopped Timer. Time Sptent: {data['time_spent']}s")

except Exception as e:
    print(f"❌ Tests failed: {e}")
    sys.exit(1)
finally:
    process.terminate()
    print("Backend stopped.")
