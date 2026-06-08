import sys
sys.path.append(".")
from app.agent.graph import agent
from app.agent.state import AgentState


def test_agent_graph():
    state = AgentState(
        query="c'est quoi une arbre ?" ,
        tool="",
        context=[] , 
        answer="" , 
        filename= None ,     
    )

    result = agent.invoke(state)
    
    return result

if __name__ == "__main__":
    result = test_agent_graph()
    print(f"chunks_length: {len(result['context'])}" , f"answer: {result['answer']}")