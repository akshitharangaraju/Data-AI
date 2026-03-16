import os
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
from docx import Document

# 1. Initialize Pinecone (Use environment variables for safety!)
# API_KEY = os.getenv("PINECONE_API_KEY") 
API_KEY = "pcsk_6hsZqQ_CPC3JAZmFfyVFTMbDGMiBPW4avbAwsVmUkioKhsuZqqNxWo7NRJYUkqwtyKtHGu" # REPLACEME: Use a new key immediately
pc = Pinecone(api_key=API_KEY)

# 2. Setup Index
index_name = "demo-index"
dimension = 384  # Matches 'all-MiniLM-L6-v2' output size

if index_name not in [idx.name for idx in pc.list_indexes()]:
    print(f"Creating index: {index_name}...")
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(index_name)

# 3. Load Embedding Model
# This model turns text into 384-dimensional vectors
model = SentenceTransformer("all-MiniLM-L6-v2")

# 4. Helper Function to extract text from files
def extract_text(file_path):
    text = ""
    if file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

print("Setup Complete. Pinecone Index and Model are ready.")