import os
import streamlit as st

from dotenv import load_dotenv
from groq import Groq
from modules.study_planner import generate_study_plan
from modules.text_summarizer import summarize_text
from modules.quiz_generator import generate_quiz
from modules.notes_generator import generate_notes


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Study Buddy")
st.caption("Your Personal AI Learning Assistant")

if not api_key:
    st.error("API key not found!")
    st.stop()

client = Groq(api_key=api_key)


# Sidebar
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Choose Feature",
    [
        "AI Chat",
        "Notes Generator",
        "Quiz Generator",
        "Text Summarizer",
        "Study Planner"
    ]
)


# AI Chat
if menu == "AI Chat":

    st.header("💬 AI Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask anything...")

    if user_input:

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                try:
                    response = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a friendly college study tutor. Explain in simple Hinglish."
                            },
                            *st.session_state.messages
                        ]
                    )

                    answer = response.choices[0].message.content

                    st.markdown(answer)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer
                    })

                except Exception as e:
                    st.error(str(e))


# Notes Generator
elif menu == "Notes Generator":

    st.header("📝 AI Notes Generator")

    topic = st.text_input(
        "Enter your study topic",
        placeholder="Example: Python File Handling"
    )

    if st.button("Generate Notes"):

        if topic.strip():

            with st.spinner("Generating your notes..."):

                try:
                    notes = generate_notes(client, topic)

                    st.success("Notes generated successfully!")

                    st.markdown(notes)

                    st.download_button(
                        "Download Notes",
                        data=notes,
                        file_name="study_notes.txt"
                    )

                except Exception as e:
                    st.error(str(e))

        else:
            st.warning("Please enter a topic.")


# Other Features
elif menu == "Quiz Generator":
   

    st.header("📝 AI Quiz Generator")

    topic = st.text_input(
        "Enter a topic",
        placeholder="Example: Python, Artificial Intelligence"
    )

    if st.button("Generate Quiz"):

        if topic:

            with st.spinner("AI is generating your quiz..."):

                quiz = generate_quiz(client, topic)

                st.subheader("Your AI Generated Quiz")

                st.markdown(quiz)

        else:
            st.warning("Please enter a topic first.")

elif menu == "Text Summarizer":

    st.header("📄 AI Text Summarizer")

    user_text = st.text_area(
        "Paste your text here",
        height=250,
        placeholder="Paste your notes or any long paragraph..."
    )

    if st.button("Summarize Text"):

        if user_text.strip():

            with st.spinner("AI is summarizing your text..."):

                summary = summarize_text(client, user_text)

                st.subheader("Your Summary")

                st.markdown(summary)

                st.download_button(
                    label="Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )

        else:
            st.warning("Please enter some text first.")

elif menu == "Study Planner":

    st.header("📅 AI Study Planner")

    subjects = st.text_input(
        "Enter your subjects",
        placeholder="Python, DBMS, Computer Graphics"
    )

    exam_date = st.date_input("Select your exam date")

    study_hours = st.slider(
        "Daily available study hours",
        min_value=1,
        max_value=12,
        value=4
    )

    if st.button("Generate Study Plan"):

        if subjects.strip():

            with st.spinner("AI is creating your study plan..."):

                plan = generate_study_plan(
                    client,
                    subjects,
                    exam_date,
                    study_hours
                )

                st.subheader("Your Study Plan")

                st.markdown(plan)

                st.download_button(
                    "Download Study Plan",
                    data=plan,
                    file_name="study_plan.txt",
                    mime="text/plain"
                )

        else:
            st.warning("Please enter your subjects.")