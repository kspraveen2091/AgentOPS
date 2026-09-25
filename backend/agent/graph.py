from langgraph.graph import StateGraph, START, END

from backend.agent.state import AgentState
from backend.agent.nodes import call_model


def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("call_model", call_model)

    graph.add_edge(START, "call_model")
    graph.add_edge("call_model", END)

    return graph.compile()


agent = build_graph()
