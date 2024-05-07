from fastapi import FastAPI, HTTPException
from flask import Flask
# выбрать

app = FastAPI()

# there should be a connection to the BD
# ...

# POST request для регистрации пользователей
@app.post("/users/register")
def register_user(login: str, password: str, email: str, gender: str, phone: str, birthday: str):
  
    # ПОДКЛЮЧЕНИЕ К БД !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    cnx = mysql.connector.connect(user=bdUser, password=bdPasswd,
                                   host='localhost',
                                  database=bdName)
    cursor = cnx.cursor()
  
    # Проверяем, есть ли такой логин уже в базе
    cursor.execute(f"SELECT 1 FROM users WHERE login = {login}")
    if cursor.fetchone():
        conn.close()
        raise Exception("404: This login is already registered")

    # Если логин уникален, добавляем его в базу
    cursor.execute(f"INSERT INTO users (login, password, email, gender, phone, birthday) VALUES ({login}, {password}, {email}, {gender}, {phone}, {birthday})")
    conn.commit()
    conn.close()

  
    #users_db[id_user] = {
    #    "login": login,
    #    "password": password,
    #    "email": email,
    #    "gender": gender,
    #    "phone": phone,
    #    "birthday": birthday
    #}
    return {"message": "User registered successfully"}


# POST request для регистрации ошейников
@app.post("/collars/register")
def register_collar(uni_num_dog: int, name_dog: str, temp: float, feeling_hungry: bool, health_status: str):

    # ПОДКЛЮЧЕНИЕ К БД !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    cnx = mysql.connector.connect(user=bdUser, password=bdPasswd,
                                   host='localhost',
                                  database=bdName)
    cursor = cnx.cursor()

    # Проверяем, есть ли такой номер ошейника в базе
    cursor.execute(f"SELECT 1 FROM dogs_collar WHERE uni_num_dog = {uni_num_dog}")
    if cursor.fetchone():
        conn.close()
        raise Exception("404: This dog`s collar is already registered")

    # Если номер ошейника уникален, добавляем его в базу
    cursor.execute(f"INSERT INTO dogs_collar (uni_num_dog, name_dog, temp, feeling_hungry, health_status) VALUES ({uni_num_dog}, {name_dog}, {temp}, {feeling_hungry}, {health_status})")
    conn.commit()
    conn.close()
  
    #collars_db[id_collar] = {
    #    "uni_num_dog": uni_num_dog,
    #    "name_dog": name_dog,
    #    "temp": temp,
    #    "feeling_hungry": feeling_hungry,
    #    "health_status": health_status
    #}
    return {"message": "Collar registered successfully"}
