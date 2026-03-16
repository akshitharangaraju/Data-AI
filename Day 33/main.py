import os
import sys
from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from ingestion.embed_store import store_chunks
from chatbot.chatbot import start_chat

def index_documents():
    data_folder = "data"
    if not os.path.exists(data_folder):
        print(f"Data folder '{data_folder}' not found.")
        return
        
    for file in os.listdir(data_folder):
        if file.endswith(".pdf"):
            path = os.path.join(data_folder, file)
            print("Processing:", file)
            text = load_pdf(path)
            chunks = chunk_text(text)
            print("Chunks:", len(chunks))
            store_chunks(chunks, source=file)
    print("All documents stored in Pinecone!")

if __name__ == "__main__":
    print("1. Index documents into Vector DB")
    print("2. Start Chatbot")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        index_documents()
    elif choice == '2':
        start_chat()
    else:
        print("Invalid choice.")
        sys.exit(1)