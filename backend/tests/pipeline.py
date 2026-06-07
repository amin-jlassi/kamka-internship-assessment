import sys
sys.path.append(".")
from app.ingestion.pipeline import Pipeline



pipeline = Pipeline()
def test_ingest() :
    res = pipeline.ingest(file_path="uploads/liste_chaine.pdf")
    return res
    
def test_query() :
    query = " Implémenter de manière itérative les opérations suivantes"
    res = pipeline.query(query)
    return res

if __name__ == "__main__" :
    #ingest_res = test_ingest()
    #print("ingest res : " , ingest_res)
    query_res = test_query()
    print("query res : " , query_res)
