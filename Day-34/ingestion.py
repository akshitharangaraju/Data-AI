import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def get_gemini_embeddings():
    """
    Uses the 2026 stable gemini-embedding-001.
    Senior Tip: Default dimension is 3,072 for maximum medical precision.
    """
    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001", 
        google_api_key=os.getenv("GEMINI_API_KEY"),
        task_type="retrieval_document"
    )

def process_medical_library(folder_path="data/"):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
        return []

    documents = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            try:
                loader = PyPDFLoader(os.path.join(folder_path, file))
                documents.extend(loader.load())
            except Exception as e:
                print(f"Error loading {file}: {e}")
    
    if not documents: return []

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=120)
    return text_splitter.split_documents(documents)