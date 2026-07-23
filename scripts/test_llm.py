from rag.llm import generate_answer


def main():
    prompt = "Explain deep learning in one paragraph."

    answer = generate_answer(prompt)

    print(answer)


if __name__ == "__main__":
    main()