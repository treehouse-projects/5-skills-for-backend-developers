from flask import Flask, escape, render_template, jsonify
import sqlite3 as sql
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

@app.route('/articles.json')
def articles_json():
    article_list = []
    for record in articles():
        article_list.append({'title': record['title'], 'content': record['content']})
    return jsonify(article_list)

app.run()
