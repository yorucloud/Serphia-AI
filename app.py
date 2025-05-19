import os
import json
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from rapidfuzz import process, fuzz
import streamlit as st

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Constants
API_URL = "http://localhost:3000/api/chat/completions"
MODEL_NAME = "deepseek-r1:latest"
MAX_HISTORY = 20
DATA_FILE = "kolorist_chatbot_dataset.xlsx"

LANGUAGES = {
    "English": "strings_en.json",
    "中文": "strings_zh.json"
}

# Load strings for selected language
def load_strings(lang="English"):
    try:
        with open(LANGUAGES[lang], "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "app_name": "Kolorist Chatbot",
            "greeting": "Ask anything...",
            "thinking": "Thinking...",
            "error": "⚠️ Error",
            "default_reply": "🤔 Sorry, I didn’t understand that.",
            "save_success": "✅ Chat history saved!"
        }

# Set default language
if "lang" not in st.session_state:
    st.session_state.lang = "English"
strings = load_strings(st.session_state.lang)

# Load FAQ pairs
faq_pairs = []
if os.path.exists(DATA_FILE):
    df = pd.read_excel(DATA_FILE)
    for _, row in df.iterrows():
        q = str(row.get("User Input Example", "")).strip()
        a = str(row.get("Bot Response", "")).strip()
        if q and a:
            faq_pairs.append((q.lower(), a))

questions = [q for q, _ in faq_pairs]
answers = [a for _, a in faq_pairs]

# Generate system prompt context
def generate_context(pairs, limit=20):
    context = (
        "You are Kolorist's virtual assistant. Only provide direct, helpful answers. "
        "Avoid greetings, opinions, filler words, or explanations. Focus on clarity and brevity.\n\n"
    )
    for q, a in pairs[:limit]:
        context += f"- Q: {q}\n  A: {a}\n"
    return context

kolorist_context = generate_context(faq_pairs)

# Streamlit UI Header
col1, col2 = st.columns(2)
with col1:
    st.title("💬 " + strings["app_name"])
with col2:
    if st.button("🌐 中文" if st.session_state.lang == "English" else "🌐 English"):
        st.session_state.lang = "中文" if st.session_state.lang == "English" else "English"
        st.rerun()

# Sidebar controls
with st.sidebar:
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    if st.button("💾 Save Chat"):
        with open("chat_history.json", "w", encoding="utf-8") as f:
            json.dump(st.session_state.get("messages", []), f, indent=2, ensure_ascii=False)
        st.success(strings["save_success"])

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f"{msg['content']} <sub>{msg.get('timestamp', '')}</sub>", unsafe_allow_html=True)

# Matching user input to known FAQ
def find_match(query, threshold=80):
    result = process.extractOne(query.lower(), questions, scorer=fuzz.partial_ratio)
    if result and result[1] >= threshold:
        return answers[result[2]]
    return None

# Remove filler phrases from LLM responses
def trim_filler(response):
    fillers = [
        "Sure, ", "Of course, ", "Let me help you with that. ", "Here's what I found: ",
        "As an AI assistant, ", "Please note that ", "Hope this helps. ", "Let me explain. "
    ]
    for f in fillers:
        if response.startswith(f):
            response = response[len(f):]
    return response.strip()

# User input and response logic
user_input = st.chat_input(strings["greeting"])
if user_input:
    now = datetime.now().strftime("%H:%M")
    st.session_state.messages.append({"role": "user", "content": user_input, "timestamp": now})
    with st.chat_message("user"):
        st.markdown(f"{user_input} <sub>{now}</sub>", unsafe_allow_html=True)

    reply = find_match(user_input)

    if reply:
        st.session_state.messages.append({"role": "assistant", "content": reply, "timestamp": now})
        with st.chat_message("assistant"):
            st.markdown(f"{reply} <sub>{now}</sub>", unsafe_allow_html=True)
    else:
        with st.spinner(strings["thinking"]):
            context_message = {
                "role": "system",
                "content": kolorist_context + (
                    "\nRespond briefly, with only essential information. Do not include greetings, explanations, or filler. "
                    "Avoid phrases like 'sure,' 'here you go,' 'let me help you,' or 'as an AI.'"
                )
            }
            history = [context_message] + [
                {"role": msg["role"], "content": msg["content"]}
                for msg in st.session_state.messages
            ][-MAX_HISTORY:]

            payload = {"model": MODEL_NAME, "messages": history}
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }

            try:
                res = requests.post(API_URL, json=payload, headers=headers)
                res.raise_for_status()
                data = res.json()
                raw_reply = data.get("choices", [{}])[0].get("message", {}).get("content", strings["default_reply"])
                reply = trim_filler(raw_reply)
            except Exception as e:
                reply = f"{strings['error']}: {e}"

        st.session_state.messages.append({"role": "assistant", "content": reply, "timestamp": now})
        with st.chat_message("assistant"):
            st.markdown(f"{reply} <sub>{now}</sub>", unsafe_allow_html=True)

# Style overrides
st.markdown("""
    <style>
        .main, .block-container {
            background-color: white;
            color: black;
        }
        .stChatMessage {
            background-color: #f8f9fa !important;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
        sub {
            color: #999;
            font-size: 0.75em;
            margin-left: 10px;
        }
    </style>
""", unsafe_allow_html=True)