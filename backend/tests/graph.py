import sys
sys.path.append(".")
from app.agent.graph import agent
from app.agent.state import AgentState


def test_agent_graph():
    state = AgentState(
        query="150 * 150 ?" ,
        tool="",
        context=[] , 
        answer="" , 
        filename= "Chapitre7 les Arbres.pptx.pdf"  ,     
    )

    result = agent.invoke(state)
    
    return result

if __name__ == "__main__":
    result = test_agent_graph()
    print(f"chunks_length: {len(result['context'])}" , f"answer: {result['answer']}")
    for chunk in result["context"] :
        print(f"chunk text : {chunk['text'][:100]}..." , f"metadata : {chunk['metadata']} " , f"score : {chunk['score']}")