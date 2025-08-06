from dotenv import load_dotenv
import os
from openai import OpenAI
import requests

load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def web_search(query):
    # Simple dummy web search logic (replace with real search API later)
    return f"Search results for: {query}\n1. Article about {query}\n2. Blog about {query}\n3. News on {query}"

def summarize_text(text):
    prompt = f"Summarize this text for a blog:\n\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content

def generate_content(topic):
    prompt = f"Write a 300-word engaging blog on the topic:\n'{topic}'\n\nMake it suitable for social media or a personal website."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content
