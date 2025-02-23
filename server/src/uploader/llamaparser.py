import pickle
import os
from llama_index.core import SimpleDirectoryReader, Document
from llama_cloud_services import LlamaParse
from dotenv import load_dotenv
load_dotenv()


def getOnTheIncarnation() -> list[Document]:
    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define absolute paths for cache and documents
    cache_dir = os.path.join(current_dir, "data", "cache")
    pdfs_dir = os.path.join(current_dir, "data", "pdfs")
    cache_file = os.path.join(cache_dir, "cached_documents.pkl")
    pdf_file = os.path.join(pdfs_dir, "on_the_incarnation_athenasius.pdf")

    # Create directories if they don't exist
    os.makedirs(cache_dir, exist_ok=True)
    os.makedirs(pdfs_dir, exist_ok=True)

    # set up parser
    parser = LlamaParse(
        result_type="text"
    )

    # Check if cached documents exist
    if os.path.exists(cache_file):
        print("Opening old file")
        with open(cache_file, 'rb') as f:
            documents = pickle.load(f)
    else:
        print("Parsing document again")
        # use SimpleDirectoryReader to parse our file
        file_extractor = {".pdf": parser}
        documents = SimpleDirectoryReader(
            input_files=[pdf_file],
            file_extractor=file_extractor
        ).load_data()

        # Save documents to cache
        with open(cache_file, 'wb') as f:
            pickle.dump(documents, f)

    return documents
