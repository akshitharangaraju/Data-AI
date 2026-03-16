from ingestion.embed_store import get_embedding, index

def search(query):
    query_embedding = get_embedding(query)
    results = index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True
    )

    contexts = []
    for match in results["matches"]:
        contexts.append(match["metadata"]["text"])

    return contexts