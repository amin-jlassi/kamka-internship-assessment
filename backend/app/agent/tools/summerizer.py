from app.config import get_settings
from langchain_google_genai import ChatGoogleGenerativeAI #type: ignore
from app.vectoreStore.chroma import VectorStore
from app.agent.state import AgentState


"""
Summarizer Node : this node is responsible for generating a concise summary of a document based on the user's query.
It retrieves all the chunks of the document using the filename stored in the state, formats them into a readable context, 
and then uses a prompt to instruct the model to generate a summary that is relevant to the user's query.
The output of this node is the generated summary which is stored in the state under the "answer

"""


settings = get_settings()
vector_store = VectorStore()
llm = ChatGoogleGenerativeAI(model=settings.model_name, temperature=0 , api_key=settings.google_api_key)

SummarizerPrompt = """
You are a summarization assistant. Given a user query and relevant context, generate a concise summary
Context: {context}
Query: {query}
"""

def summarizer_node(state: AgentState) -> AgentState:
    filename = state["filename"]
    related_chunks = vector_store.get_document_chunks_by_filename(filename)
    context = ""
    for chunk in related_chunks : 
        context += chunk["text"] + "\n"
        
    prompt = SummarizerPrompt.format(context=context , query=state["query"])
    response = llm.invoke(prompt)
    state["answer"] = response.content.strip()
    return state
