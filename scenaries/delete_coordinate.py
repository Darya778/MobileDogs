import requests

def delete_coordinate():
    url = "http://localhost:8000/device/coordinates/4"
    response = requests.delete(url)
    
    if response.status_code == 200:
        print("Координаты успешно удалены.")
    else:
        print(f"Ошибка: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    delete_coordinate()
