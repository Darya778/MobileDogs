import requests
import json
from datetime import datetime

def add_task():
    url = "http://localhost:8000/tasks/tasks"
    data = {
        "id_user_13": 1,
        "id_user_14": 2,
        "id_task": 7,
        "confirm": False,
        "send_date": datetime.utcnow().isoformat(),
        "completion_date": None,
        "task_text": "Complete the training module."
    }
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
    print(response.status_code, response.json())

if __name__ == "__main__":
    add_task()
