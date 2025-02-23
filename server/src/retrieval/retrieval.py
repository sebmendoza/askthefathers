from chromadb import QueryResult
from utils import chromautils
import json


# chroma_client = chromadb.HttpClient(host='localhost', port=8000)
# results = json.dumps(results, indent=2)
# with open("./results/retrieval.json", "w", encoding="utf-8") as f:
#     json.dump(results, f, ensure_ascii=False, indent=2)


def retrieve_from_chroma(query):
    db_path = chromautils.getDBPath()
    chroma_client = chromautils.getChromaClient(db_path)
    collection = chroma_client.get_or_create_collection(
        name="on_the_incarnation")
    results: QueryResult = collection.query(
        query_texts=query,
        n_results=10
    )
    # print(results)
    # return [str(collection.count())]
    # with open("./retrieval.json", "w", encoding="utf-8") as f:
    #     json.dump(results, f, ensure_ascii=False, indent=2)
    return results["documents"][0]


def test_retrieval():
    db_path = chromautils.getDBPath()
    chroma_client = chromautils.getChromaClient(db_path)

    collection = chroma_client.get_or_create_collection(
        name="on_the_incarnation")
    collection.count()
    results: QueryResult = collection.query(
        query_texts="kingdom",
        n_results=3
    )
    print(results)


if "__name__" == "__name__":
    test_retrieval()
