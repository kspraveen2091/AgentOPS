import asyncio

from backend.agent.mcp_client import get_mcp_tools


async def main():

    tools = await get_mcp_tools()

    print("\nAvailable MCP tools:\n")

    for tool in tools:
        print(f"Name: {tool.name}")
        print(f"Description: {tool.description}")
        print()


if __name__ == "__main__":
    asyncio.run(main())
