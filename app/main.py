from fastapi import FastAPI

from app.schemas import QuestionRequest, AnswerResponse
from app.service import ask

app = FastAPI(
    title="MedRAG AI",
    version="1.0.0",
    description="Medical Research RAG System"
)


@app.get("/")
def root():
    return {"message": "MedRAG AI API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):

    result = ask(request.question)

    sources = []

    for doc in result["sources"]:
        sources.append(
            {
                "filename": doc["filename"],
                "chunk_id": doc["chunk_id"],
                "distance": round(doc["distance"], 4),
                "text": doc["text"]
            }
        )

    return AnswerResponse(
        question=request.question,
        answer=result["answer"],
        sources=sources
    )
