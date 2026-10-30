from groq import Groq


def generate_notes(client, topic):

    prompt = f"""
    You are an expert study notes generator.

    Create detailed study notes on: {topic}

    Follow this structure:

    1. Introduction
    2. Definition
    3. Important Concepts
    4. Real World Examples
    5. Advantages
    6. Conclusion

    Instructions:
    - Use simple English.
    - Explain concepts clearly.
    - Use bullet points.
    - Give practical examples.
    - Make notes suitable for college students.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_completion_tokens=1500
    )

    return response.choices[0].message.content