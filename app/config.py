import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")
CHROMA_PATH = os.getenv("CHROMA_PATH", "chroma_db")
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/ask")