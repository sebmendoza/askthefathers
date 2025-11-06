# askthefathers

Exploring Retrieval-Augmented Generation (RAG). This project uses a local embedding store of patristic texts and generates query responses from Gemini. Ambitions for this project include publicly releasing with MUCH more texts.

### Tools

- Next.js — quick (though bloated) frontend to prototype a UI
- FastAPI — minimal API layer that wires retrieval and LLM calls. Wanted to work with Python on this part
- ChromaDB (local persistent vector DB) — stores document embeddings and does retrieval for RAG
- Gemini — used as the backing LLM because it was free

### Next steps:

- Improve and unify document parsing from different sources (pdfs, .txt, etc)
- Add more source texts and expand the Chroma collection
- Build hosting/deployment for full stack
