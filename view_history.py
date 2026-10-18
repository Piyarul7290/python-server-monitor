
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT id, checked_at, cpu, memory, disk, status
    FROM health_history
    ORDER BY id DESC
""")

records = cursor.fetchall()

print("\nSERVER MONITORING HISTORY")
print("-" * 70)

if records:
    for record in records:
        print(f"ID: {record[0]}")
        print(f"Time: {record[1]}")
        print(f"CPU: {record[2]}%")
        print(f"Memory: {record[3]}%")
        print(f"Disk: {record[4]}%")
        print(f"Status: {record[5]}")
        print("-" * 70)
else:
    print("No monitoring records found.")

conn.close()
