from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

DB_NAME = "aidatlas.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            description TEXT,
            lat REAL NOT NULL,
            lng REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_incident", methods=["POST"])
def add_incident():
    data = request.get_json(force=True)
    incident_type = data.get("type")
    description   = data.get("description", "")
    lat           = float(data.get("lat"))
    lng           = float(data.get("lng"))

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "INSERT INTO incidents (type, description, lat, lng) VALUES (?, ?, ?, ?)",
        (incident_type, description, lat, lng)
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

@app.route("/get_incidents", methods=["GET"])
def get_incidents():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, type, description, lat, lng FROM incidents")
    rows = c.fetchall()
    conn.close()
    return jsonify([
        {"id": r[0], "type": r[1], "description": r[2], "lat": r[3], "lng": r[4]}
        for r in rows
    ])

if __name__ == "__main__":
    app.run(debug=True)
