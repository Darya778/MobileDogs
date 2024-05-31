import requests
import json

url = "http://localhost:8000/users/users"
data = {
    "login": "newuser",
    "password": "password123",
    "email": "newuser@example.com",
    "gender": "male",
    "phone": "1234567890",
    "birthday": "2000-01-01T00:00:00",
    "registration_date": "2023-01-01T00:00:00",
    "deletion_date": None
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())

