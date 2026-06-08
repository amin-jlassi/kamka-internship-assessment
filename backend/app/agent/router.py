from app.agent.state import AgentState
from app.config import get_settings
from app.agent.llm import get_llm



"""

Router Node : this node is responsible for deciding which tool to use based on the user's query.
It uses a prompt that describes the available tools and their use cases, and instructs the modelto select the most appropriate tool for the given query. 
The selected tool is then stored in the state under the "tool" key.


"""


settings = get_settings()
llm = get_llm()

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
    print("selected tool is : " , tool)
    if "retrieval" in tool : #local model mistral hillucinates the answer and is not responding with one word in retrieval case
        state['tool'] = "retrieval"
        
    elif tool not in ['retrieval', 'summarize', 'calculator']:
        raise ValueError(f"Invalid tool selected: {tool}")
    else :
        state["tool"] = tool
    return state