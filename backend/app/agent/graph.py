from langgraph.graph import StateGraph, END #type: ignore
from app.agent.state import AgentState
from app.agent.router import router_node
from app.agent.tools.retrieval import retrieval_node
from app.agent.tools.summerizer import summarizer_node
from app.agent.tools.calculer import calculator_node
from app.agent.answer import answer_node


def create_agent_graph():
    graph = StateGraph(AgentState)

    graph.add_node("router", router_node)
    graph.add_node("retrieval", retrieval_node)
    graph.add_node("summarizer", summarizer_node)
    graph.add_node("calculator", calculator_node)
    graph.add_node("answer", answer_node)

    graph.set_entry_point("router")

    graph.add_conditional_edges(
        "router",
        lambda state: state["tool"],
        {
            "retrieval": "retrieval",
            "summarize": "summarizer",
            "calculator": "calculator"
        }
    )

    graph.add_edge("retrieval", "answer")
    graph.add_edge("summarizer", "answer")
    graph.add_edge("calculator", "answer")
    graph.add_edge("answer", END)

    return graph.compile()


agent = create_agent_graph()