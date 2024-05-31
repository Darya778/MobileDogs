import requests

def delete_dog_collar(collar_id):
    url = f"http://localhost:8000/devices/collars/{collar_id}"
    response = requests.delete(url)
    print(response.status_code, response.json())

if __name__ == "__main__":
    collar_id = 19
    delete_dog_collar(collar_id)
