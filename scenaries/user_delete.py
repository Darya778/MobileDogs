import requests

url = "http://localhost:8000/users/users/12"

response = requests.delete(url)
print(response.status_code, response.json())

