import streamlit as st
import google.generativeai as genai

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(page_title="Arhaanio Pro", page_icon="🤖", layout="wide")

st.title("🤖 Arhaanio Pro")
st.caption("A ChatGPT-like AI Assistant by Arhaan 🚀")

# ----------------------------
# API SETUP
# ----------------------------
genai.configure(api_key=st.secrets["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# ----------------------------
# SESSION MEMORY
# ----------------------------
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# SIDEBAR (Controls)
# ----------------------------
with st.sidebar:
    st.header("⚙️ Controls")
    
    if st.button("🗑 Clear Chat"):
        st.session_state.chat = model.start_chat(history=[])
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.write("**Arhaanio Pro v1.0**")
    st.write("Developed By Arhaan 🚀")

# ----------------------------
# DISPLAY CHAT
# ----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ----------------------------
# USER INPUT
# ----------------------------
user_input = st.chat_input("Ask anything...")

if user_input:
    # user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI response
    response = st.session_state.chat.send_message(user_input)

    ai_text = response.text

    st.session_state.messages.append({"role": "assistant", "content": ai_text})

    with st.chat_message("assistant"):
        st.markdown(ai_text)
