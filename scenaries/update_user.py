import requests
import json

url = "http://localhost:8000/users/users/12" 
data = {
    "login": "updatedlogin",
    "email": "updatedemail@example.com",
    "gender": "female",
    "phone": "0987654321",
    "birthday": "1990-01-01T00:00:00",
    "registration_date": "2023-01-01T00:00:00",
    "deletion_date": None
}

response = requests.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())
