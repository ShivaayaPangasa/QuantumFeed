from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
    NEWS_API_BASE_URL = "https://content.guardianapis.com/"