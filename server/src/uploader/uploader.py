import chromadb
from chromadb.config import Settings
from datetime import datetime
from chunker import Chunker


if __name__ == "__main__":
    chroma_client = chromadb.PersistentClient(
        settings=Settings(anonymized_telemetry=False))
    # chroma_client.delete_collection("on_the_incarnation")
    collection = chroma_client.get_or_create_collection(name="on_the_incarnation", metadata={
        "description": "Collection on On The Incarnation",
        "created": str(datetime.now())}
    )

    # Prepare Data
    c = Chunker()
    chunks = c.prepareChunks()
    ids = [f"chunk_{i}" for i, _ in enumerate(chunks)]

    collection.upsert(
        documents=chunks,
        ids=ids
    )
