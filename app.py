from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from dotenv import load_dotenv
import os

app = Flask(__name__)
# load values from .env into environment
load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")
print(app.secret_key)

DB_NAME = "aidatlas.db"
   

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Incidents table
    c.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            description TEXT,
            lat REAL NOT NULL,
            lng REAL NOT NULL
        )
    """)

    # Users table
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('public', 'emergency'))
        )
    """)



    # Optional: Insert default emergency user
    c.execute("SELECT * FROM users WHERE username='admin'")
    if not c.fetchone():
        from werkzeug.security import generate_password_hash
        c.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            ("admin", generate_password_hash("admin123"), "emergency")
        )

    conn.commit()
    conn.close()


init_db()

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        role = request.form["role"]

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                      (username, password, role))
            conn.commit()
        except sqlite3.IntegrityError:
            return "⚠️ User already exists"
        finally:
            conn.close()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        user = conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["role"] = user["role"]

            if user["role"] == "emergency":
                return redirect(url_for("emergency_dashboard"))
            else:
                return redirect(url_for("public_dashboard"))
        else:
            return "❌ Invalid credentials"

    return render_template("login.html")


@app.route("/public")
@app.route("/public")
def public_dashboard():
    if session.get("role") != "public":
        return redirect(url_for("login"))
    return render_template("public.html")


@app.route("/emergency")
def emergency_dashboard():
    if session.get("role") != "emergency":
        return redirect(url_for("login"))
    return render_template("emergency.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))  # send to login first
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
