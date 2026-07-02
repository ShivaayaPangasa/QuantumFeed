from flask import Flask
import sqlite3
import datetime
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from .routes import main
    app.register_blueprint(main)

    return app

def get_articles():
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "services", "articles.db"))
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT title, summary, published_date FROM articles")
    articles = cursor.fetchall()
    conn.close()

    return [
        {"title": row[0], "summary": row[1], "published_date": row[2]}
        for row in articles
    ]

def format_date(date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        return date_obj.strftime("%B %d, %Y")