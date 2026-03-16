import os
from serpapi import GoogleSearch


def search_images(query: str):

    api_key = os.getenv("SERPAPI_KEY")

    params = {
        "engine": "google_images",
        "q": query + " product photo",
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    images = []

    if "images_results" in results:
        for img in results["images_results"][:4]:
            images.append(img["original"])

    return images