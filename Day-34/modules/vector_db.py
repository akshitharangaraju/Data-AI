import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

def initialize_vector_db(chunks, embeddings):
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    idx_name = os.getenv("PINECONE_INDEX_NAME", "cardio-ai-2026").lower().replace("_", "-")

    # Recreate index if dimension is not 3072
    if idx_name in [idx.name for idx in pc.list_indexes()]:
        desc = pc.describe_index(idx_name)
        if desc.dimension != 3072:
            pc.delete_index(idx_name)

    if idx_name not in [idx.name for idx in pc.list_indexes()]:
        pc.create_index(
            name=idx_name,
            dimension=3072, # 2026 STABLE STANDARD
            metric='cosine',
            spec=ServerlessSpec(cloud='aws', region='us-east-1')
        )
    
    return PineconeVectorStore.from_documents(chunks, embeddings, index_name=idx_name)