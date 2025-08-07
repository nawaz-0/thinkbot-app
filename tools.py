import os
import requests
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY missing!")

# Create GenAI client
client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-2.5-flash"  # Use model name without 'models/' prefix now

def web_search(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def summarize_text(text):
    if len(text) > 5000:
        text = text[:5000]
    prompt = f"Summarize this content in simple terms:\n{text}"
    
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text.strip()

def generate_content(summary):
    prompt = f"Write a blog article based on this summary:\n{summary}"
    
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text.strip()

