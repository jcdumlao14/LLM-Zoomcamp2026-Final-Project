from rag.retriever import search
from rag.prompt import build_prompt
from rag.llm import generate


def ask(question: str):

    docs = search(question, k=5)

    prompt = build_prompt(question, docs)

    answer = generate(prompt)

    return {
        "answer": answer,
        "sources": docs
    }