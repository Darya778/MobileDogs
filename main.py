from fastapi import FastAPI, HTTPException

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
