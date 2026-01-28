
import subprocess
import time
import requests
import sys

# Start server in background
process = subprocess.Popen(
    ["uvicorn", "main:app", "--port", "8001"], 
    cwd="backend",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print("Starting backend for testing...")
time.sleep(3)  # Wait for startup

try:
    base_url = "http://localhost:8001"
    
    # 1. Test Root
    res = requests.get(f"{base_url}/")
    assert res.status_code == 200
    print("✅ Root endpoint working")

    # 2. Test Create
    res = requests.post(f"{base_url}/todos", json={"title": "Test Todo"})
    assert res.status_code == 200
    data = res.json()
    assert data["title"] == "Test Todo"
    assert data["id"] is not None
    todo_id = data["id"]
    print("✅ Create Todo working")

    # 3. Test List
    res = requests.get(f"{base_url}/todos")
    assert res.status_code == 200
    assert len(res.json()) >= 1
    print("✅ List Todos working")

    # 4. Test Update
    res = requests.put(f"{base_url}/todos/{todo_id}", json={"completed": True})
    assert res.status_code == 200
    assert res.json()["completed"] is True
    print("✅ Update Todo working")

    # 5. Test Delete
    res = requests.delete(f"{base_url}/todos/{todo_id}")
    assert res.status_code == 200
    print("✅ Delete Todo working")

except Exception as e:
    print(f"❌ Tests failed: {e}")
    sys.exit(1)
finally:
    process.terminate()
    print("Backend stopped.")
