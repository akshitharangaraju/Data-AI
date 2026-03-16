class WriterAgent:

    def write_answer(self, query, research_data, images):

        summary = research_data.get("summary", "")
        sources = research_data.get("sources", [])

        explanation = f"""
The system analyzed multiple sources using the Research Agent.

Summary of research:
{summary}

Sources:
{", ".join(sources)}
"""

        answer = f"Recommended answer for: {query}"

        return {
            "answer": answer,
            "explanation": explanation,
            "images": images
        }