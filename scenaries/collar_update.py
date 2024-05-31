import requests
import json

def update_dog_collar(collar_id):
    url = f"http://localhost:8000/devices/collars/{collar_id}"
    data = {
        "name_dog": "Buddy Updated",
        "feeling_hungry": False,
        "health_status": "Recovered"
    }
    response = requests.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
    print(response.status_code, response.json())

if __name__ == "__main__":
    collar_id = 19
    update_dog_collar(collar_id)
