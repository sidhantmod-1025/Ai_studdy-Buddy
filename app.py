import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from modules.study_planner import generate_study_plan
from modules.text_summarizer import summarize_text
from modules.quiz_generator import generate_quiz
from modules.notes_generator import generate_notes


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------- API CONFIGURATION ----------------

load_dotenv()

try:
    api_key = st.secrets.get("GROQ_API_KEY", "")
except Exception:
    # Local computer: read the key from .env
    api_key = os.getenv("GROQ_API_KEY", "")


# ---------------- NAVIGATION ----------------

MENU_OPTIONS = [
    "Dashboard",
    "AI Chat",
    "Notes Generator",
    "Quiz Generator",
    "Text Summarizer",
    "Study Planner",
]


def go_to(page_name):
    """Called before Streamlit reruns, so the radio can safely update."""
    st.session_state.selected_menu = page_name


if "selected_menu" not in st.session_state:
    st.session_state.selected_menu = "Dashboard"


# ---------------- CUSTOM CSS ----------------

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b1120, #111827);
        color: #f8fafc;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    section[data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #263449;
    }

    section[data-testid="stSidebar"] h1 {
        color: #a78bfa;
    }

    h1, h2, h3 {
        color: #f8fafc !important;
    }

    .hero {
        background: linear-gradient(120deg, #312e81, #581c87, #1e3a8a);
        padding: 38px;
        border-radius: 20px;
        margin-bottom: 28px;
        border: 1px solid #6366f1;
    }

    .hero h1 {
        font-size: 36px;
        color: white !important;
        margin-bottom: 10px;
    }

    .hero p {
        color: #e0e7ff;
        font-size: 17px;
        margin-bottom: 0;
    }

    .feature-card {
        background: #172033;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #334155;
        min-height: 145px;
        margin-bottom: 10px;
    }

    .feature-card h3 {
        color: #c4b5fd !important;
        font-size: 19px;
    }

    .feature-card p {
        color: #cbd5e1;
        font-size: 14px;
    }

    .stButton > button {
        background: linear-gradient(90deg, #7c3aed, #4f46e5);
        color: white;
        border: 0;
        border-radius: 10px;
        min-height: 42px;
        font-weight: 600;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #6d28d9, #4338ca);
        color: white;
        border: 0;
        transform: translateY(-2px);
    }

    .stTextInput input, .stTextArea textarea {
        background: #172033;
        color: white;
        border: 1px solid #475569;
        border-radius: 10px;
    }

    div[data-baseweb="select"] > div {
        background: #172033;
    }

    hr {
        border-color: #334155;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown("# 📚 AI Study Buddy")
    st.caption("YOUR PERSONAL AI LEARNING ASSISTANT")
    st.divider()

    menu = st.radio(
        "NAVIGATION",
        MENU_OPTIONS,
        key="selected_menu",
    )

    st.divider()
    st.markdown("### 🎯 Your Learning Partner")
    st.caption(
        "Learn smarter, save time, and improve your productivity with AI."
    )
    st.divider()
    st.caption("Made with ❤️ using Python & Groq AI")
    st.caption("Version 2.1")


# ---------------- DASHBOARD ----------------

if menu == "Dashboard":
    st.markdown(
        """
        <div class="hero">
            <h1>Welcome to AI Study Buddy 👋</h1>
            <p>
                Your personal AI-powered learning assistant.
                Generate notes, practice quizzes, summarize text,
                chat with AI, and plan your studies.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("🚀 Your Learning Workspace")
    st.write("Choose a tool to get started.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <h3>💬 AI Chat</h3>
                <p>Ask questions and get easy-to-understand explanations.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button(
            "Open AI Chat",
            key="open_chat",
            use_container_width=True,
            on_click=go_to,
            args=("AI Chat",),
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <h3>📝 Notes Generator</h3>
                <p>Create structured study notes on any subject or topic.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button(
            "Open Notes Generator",
            key="open_notes",
            use_container_width=True,
            on_click=go_to,
            args=("Notes Generator",),
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <h3>🧠 Quiz Generator</h3>
                <p>Test your understanding with AI-generated quizzes.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button(
            "Open Quiz Generator",
            key="open_quiz",
            use_container_width=True,
            on_click=go_to,
            args=("Quiz Generator",),
        )

    col4, col5 = st.columns(2)

    with col4:
        st.markdown(
            """
            <div class="feature-card">
                <h3>📄 Text Summarizer</h3>
                <p>Turn lengthy notes and paragraphs into concise summaries.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button(
            "Open Text Summarizer",
            key="open_summarizer",
            use_container_width=True,
            on_click=go_to,
            args=("Text Summarizer",),
        )

    with col5:
        st.markdown(
            """
            <div class="feature-card">
                <h3>📅 Study Planner</h3>
                <p>Build a personalized study plan for your exam preparation.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button(
            "Open Study Planner",
            key="open_planner",
            use_container_width=True,
            on_click=go_to,
            args=("Study Planner",),
        )

    st.divider()
    st.subheader("✨ Learn smarter, not harder")

    benefit1, benefit2, benefit3 = st.columns(3)
    with benefit1:
        st.markdown("### ⚡ Save Time")
        st.write("Create useful learning material in less time.")
    with benefit2:
        st.markdown("### 🎯 Understand Better")
        st.write("Break down difficult topics into simpler explanations.")
    with benefit3:
        st.markdown("### 📚 Stay Organized")
        st.write("Prepare a study plan and keep your learning focused.")

    st.info("Tip: Use the buttons above or the sidebar to open any AI tool.")


# ---------------- API CLIENT CHECK ----------------
# Dashboard remains accessible even if the key is missing.
# The API key is required only when the user opens an AI feature.

else:
    if not api_key:
        st.error(
            "Groq API key not found. Add GROQ_API_KEY to Streamlit Cloud "
            "Settings → Secrets, or add it to your local .env file."
        )
        st.stop()

    try:
        client = Groq(api_key=api_key)
    except Exception as error:
        st.error(f"Could not initialize Groq: {error}")
        st.stop()


    # ---------------- AI CHAT ----------------

    if menu == "AI Chat":
        st.title("💬 AI Learning Assistant")
        st.caption("Ask questions. Learn with clear, simple explanations.")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        user_input = st.chat_input("Ask your study question...")

        if user_input:
            st.session_state.messages.append(
                {"role": "user", "content": user_input}
            )

            with st.chat_message("user"):
                st.markdown(user_input)

            with st.chat_message("assistant"):
                with st.spinner("AI is thinking..."):
                    try:
                        response = client.chat.completions.create(
                            model="openai/gpt-oss-120b",
                            messages=[
                                {
                                    "role": "system",
                                    "content": (
                                        "You are a friendly college study tutor. "
                                        "Explain concepts in simple Hinglish "
                                        "with examples."
                                    ),
                                },
                                *st.session_state.messages,
                            ],
                        )

                        answer = response.choices[0].message.content
                        st.markdown(answer)

                        st.session_state.messages.append(
                            {"role": "assistant", "content": answer}
                        )
                    except Exception as error:
                        st.error(f"AI Chat error: {error}")

        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()


    # ---------------- NOTES GENERATOR ----------------

    elif menu == "Notes Generator":
        st.title("📝 AI Notes Generator")
        st.caption("Create organized study notes using artificial intelligence.")

        topic = st.text_input(
            "Enter your study topic",
            placeholder="Example: Python File Handling",
        )

        if st.button("✨ Generate Notes"):
            if topic.strip():
                with st.spinner("Creating your notes..."):
                    try:
                        notes = generate_notes(client, topic)
                        st.success("Your notes are ready!")
                        st.markdown(notes)

                        st.download_button(
                            "⬇️ Download Notes",
                            data=notes,
                            file_name="study_notes.txt",
                            mime="text/plain",
                        )
                    except Exception as error:
                        st.error(f"Notes generation error: {error}")
            else:
                st.warning("Please enter a topic.")


    # ---------------- QUIZ GENERATOR ----------------

    elif menu == "Quiz Generator":
        st.title("🧠 AI Quiz Generator")
        st.caption("Practice your knowledge with AI-generated questions.")

        topic = st.text_input(
            "Enter your quiz topic",
            placeholder="Example: Python, DBMS, Artificial Intelligence",
        )

        if st.button("✨ Generate Quiz"):
            if topic.strip():
                with st.spinner("AI is preparing your quiz..."):
                    try:
                        quiz = generate_quiz(client, topic)
                        st.success("Your quiz is ready!")
                        st.markdown("### Your AI Generated Quiz")
                        st.markdown(quiz)
                    except Exception as error:
                        st.error(f"Quiz generation error: {error}")
            else:
                st.warning("Please enter a topic first.")


    # ---------------- TEXT SUMMARIZER ----------------

    elif menu == "Text Summarizer":
        st.title("📄 AI Text Summarizer")
        st.caption("Turn lengthy text into simple, meaningful summaries.")

        user_text = st.text_area(
            "Paste your text below",
            height=250,
            placeholder="Paste your notes or any long paragraph...",
        )

        if st.button("✨ Summarize Text"):
            if user_text.strip():
                with st.spinner("AI is summarizing your text..."):
                    try:
                        summary = summarize_text(client, user_text)
                        st.success("Summary generated successfully!")
                        st.markdown("### Your Summary")
                        st.markdown(summary)

                        st.download_button(
                            "⬇️ Download Summary",
                            data=summary,
                            file_name="summary.txt",
                            mime="text/plain",
                        )
                    except Exception as error:
                        st.error(f"Summarization error: {error}")
            else:
                st.warning("Please paste some text first.")


    # ---------------- STUDY PLANNER ----------------

    elif menu == "Study Planner":
        st.title("📅 AI Study Planner")
        st.caption("Create a personalized timetable for your exams.")

        subjects = st.text_input(
            "Enter your subjects",
            placeholder="Python, DBMS, Computer Graphics",
        )

        exam_date = st.date_input("Select your exam date")

        study_hours = st.slider(
            "Daily available study hours",
            min_value=1,
            max_value=12,
            value=4,
        )

        if st.button("✨ Generate Study Plan"):
            if subjects.strip():
                with st.spinner("AI is creating your study plan..."):
                    try:
                        plan = generate_study_plan(
                            client,
                            subjects,
                            exam_date,
                            study_hours,
                        )

                        st.success("Your study plan is ready!")
                        st.markdown("### 📚 Your Personalized Study Plan")
                        st.markdown(plan)

                        st.download_button(
                            "⬇️ Download Study Plan",
                            data=plan,
                            file_name="study_plan.txt",
                            mime="text/plain",
                        )
                    except Exception as error:
                        st.error(f"Study plan error: {error}")
            else:
                st.warning("Please enter your subjects.")
