# streamlit_app.py

import streamlit as st
from backend.agent import run_agent

st.set_page_config(page_title="AI Calendar Agent", page_icon="📅")
st.title("📅 AI Calendar Booking Assistant")

# Persistent memory per user session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Ask to check or book a time slot...")

# Run agent on user input
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.spinner("Thinking..."):
        response = run_agent(user_input)
    st.session_state.chat_history.append(("ai", response))

# Render chat history
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)
