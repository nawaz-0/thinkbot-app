from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os
import requests
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# Web Search Function
def web_search(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()[:3000]  # Optional: limit to 3000 characters

# Summarize the fetched web content using Gemini
def summarize_text(text):
    if len(text) > 5000:
    text = text[:5000]
    prompt = f"Summarize this content in simple terms:\n{text}"
    model = genai.GenerativeModel("models/gemini-2.0-pro")  # ✅ CORRECTED
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text.strip()

# Generate the final blog or content using Gemini
def generate_content(summary):
    prompt = f"Write a blog article based on this summary:\n{summary}"
    model = genai.GenerativeModel("models/gemini-2.0-pro")  # ✅ CORRECTED
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text.strip()
