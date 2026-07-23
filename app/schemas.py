from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str


class SourceDocument(BaseModel):
    filename: str
    chunk_id: int
    distance: float
    text: str


class AnswerResponse(BaseModel):
    question: str
    answer: str
    sources: list[SourceDocument]