import requests

def update_coordinate():
    url = "http://localhost:8000/device/coordinates/4"
    headers = {"Content-Type": "application/json"}
    data = {
        "latitude": 40.7128,
        "longitude": -74.0060
    }
    response = requests.put(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print("Координаты успешно обновлены.")
    else:
        print(f"Ошибка: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    update_coordinate()
