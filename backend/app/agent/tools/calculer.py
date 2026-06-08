from app.config import get_settings
from langchain_google_genai import ChatGoogleGenerativeAI #type: ignore
from app.agent.state import AgentState

settings = get_settings()
llm = ChatGoogleGenerativeAI(model=settings.model_name, temperature=0 , api_key=settings.google_api_key)


CalculatorPrompt = """
You are a calculator assistant. Given a user query, perform the necessary calculations and provide the answer
Query: {query}
"""


def calculator_node(state: AgentState) -> AgentState:
    prompt = CalculatorPrompt.format(query=state["query"])
    response = llm.invoke(prompt)
    state["answer"] = response.content.strip()
    return state