import streamlit as st
from ai.chatbot import answer_question

st.title("🤖 CropInsight AI Assistant")

st.write("Ask anything about crops, diseases, fertilizers, or farming advice.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Your Question")

if st.button("Ask"):

    if user_input.strip():

        response = answer_question(user_input)

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("AI", response))

# ---------------- CHAT DISPLAY ----------------
for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"🧑‍🌾 **You:** {msg}")
    else:
        st.markdown(f"🤖 **AI:** {msg}")
