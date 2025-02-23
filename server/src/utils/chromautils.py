import os
import chromadb
from chromadb import Settings


def getDBPath():
    # Get the absolute path relative to your FastAPI app
    src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    db_path = os.path.join(src_dir, "chroma")

    # Make sure the directory exists
    os.makedirs(db_path, exist_ok=True)
    return db_path


def getChromaClient(path):
    chroma_client = chromadb.PersistentClient(
        path=path,
        settings=Settings(
            anonymized_telemetry=False,
            is_persistent=True
        )
    )
    return chroma_client
