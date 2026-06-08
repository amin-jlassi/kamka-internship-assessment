import sys
import time
sys.path.append(".")
from app.ingestion.pipeline import Pipeline

pipeline = Pipeline()

t = time.time()
query_embedding = pipeline.embedder.embed_text("what is 150 * 150?")
print(f"embedding query: {time.time() - t:.2f}s")

t = time.time()
chunks = pipeline.vectorStore.retrieve_related_chunks(query_embedding)
print(f"chromadb retrieval: {time.time() - t:.2f}s")