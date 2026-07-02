import re
from textblob import TextBlob
from transformers import pipeline
import tiktoken
from config import Config

fake_news_model = pipeline("text-classification", model="mrm8488/bert-mini-finetuned-fake-news")
fake_news_sites = ["beforeitsnews.com", "infowars.com", "yournewswire.com"]
fact_check_api_key = Config.GOOGLE_API_KEY

def clean_text(text):
    text = re.sub(r'<[^>]+>', '', text)  # HTML tags
    text = re.sub(r'http\S+', '', text)  # URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Special characters
    return text.lower().strip()

def check_source_credibility(url):
    for site in fake_news_sites:
        if site in url:
            return 100
    return 0 # Assume reputable if not in list

def check_clickbait(title):
    clickbait_keywords = ["shocking", "you won’t believe", "must see", "amazing", "secret", "unbelievable"]
    return 100 if any(word in title.lower() for word in clickbait_keywords) else 0

def cross_check(title):
    # TBD - Google fact check API
    return 0

def check_ai_gen(text):
    enc = tiktoken.encoding_for_model("gpt-4")
    token_count = len(enc.encode(text))
    return 100 if token_count > 1000 else 0

def analyze_sentiment(text):
    sentiment_score = TextBlob(text).sentiment.polarity
    return abs(sentiment_score)*100 # Higher polarity = Higher bias

# TBD - Add custom Regression model to identify fake articles

"""
Distribution for scoring system:
1--> Source credibility - 25%
2--> Clickbait title - 15%
3--> Cross-check with API - 30%
4--> Check for AI generated content - 15%
5--> Check for bias and sentiment analysis - 15%
Lower score = More trustworthy (<50 then flag)
"""

def calculate_fakescore(title, text, url):
    credibility_score = check_source_credibility(url) * 0.25
    clickbait_score = check_clickbait(title) * 0.15
    cross_check_score = cross_check(title) * 0.30
    ai_gen_score = check_ai_gen(text) * 0.15
    sentiment_score = analyze_sentiment(text) * 0.15
    final_score = (credibility_score + clickbait_score + cross_check_score + ai_gen_score + sentiment_score)
    return round(final_score, 2)