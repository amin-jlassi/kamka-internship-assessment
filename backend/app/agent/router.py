from langchain_google_genai import ChatGoogleGenerativeAI #type: ignore
from app.agent.state import AgentState
from app.config import get_settings



"""

Router Node : this node is responsible for deciding which tool to use based on the user's query.
It uses a prompt that describes the available tools and their use cases, and instructs the modelto select the most appropriate tool for the given query. 
The selected tool is then stored in the state under the "tool" key.


"""


settings = get_settings()
llm = ChatGoogleGenerativeAI(model=settings.model_name, temperature=0 , api_key=settings.google_api_key)

RouterPrompt = """
You are a routing assistant. Given a user query, decide which tool to use.

Tools available:
- retrieval: for questions about document content
- summarize: for summarization requests  
- calculator: for math or numerical questions

Reply with ONLY one word: retrieval, summarize, or calculator.

Query: {query} 

"""

def router_node(state: AgentState) -> AgentState:
    prompt = RouterPrompt.format(query=state["query"])
    response = llm.invoke(prompt)
    tool = response.content.strip().lower()
    
    if tool not in ['retrieval', 'summarize', 'calculator']:
        raise ValueError(f"Invalid tool selected: {tool}")
    state["tool"] = tool
    return state