import time
import sys
sys.path.append(".")
from app.agent.llm import get_llm

llm = get_llm()

t = time.time()
response = llm.invoke("what is 2 + 2?")
print(f"LLM response time: {time.time() - t:.2f}s")
print(response.content)