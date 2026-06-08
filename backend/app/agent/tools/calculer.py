from app.config import get_settings
from app.agent.state import AgentState
from app.agent.llm import get_llm

settings = get_settings()
llm = get_llm()


CalculatorPrompt = """
You are a calculator assistant. Given a user query, perform the necessary calculations and provide the answer
Query: {query}
"""


def calculator_node(state: AgentState) -> AgentState:
    prompt = CalculatorPrompt.format(query=state["query"])
    response = llm.invoke(prompt)
    state["answer"] = response.content.strip()
    return state