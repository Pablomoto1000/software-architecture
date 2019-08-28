from flask import render_template
from app import app 
import sqlite3
from flask import jsonify

@app.route('/') 
def home():
    return render_template("home.html")

@app.route('/users/list')
def list():
    con = sqlite3.connect('app/software-architecture.db')
    print("Opened database successfully")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    return render_template("list.html", rows = rows)

@app.route('/api/v1/users/')
def summary():
    con = sqlite3.connect('app/software-architecture.db')
    print("Opened database successfully")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    data = []
    
    for row in rows:
        data.append([x for x in row]) # or simply data.append(list(row))

    return jsonify(data)