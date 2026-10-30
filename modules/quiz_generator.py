def generate_quiz(client, topic):

    prompt = f"""
    Create a quiz on the topic: {topic}

    Generate 5 multiple-choice questions.

    Each question must have:
    - 4 options (A, B, C, D)
    - One correct answer
    - A short explanation of the correct answer.

    Use simple English suitable for college students.

    Follow this format:

    Q1. Question?
    A. Option 1
    B. Option 2
    C. Option 3
    D. Option 4

    Correct Answer: B
    Explanation: Explain why B is correct.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_completion_tokens=1500
    )

    return response.choices[0].message.content