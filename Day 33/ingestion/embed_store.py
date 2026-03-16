from google import genai
import os
from pinecone import Pinecone
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("INDEX_NAME"))

from google.genai import types

def get_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(output_dimensionality=1024)
    )
    return result.embeddings[0].values

def store_chunks(chunks, source=""):
    vectors = []
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        vector_id = f"{source}_{i}"
        vectors.append(
            {"id": vector_id, "values": embedding, "metadata": {"text": chunk, "source": source}}
        )
    index.upsert(vectors)