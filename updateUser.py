from db import cursor, conn

def update_user():
    user_id = int(input("Enter User ID to update: "))

    firstName = input("Enter new First Name: ")
    lastName = input("Enter new Last Name: ")
    email = input("Enter new Email: ")

    query = """
    UPDATE user 
    SET firstName = %s, lastName = %s, email = %s
    WHERE id = %s
    """

    try:
        cursor.execute(query, (firstName, lastName, email, user_id))
        conn.commit()

        if cursor.rowcount:
            print("User updated successfully ✅")
        else:
            print("User not found ❌")

    except Exception as e:
        print("Error:", e)

update_user()