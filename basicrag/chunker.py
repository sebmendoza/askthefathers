from chonkie import SentenceChunker, LateChunker
from llamaparser import getOnTheIncarnation


def getLateChunker():
    return LateChunker(
        # mode="sentence",
        # chunk_size=512,
        # min_sentences_per_chunk=1,
        # min_characters_per_sentence=12,
    )


def getSentenceChunker():
    return SentenceChunker(
        chunk_size=400,
        chunk_overlap=0,
        # Minimum sentences in each chunk
        min_sentences_per_chunk=1,
        return_type="texts"                              # Return Chunks or texts only
    )


def resultOfLateChunker(book_text):
    chunker = getLateChunker()
    batch_chunks = chunker(book_text)
    return batch_chunks


def resultOfSentenceChunker(book_text):
    chunker = getSentenceChunker()
    chunks = chunker(book_text)
    return chunks


def getAllText(docs):
    all_text = ""
    for doc in docs:
        text = doc.text
        text = " ".join(text.split())
        all_text += text
    return all_text


def prepareChunks():
    docs = getOnTheIncarnation()
    docs = docs[3:64]
    book = getAllText(docs)
    return resultOfSentenceChunker(book)


if __name__ == "__main__":
    docs = getOnTheIncarnation()
    docs = docs[3:]
    book = getAllText(docs)
    print("\n\n\n", "-"*80, "Late Chunker")
    resultOfLateChunker(book)
    print("\n\n\n", "-"*80, "Default Chunker")
    resultOfSentenceChunker(book)
