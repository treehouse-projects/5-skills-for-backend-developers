from flask import Flask, render_template # Modified
import sqlite3 as sql
import json # Added
app = Flask(__name__)

def articles():
    query = "SELECT * FROM articles"
    connection = sql.connect("test.db")
    connection.row_factory = sql.Row
    result = connection.cursor().execute(query)
    records = result.fetchall()
    connection.close()
    return records

@app.route('/')
def main_page():
    records = articles()
    return render_template("main.html", articles = records)

# New
@app.route('/articles.json')
def articles_json():
    return json.dumps([dict(row) for row in articles()])

app.run()
