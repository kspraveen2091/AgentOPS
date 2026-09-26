from langchain_mcp_adapters.client import MultiServerMCPClient


client = MultiServerMCPClient(
    {
        "research": {
            "command": "python",
            "args": [
                "mcp_servers/research/server.py"
            ],
            "transport": "stdio",
        }
    }
)


async def get_mcp_tools():
    tools = await client.get_tools()

    print("MCP tools discovered:")

    for tool in tools:
        print(f"- {tool.name}")

    return tools
