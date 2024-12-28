import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

try:
    cursor.execute("BEGIN TRANSACTION")

    cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ("John Doe", 25))

    cursor.execute("UPDATE employees SET age = ? WHERE id = ?", (30, 1))

    conn.commit()

except Exception as e:
    conn.rollback()
    print(f"Ошибка: {e}")

finally:
    cursor.close()
    conn.close()



