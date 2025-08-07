import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.0-flash-live-001")

# Web Search Function
def web_search(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    return response.text

# Summarize the fetched web content using Gemini
def summarize_text(text):
    prompt = f"Summarize this content in simple terms:\n{text}"
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text.strip()

# Generate the final blog or content using Gemini
def generate_content(summary):
    prompt = f"Write a blog article based on this summary:\n{summary}"
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text.strip()
