import requests

def get_all_collars():
    url = "http://localhost:8000/device/getallcollars/"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Список всех ошейников:")
        collars = response.json()
        for index, collar in enumerate(collars, start=1):
            print(f"Ошейник {index}:")
            print(f"Name: {collar['name_dog']}")
            print(f"Registration Date: {collar['registration_date']}")
            print()  # Пустая строка между ошейниками
    else:
        print(f"Ошибка: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    get_all_collars()

