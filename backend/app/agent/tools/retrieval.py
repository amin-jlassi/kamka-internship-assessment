from app.ingestion.pipeline import Pipeline
from app.agent.state import AgentState

pipeline = Pipeline()
def retrieval_node(state: AgentState) -> AgentState:
    
    results = pipeline.query(state["query"])
    if not results:
        state["answer"] = "No relevant information found in the documents."
        return state
    state["context"] = results
    return state