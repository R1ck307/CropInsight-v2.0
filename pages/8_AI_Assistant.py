import streamlit as st

from ai.chatbot import answer_question
from utils.theme import apply_theme, page_header


apply_theme()


page_header(
    "CropInsight AI Assistant",
    "Your digital agricultural advisor"
)


# ---------------- SESSION MEMORY ----------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---------------- CLEAR CHAT ----------------

col1, col2 = st.columns([4,1])

with col2:

    if st.button("🗑 Clear"):

        st.session_state.chat_history = []

        st.rerun()



# ---------------- QUICK QUESTIONS ----------------

st.subheader("💡 Suggested Questions")


questions = [
    "What diseases affect maize?",
    "What fertilizer should I use?",
    "How can I prevent crop diseases?",
    "What treatments are available?"
]


cols = st.columns(2)


for index, question in enumerate(questions):

    with cols[index % 2]:

        if st.button(question):

            response = answer_question(question)

            st.session_state.chat_history.append(
                ("You", question)
            )

            st.session_state.chat_history.append(
                ("AI", response)
            )



st.divider()


# ---------------- USER INPUT ----------------

user_input = st.chat_input(
    "Ask CropInsight anything..."
)


if user_input:

    response = answer_question(
        user_input
    )


    st.session_state.chat_history.append(
        ("You", user_input)
    )


    st.session_state.chat_history.append(
        ("AI", response)
    )



# ---------------- DISPLAY CHAT ----------------


for role, message in st.session_state.chat_history:


    if role == "You":

        with st.chat_message("user"):

            st.write(message)


    else:

        with st.chat_message("assistant"):

            st.write(message)
