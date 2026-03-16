import os
import requests


def tavily_search(query: str):

    api_key = os.getenv("TAVILY_API_KEY")

    url = "https://api.tavily.com/search"

    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": "advanced",
        "max_results": 5
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()

        results = data.get("results", [])

        summaries = []
        sources = []

        for r in results:
            summaries.append(r.get("content", ""))
            sources.append(r.get("url", ""))

        return {
            "summary": "\n".join(summaries),
            "sources": sources,
            "images": []
        }

    except Exception as e:
        return {
            "summary": "Search failed",
            "sources": [],
            "images": [],
            "error": str(e)
        }