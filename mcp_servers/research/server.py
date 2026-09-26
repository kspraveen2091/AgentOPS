import os

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient


load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is not configured")


tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

mcp = FastMCP("Research")


@mcp.tool()
def search_web(query: str) -> str:
    """
    Search the web for current information.

    Args:
        query: The search query.
    """

    response = tavily_client.search(
        query=query,
        max_results=5,
    )

    results = response.get("results", [])

    if not results:
        return "No search results found."

    formatted_results = []

    for result in results:
        formatted_results.append(
            f"Title: {result.get('title', '')}\n"
            f"URL: {result.get('url', '')}\n"
            f"Content: {result.get('content', '')}\n"
        )

    return "\n---\n".join(formatted_results)


if __name__ == "__main__":
    mcp.run()
