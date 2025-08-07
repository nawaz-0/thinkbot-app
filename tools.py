from dotenv import load_dotenv
import os
import requests
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Get the API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in environment!")

# Configure Gemini with the API key
genai.configure(api_key=api_key)

# Define the model name (update if needed)
MODEL_NAME = "models/gemini-2.5-flash"

# Web Search Function
def web_search(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    return response.text

# Summarize the fetched web content using Gemini
def summarize_text(text):
    if len(text) > 5000:
        text = text[:5000]

    prompt = f"Summarize this content in simple terms:\n{text}"

    # Correct usage: call generate_content through genai client
    response = genai.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text.strip()

# Generate the final blog or content using Gemini
def generate_content(summary):
    prompt = f"Write a blog article based on this summary:\n{summary}"

    response = genai.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text.strip()

