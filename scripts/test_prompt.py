from rag.retriever import search
from rag.prompt import build_prompt


def main():
    question = input("Question: ")

    docs = search(question, k=3)

    prompt = build_prompt(question, docs)

    print("=" * 80)
    print(prompt)


if __name__ == "__main__":
    main()