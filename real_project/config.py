import os
from dotenv import load_dotenv

load_dotenv()

# Look for the Gemini key instead
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("ERROR: GEMINI_API_KEY not found in your .env file!")