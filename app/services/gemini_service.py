import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

client = genai.Client(
    api_key=GEMINI_API_KEY,
    http_options=types.HttpOptions(
        timeout=30000,
        retry_options=types.HttpRetryOptions(
            attempts=2,
            initial_delay=1,
            max_delay=2
        )
    )
)



def generate_response(message: str, history: list = None):

    contents = history or []

    contents.append(
        {
            "role": "user",
            "parts": [{"text": message}]
        }
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=contents,
        config=types.GenerateContentConfig(
            max_output_tokens=256
        )
    )

    return response.text