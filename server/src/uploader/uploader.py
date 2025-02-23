from datetime import datetime
from utils import chromautils
from chunker import Chunker

collection_name = "on_the_incarnation"

if __name__ == "__main__":
    db_path = chromautils. getDBPath()
    chroma_client = chromautils.getChromaClient(db_path)
    chroma_client.delete_collection(collection_name)
    collection = chroma_client.get_or_create_collection(name=collection_name, metadata={
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
    print(f"Finished Upserting to {collection_name}")
