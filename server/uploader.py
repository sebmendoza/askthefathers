import chromadb
from chromadb import QueryResult, Collection
from chromadb.config import Settings
from datetime import datetime
from chunker import prepareChunks
from llamaparser import Document


def prepareData() -> tuple[list[str], list[str]]:
    chunks = prepareChunks()
    ids = [f"chunk_{i}" for i, _ in enumerate(chunks)]
    return chunks, ids


if __name__ == "__main__":
    chroma_client = chromadb.PersistentClient(
        settings=Settings(anonymized_telemetry=False))
    # chroma_client.delete_collection("on_the_incarnation")
    collection = chroma_client.get_or_create_collection(name="on_the_incarnation", metadata={
        "description": "Collection on On The Incarnation",
        "created": str(datetime.now())}
    )
    chunks, ids = prepareData()
    # print(chunks)
    # for i in range(40):
    #     print(chunks[i], "\n\n\n\n")
    collection.upsert(
        documents=chunks,
        ids=ids
    )
