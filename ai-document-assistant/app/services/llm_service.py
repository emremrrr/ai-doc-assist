import os
from openai import OpenAI

token=os.getenv("OPENAI_API_KEY")

if not token:
    raise Exception("GITHUB_TOKEN is not set")

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=token
)

model_name = "openai/gpt-4o-mini"

def generate_answer(question: str, context_chunks: list[dict]) -> str:
    context = "\n\n".join([
        chunk["text"] for chunk in context_chunks
    ])

    prompt = f"""
Answer the question using only the context below.

If the answer is not in the context, say:
"I could not find the answer in the uploaded documents."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful document assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content