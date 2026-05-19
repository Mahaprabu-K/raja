from flask import Flask, render_template, request, jsonify
import pyodbc

app = Flask(__name__)

# =========================================
# SQL SERVER CONNECTION
# =========================================
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=KISHORE\\SQLEXPRESS;'
    'DATABASE=sampledb;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# =========================================
# CREATE TABLE
# =========================================
cursor.execute("""
IF NOT EXISTS (
    SELECT * FROM sysobjects
    WHERE name='users' AND xtype='U'
)
CREATE TABLE users (
    id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(100),
    age INT
)
""")

conn.commit()

# =========================================
# HOME PAGE
# =========================================
@app.route("/")
def home():
    return render_template("index.html")


# =========================================
# SAVE DATA
# =========================================
@app.route("/save", methods=["POST"])
def save_data():

    data = request.get_json()

    name = data["name"]
    age = data["age"]

    cursor.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)",
        (name, age)
    )

    conn.commit()

    return jsonify({
        "messag": "Data Saved Successfully"
    })


# =========================================
# RUN APP
# =========================================
if __name__ == "__main__":
    app.run(debug=True)