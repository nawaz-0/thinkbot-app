from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# Load .env and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the correct model
model = genai.GenerativeModel("models/gemini-pro")  # ✅ Supported for generate_content

def web_search(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()[:3000]

def summarize_text(text):
    if len(text) > 5000:
        text = text[:5000]
    prompt = f"Summarize this content in simple terms:\n{text}"
    response = model.generate_content(prompt)  # ✅ Use generate_content directly
    return response.text.strip()

def generate_content(summary):
    prompt = f"Write a blog article based on this summary:\n{summary}"
    response = model.generate_content(prompt)  # ✅ Use generate_content directly
    return response.text.strip()
