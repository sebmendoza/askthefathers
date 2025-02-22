# bring in our LLAMA_CLOUD_API_KEY
from dotenv import load_dotenv
load_dotenv()

# bring in deps
from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader, Document
import os
import pickle



def getOnTheIncarnation() -> list[Document]:
    # set up parser
    parser = LlamaParse(
        result_type="text"
    )

    # Define path for cached documents
    cache_file = "./cached_documents.pkl"

    # Check if cached documents exist
    if os.path.exists(cache_file):
        with open(cache_file, 'rb') as f:
            documents = pickle.load(f)
    else:
        # use SimpleDirectoryReader to parse our file
        file_extractor = {".pdf": parser}
        documents = SimpleDirectoryReader(input_files=['./pdfs/on_the_incarnation_athenasius.pdf'], file_extractor=file_extractor).load_data()
        
        # Save documents to cache
        with open(cache_file, 'wb') as f:
            pickle.dump(documents, f)

    return documents

if __name__ == "__main__":
    docs = getOnTheIncarnation()
    doc: Document = docs[10]
    print(doc.text)