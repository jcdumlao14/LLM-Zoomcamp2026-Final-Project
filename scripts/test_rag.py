"""
End-to-End MedRAG AI Test
"""

from rag.retriever import search
from rag.prompt import build_prompt
from rag.llm import generate


def main():

    question = input("Question: ")

    print("\nSearching documents...\n")

    docs = search(question, k=5)

    prompt = build_prompt(question, docs)

    print("Generating answer...\n")

    answer = generate(prompt)

    print("=" * 60)
    print("PROMPT")
    print("=" * 60)
    print(prompt)

    print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)
    print(answer)


if __name__ == "__main__":
    main()