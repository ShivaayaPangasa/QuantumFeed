import requests
import sqlite3
from transformers import pipeline
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import config
#from apscheduler.schedulers.background import BackgroundScheduler

NEWS_API_KEY = "a7f6a2f6-cb3a-45e3-ba24-d5a51e8579b4"
BASE_URL = "https://content.guardianapis.com/search?page=2&q=debate&api-key={}".format(NEWS_API_KEY)

# --Function to fetch news from The Guardian API--
def fetch_news(query="technology", num_articles=10):
    params = {
        "section": query,
        "show-fields": "body",  # Full article
        "order-by": "newest",
        "page-size": num_articles
    }
    
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Error fetching data:", response.json())
        return []

    data = response.json()
    print("Full API Response:", response.json())
    print("API Response:", data)
    if data.get("response", {}).get("status") != "ok":
        return []

    articles = data["response"].get("results", [])
    
    return [
        {
            "title": article.get("webTitle", "No Title"),
            "body": article.get("fields", {}).get("body", "No Content"),
            "published_date": article.get("webPublicationDate", "No Date")
        }
        for article in articles
    ]

summarizer = pipeline("summarization", model="facebook/bart-large-cnn") #Initialize BART for NLP
fetched_articles = fetch_news("technology", 10)
print("Fetched Articles:", fetched_articles)


# --Connect to SQLite Database--
db_path = r"C:\Users\Hritvika\Documents\GitHub\QuantumFeed\app\services\articles.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        body TEXT NOT NULL,
        summary TEXT NOT NULL,
        published_date TEXT NOT NULL
    );
""")
conn.commit()

print("Database and table created.")

# --Insert Data into Database after Summarization--
for art in fetched_articles:
    summary = summarizer(art["body"][0:1024], max_length=150, min_length=50, do_sample=False)[0]["summary_text"]
    cursor.execute(
        "INSERT OR IGNORE INTO articles (title, body, summary, published_date) VALUES (?, ?, ?, ?)",
        (art["title"], art["body"], summary, art["published_date"])
    )
conn.commit()

print("Data inserted successfully with summaries!")

# --Fetch & Print Data from SQLite--
cursor.execute("SELECT id, title, summary, published_date FROM articles")
rows = cursor.fetchall()

print("\nArticles Table with Summaries:")
print("ID | Title | Summary | Published Date")
print("-" * 120)
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

# TBD - Add scheduler (daily).
# TBD - Integrate the fake score module