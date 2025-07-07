# streamlit_app.py

import streamlit as st
import requests
import os

# Load backend URL from environment variables
BACKEND_URL = os.getenv("BACKEND_URL")

st.set_page_config(page_title="AI Calendar Agent")
st.title("AI Calendar Booking Assistant")

# Persistent memory per user session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Ask to check or book a time slot...")

# Run agent via backend API
def get_agent_response(query):
    try:
        response = requests.post(
            f"{BACKEND_URL}/chat",
            json={"query": query},
            timeout=10
        )
        return response.json().get("response", "❌ Error: Invalid response from backend.")
    except Exception as e:
        return f"❌ Error: {e}"

# Handle chat interaction
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.spinner("Thinking..."):
        ai_response = get_agent_response(user_input)
    st.session_state.chat_history.append(("ai", ai_response))

# Render chat history
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)
