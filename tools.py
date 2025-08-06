import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env (for local testing)
load_dotenv()

# Get OpenAI API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Web Search Function
def web_search(query):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    return response.text

# Summarize the fetched web content
def summarize_text(text):
    prompt = f"Summarize this content in simple terms:\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()

# Generate the final blog or content
def generate_content(summary):
    prompt = f"Write a blog article based on this summary:\n{summary}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()
