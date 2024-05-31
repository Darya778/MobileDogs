import requests
import json

def update_task(task_id):
    url = f"http://localhost:8000/tasks/tasks/{task_id}"
    data = {
        "task_text": "Complete the updated training module.",
        "confirm": True
    }
    response = requests.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
    print(response.status_code, response.json())

if __name__ == "__main__":
    task_id = 7 
    update_task(task_id)
