from db import cursor

def user_login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    query = "SELECT * FROM user WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))

    user = cursor.fetchone()

    if user:
        print("Login successful ✅")
    else:
        print("Invalid email or password ❌")

user_login()