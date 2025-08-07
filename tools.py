import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Retrieve Gemini API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is missing in your environment variables!")

# Configure the Gemini client with the API key
genai.configure(api_key=API_KEY)

# Define the Gemini model to use
MODEL_NAME = "models/gemini-2.5-flash"  # Change as needed

def web_search(query):
    """
    Perform a simple web search by querying Google and returning the raw HTML results.
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def summarize_text(text):
    """
    Summarize text using the Google Gemini API.
    Trims the input text to 5000 characters max.
    """
    if len(text) > 5000:
        text = text[:5000]

    prompt = f"Summarize this content in simple terms:\n{text}"

    response = genai.generate_text(
        model=MODEL_NAME,
        prompt=prompt
    )
    return response.text.strip()

def generate_content(summary):
    """
    Generate a blog article based on a summary using the Google Gemini API.
    """
    prompt = f"Write a blog article based on this summary:\n{summary}"

    response = genai.generate_text(
        model=MODEL_NAME,
        prompt=prompt
    )
    return response.text.strip()
