from app.agent.state import AgentState
from app.config import get_settings
from app.agent.llm import get_llm


"""
Answer Node : this node is responsible for generating the answer to the user's question using the context retrieved from the database (retrieval node) 
If the answer is already present in the state, it simply returns the state without invoking the model again.


"""



settings = get_settings()
llm = get_llm()

ANSWER_PROMPT = """
You are a document assistant. Answer the user's question using ONLY the context provided.
If the answer is not in the context, say "I couldn't find this information in the uploaded documents."
Always cite your sources by mentioning the filename and page number.

Context:
{context}

Question: {query}
"""

def answer_node(state: AgentState) -> AgentState:
    if state["answer"]:
        return state
    context_text = ""
    for chunk in state["context"]:
        context_text += f"[{chunk['metadata']['filename']} - page {chunk['metadata']['page_number']}]\n"
        context_text += chunk["text"] + "\n"

    
    prompt = ANSWER_PROMPT.format(
        context=context_text,
        query=state["query"]
    )
    response = llm.invoke(prompt)
    state["answer"] = response.content.strip()

    return state