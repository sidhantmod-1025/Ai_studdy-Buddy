def generate_study_plan(client, subjects, exam_date, study_hours):

    prompt = f"""
    You are an expert AI study planner.

    Create a study timetable using these details:

    Subjects: {subjects}
    Exam Date: {exam_date}
    Daily Study Hours: {study_hours}

    Instructions:
    - Create a practical study timetable.
    - Divide subjects into daily study sessions.
    - Include short breaks.
    - Give revision time.
    - Include practice questions.
    - Use simple English.
    - Present the timetable in a clear format.
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