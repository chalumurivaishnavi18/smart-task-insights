import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="smart_task_insights"
    )

    if conn.is_connected():
        print("Connected to MySQL ✅")

        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db = cursor.fetchone()

        print("Connected to DB:", db)

except Exception as e:
    print("Error:", e)