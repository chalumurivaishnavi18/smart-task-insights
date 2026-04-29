from db import cursor, conn

def create_user():
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    query = "INSERT INTO user (firstName, lastName, email, password) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (firstName, lastName, email, password))

    conn.commit()  # ✅ fixed

    print("User created successfully ✅")

create_user()
