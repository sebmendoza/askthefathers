import chromadb
from chromadb import QueryResult
import time
import json
from chromadb.config import Settings


# chroma_client = chromadb.HttpClient(host='localhost', port=8000)
chroma_client = chromadb.PersistentClient(
    settings=Settings(anonymized_telemetry=False))
collection = chroma_client.get_or_create_collection(name="on_the_incarnation")

results: QueryResult = collection.query(
    query_texts=["kingdom of heaven"],  # Chroma will embed this for you
    n_results=3
)
# results = json.dumps(results, indent=2)
with open("./results/retrieval.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
