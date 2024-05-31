import requests
import json

def add_dog_collar():
    url = "http://localhost:8000/devices/collars"
    data = {
        "uni_num_dog": 123,
        "name_dog": "Buddy",
        "feeling_hungry": True,
        "registration_date": "2023-01-01T00:00:00",
        "deletion_date": None,
        "health_status": "Healthy"
    }
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
    print(response.status_code, response.json())

if __name__ == "__main__":
    add_dog_collar()
