import streamlit as st
from ai.chatbot import get_general_advice

st.title("🤖 CropInsight AI Assistant")

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

st.write("Ask anything about crops, diseases, fertilizers, or farming practices.")

user_input = st.text_input("Your question")

if st.button("Ask AI"):

    if user_input.strip() == "":
        st.error("Please type a question")
    else:
        response = get_general_advice(user_input)
        st.success(response)
