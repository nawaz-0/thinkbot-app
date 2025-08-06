load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def web_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
    texts = [r.get_text() for r in results[:5]]
    return "\n".join(texts)

def summarize_text(text):
    prompt = f"Summarize this text for a blog:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response['choices'][0]['message']['content']

def generate_content(topic):
    prompt = f"Write a 300-word engaging blog on the topic:\n'{topic}'\n\nMake it suitable for social media or personal website."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response['choices'][0]['message']['content']
