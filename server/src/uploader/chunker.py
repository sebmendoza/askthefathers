from chonkie import SentenceChunker
from llamaparser import getOnTheIncarnation


def getAllText(docs):
    all_text = ""
    for doc in docs:
        text = doc.text
        # text = " ".join(text.split())
        all_text += text
    return all_text


class Chunker:
    def __init__(self):
        docs = getOnTheIncarnation()
        self.docs = docs[3:64]
        self.full_text = getAllText(self.docs)

    def prepareChunks(self):
        chunker = SentenceChunker(
            chunk_size=400,
            chunk_overlap=0,
            # Minimum sentences in each chunk
            min_sentences_per_chunk=1,
            return_type="texts"                              # Return Chunks or texts only
        )
        chunks = chunker(self.full_text)
        return chunks


if __name__ == "__main__":
    c = Chunker()
    chunks = c.prepareChunks()
    # print(chunks[:10])
