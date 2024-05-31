import requests

def add_coordinate():
    url = "http://localhost:8000/device/coordinates"
    headers = {"Content-Type": "application/json"}
    data = {
        "collar_id": 2,
        "latitude": 51.5074,
        "longitude": -0.1278,
        "timestamp": "2024-05-31T12:00:00"
    }
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print("Координаты успешно добавлены.")
    else:
        print(f"Ошибка: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    add_coordinate()
