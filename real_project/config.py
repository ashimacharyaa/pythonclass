import os
from dotenv import load_dotenv

load_dotenv()

# Look for the Gemini key instead
GEMINI_API_KEY = os.getenv("----")

if not GEMINI_API_KEY:
    raise ValueError("ERROR:-----!")
