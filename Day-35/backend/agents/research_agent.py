import os
from typing import Dict, Any, List

from tools.tavily_search import tavily_search
from tools.image_search import search_images


class ResearchAgent:
    """
    Research Agent

    Responsibilities:
    - Perform web research using Tavily
    - Retrieve relevant context
    - Fetch supporting images using SerpAPI
    """

    def __init__(self):
        self.role = "Research Specialist"
        self.goal = "Find reliable information and supporting material for the query."

    def run(self, query: str) -> Dict[str, Any]:
        """
        Execute research for a given user query.
        """

        # -------- STEP 1: Web Research --------
        research_results = tavily_search(query)

        summary = research_results.get("summary", "")
        notes = research_results.get("notes", [])
        sources = research_results.get("sources", [])
        retrieved_context = research_results.get("context", "")

        # -------- STEP 2: Image Retrieval --------
        images: List[str] = search_images(query)

        # -------- STEP 3: Return Research Package --------
        return {
            "agent": "Research Agent",
            "role": self.role,
            "goal": self.goal,
            "summary": summary,
            "notes": notes,
            "sources": sources,
            "context": retrieved_context,
            "images": images
        }