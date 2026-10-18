
import psutil
import sqlite3
from datetime import datetime

DB_NAME = "monitor.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS health_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                checked_at TEXT NOT NULL,
                cpu REAL NOT NULL,
                memory REAL NOT NULL,
                disk REAL NOT NULL,
                status TEXT NOT NULL
            )
        """)


def check_server_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    warnings = []

    if cpu > 80:
        warnings.append("High CPU usage!")

    if memory > 72:
        warnings.append("High memory usage!")

    if disk > 81:
        warnings.append("High disk usage!")

    status = "WARNING" if warnings else "HEALTHY"

    print("\nSERVER HEALTH REPORT")
    print("--------------------")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print(f"Overall Status: {status}")

    for warning in warnings:
        print(f"Reason: {warning}")

    # Save the monitoring result in SQLite
    checked_at = datetime.now().isoformat(timespec="seconds")

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            INSERT INTO health_history
            (checked_at, cpu, memory, disk, status)
            VALUES (?, ?, ?, ?, ?)
        """, (checked_at, cpu, memory, disk, status))

    print("Monitoring result saved to database.")


if __name__ == "__main__":
    init_db()
    check_server_health()
