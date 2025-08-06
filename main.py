import streamlit as st
from tools import web_search, summarize_text, generate_content
import json
import os

st.set_page_config(page_title="🧠 ThinkBot", layout="centered")
st.title("🧠 ThinkBot – Your Personal AI Assistant")

st.markdown("Type a task like:\n- 'Write a blog on current AI trends'\n- 'Create Instagram content about EV tech'")

task = st.text_input("What do you want me to do?", placeholder="e.g., Write a blog on trending AI tools")

if st.button("Run Task"):
    if task:
        with st.spinner("Thinking..."):
            st.info("🔍 Searching the web...")
            search_results = web_search(task)

            st.info("🧠 Summarizing content...")
            summary = summarize_text(search_results)

            st.info("✍️ Writing blog...")
            blog = generate_content(summary)

            st.success("✅ Done! Here's your result:")
            st.subheader("📄 Blog Content")
            st.write(blog)

            # Save to memory
            if os.path.exists("memory.json"):
                with open("memory.json", "r") as f:
                    memory = json.load(f)
            else:
                memory = []

            memory.append({"task": task, "blog": blog})

            with open("memory.json", "w") as f:
                json.dump(memory, f, indent=4)

    else:
        st.warning("Please enter a task to run.")
