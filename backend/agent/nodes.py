from langchain_openrouter import ChatOpenRouter

from backend.agent.state import AgentState
from backend.core.config import OPENROUTER_API_KEY


llm = ChatOpenRouter(
    model="openai/gpt-4o-mini",
    api_key=OPENROUTER_API_KEY,
    temperature=0,
)


# Node
def call_model(state: AgentState):
    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }
