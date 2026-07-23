"""
Prompt Builder for MedRAG AI
"""


def build_prompt(question, retrieved_docs):
    """
    Build a prompt for Gemini using retrieved documents.
    """

    prompt = f"""
You are MedRAG AI, an AI assistant specialized in medical research.

Use ONLY the retrieved documents below to answer the user's question.

If multiple documents discuss the same topic, combine the information into one coherent answer.

If the documents contain only partial information, provide the best answer you can based on those documents.

Only say "I could not find sufficient evidence in the retrieved papers."
if none of the retrieved documents contain relevant information.

Question:
{question}

Retrieved Documents:

"""

    for doc in retrieved_docs:
        prompt += (
            f"Source: {doc['filename']}\n"
            f"{doc['text']}\n\n"
        )

    prompt += """
Answer in clear academic English.

Answer:
"""

    return prompt