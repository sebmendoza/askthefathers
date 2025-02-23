from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from retrieval.retrieval import retrieve_from_chroma
from llm.prompt import RAGPromptGenerator, hit_gemini


app = FastAPI()


class Query(BaseModel):
    text: str


class QueryResponse(BaseModel):
    response: str


@app.get("/")
def status():
    return {
        "Status": "Alive"
    }


@app.post("/retrieve", response_model=QueryResponse)
def handle_retrieval(query: Query):
    try:
        q = query.text
        rag_results = retrieve_from_chroma(q)
        # print("Rag:", rag_results)
        prompt_generator = RAGPromptGenerator()
        prompt = prompt_generator.generate_prompt(query, rag_results)
        response = hit_gemini(prompt)
        return QueryResponse(
            response=response
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
