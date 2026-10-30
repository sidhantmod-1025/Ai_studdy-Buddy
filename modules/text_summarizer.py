def summarize_text(client, text):

    prompt = f"""
    You are an expert text summarizer.

    Summarize the following text:

    {text}

    Instructions:
    - Use simple English.
    - Keep the summary short and clear.
    - Include all important points.
    - Use bullet points where necessary.
    - Make it easy for college students to understand.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_completion_tokens=1000
    )

    return response.choices[0].message.content