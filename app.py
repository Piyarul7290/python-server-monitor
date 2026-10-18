
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DB_NAME = "database.db"


def get_history():
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("""
            SELECT id, checked_at, cpu, memory, disk, status
            FROM health_history
            ORDER BY id DESC
            LIMIT 10
        """).fetchall()

    return rows


@app.route("/")
def dashboard():
    history = get_history()
    latest = history[0] if history else None

    return render_template(
        "dashboard.html",
        history=history,
        latest=latest
    )


if __name__ == "__main__":
    app.run(debug=True)
