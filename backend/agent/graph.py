import asyncio

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openrouter import ChatOpenRouter

from backend.agent.state import AgentState
from backend.agent.mcp_client import get_mcp_tools
from backend.core.config import OPENROUTER_API_KEY


llm = ChatOpenRouter(
    model="openai/gpt-4o-mini",
    api_key=OPENROUTER_API_KEY,
    temperature=0,
)


async def build_graph():

    # Discover tools from our MCP server
    tools = await get_mcp_tools()

    # Give the LLM knowledge of the available tools
    llm_with_tools = llm.bind_tools(tools)

    def call_model(state: AgentState):

        response = llm_with_tools.invoke(
            state["messages"]
        )

        return {
            "messages": [response]
        }

    graph = StateGraph(AgentState)

    graph.add_node("agent", call_model)
    graph.add_node("tools", ToolNode(tools))

    graph.add_edge(START, "agent")

    graph.add_conditional_edges(
        "agent",
        tools_condition,
    )

    graph.add_edge("tools", "agent")

    return graph.compile()


agent = asyncio.run(build_graph())
