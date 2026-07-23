"""
Gemini LLM Wrapper
"""

from google import genai
from app.config import GEMINI_API_KEY, MODEL_NAME

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )

client = genai.Client(api_key=GEMINI_API_KEY)


def generate(prompt: str) -> str:
    """
    Generate an answer using Gemini.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text