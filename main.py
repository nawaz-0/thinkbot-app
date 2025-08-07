from tools import web_search, summarize_text, generate_content

def main():
    query = "latest advances in AI 2025"
    print("Performing web search...")
    search_results = web_search(query)

    print("Summarizing content...")
    summary = summarize_text(search_results)
    print("Summary:")
    print(summary)

    print("Generating blog content...")
    blog_article = generate_content(summary)
    print("Generated Blog Article:")
    print(blog_article)


if __name__ == "__main__":
    main()
