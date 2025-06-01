import streamlit as st
import requests

# Constants
API_URL = "http://localhost:3000/api/chat/completions"
API_KEY = "sk-61bcbb639f4d4f3fbee03cfd6b490d85"
MODEL_NAME = "deepseek-r1:latest"

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 AI Chat Interface")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")
if user_input:
    # Add user message to session
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare request payload
    payload = {
        "model": MODEL_NAME,
        "messages": st.session_state.messages,
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Send request to API
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Extract response
        reply = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        st.session_state.messages.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        error_msg = f"Error: {e}"
        st.session_state.messages.append({"role": "assistant", "content": error_msg})
        with st.chat_message("assistant"):
            st.error(error_msg)