import requests

def delete_task(task_id):
    url = f"http://localhost:8000/tasks/tasks/{task_id}"
    response = requests.delete(url)
    print(response.status_code, response.json())

if __name__ == "__main__":
    task_id = 7  
    delete_task(task_id)
