from db import cursor, conn

def delete_user():
    user_id = int(input("Enter User ID to delete: "))

    query = "DELETE FROM user WHERE id = %s"

    cursor.execute(query, (user_id,))
    conn.commit()

    if cursor.rowcount:
        print("User deleted successfully ✅")
    else:
        print("User not found ❌")
delete_user()