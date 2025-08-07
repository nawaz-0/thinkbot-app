import google.generativeai as genai

# Replace this with your real API key or load from .env
genai.configure(api_key="AIzaSyD8QAK99ElC9ePhMnh5Pry7ba_6b_k75jA")

models = genai.list_models()

for model in models:
    print(f"Model name: {model.name}")
    print(f"  Supported generation methods: {model.supported_generation_methods}")
    print("-" * 40)
