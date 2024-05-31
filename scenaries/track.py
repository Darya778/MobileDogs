import requests

def get_track():
    url = "http://localhost:8000/device/track"
    params = {
        "collar_id": 2,
        "start_time": "2024-05-31T00:00:00",
        "end_time": "2024-05-31T23:59:59"
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        print("Трек успешно получен:")
        track = response.json()
        for coordinate in track:
            print(f"Latitude: {coordinate['latitude']}, Longitude: {coordinate['longitude']}, Timestamp: {coordinate['timestamp']}")
    else:
        print(f"Ошибка: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    get_track()
