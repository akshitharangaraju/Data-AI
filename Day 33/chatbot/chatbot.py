from retrieval.search import search
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(query):
    contexts = search(query)
    context_str = "\n\n".join(contexts)
    
    prompt = f"""You are a helpful Healthcare Knowledge Chatbot. 
Answer the user's question strictly based on the provided healthcare document context. 
If the answer is not in the context, clearly say "I don't know based on the provided documents."

Context:
{context_str}

Question:
{query}

Answer:"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def start_chat():
    print("========================================")
    print("Welcome to the Healthcare Knowledge Chatbot")
    print("========================================")
    print("Ask a healthcare query, or type 'exit' or 'quit' to stop.")
    
    while True:
        query = input("\nYou: ")
        if query.lower() in ['exit', 'quit']:
            print("Take care! Goodbye.")
            break
        
        response = generate_response(query)
        print(f"\nBot: {response}")
