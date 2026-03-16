def tavily_search(query: str):

    summary = f"""
    This is a simulated research result for the query: {query}.

    The system searched multiple sources and generated a summary
    using the research agent.
    """

    sources = [
        "https://example.com/article1",
        "https://example.com/article2",
        "https://example.com/article3"
    ]

    return {
        "summary": summary,
        "sources": sources
    }