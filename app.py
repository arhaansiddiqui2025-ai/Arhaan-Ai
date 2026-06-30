from openai import OpenAI
import time
import streamlit as st
import os
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Arhaanio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.chat-user{
background:#2b313e;
padding:15px;
border-radius:15px;
margin-bottom:10px;
}

.chat-ai{
background:#444654;
padding:15px;
border-radius:15px;
margin-bottom:10px;
}

.block-container{
padding-top:1rem;
}

.title{
font-size:42px;
font-weight:bold;
text-align:center;
margin-bottom:5px;
}

.subtitle{
text-align:center;
color:gray;
margin-bottom:20px;
}

.footer{
text-align:center;
color:gray;
padding:20px;
font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown("<div class='title'>🤖 Arhaanio</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your Personal AI Assistant</div>", unsafe_allow_html=True)

# =========================
# SESSION
# =========================
if "messages" not in st.session_state:
    st.session_state.messages=[]

if "mode" not in st.session_state:
    st.session_state.mode="Chat"
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)
# =========================
# SIDEBAR
# =========================
with st.sidebar:

    st.title("⚙️ Arhaanio")

    st.markdown("---")

    mode=st.radio(
        "Choose Feature",
        [
            "💬 Chat",
            "📂 File Upload"
        ]
    )

    st.markdown("---")

    uploaded_files=st.file_uploader(
        "Upload Files",
        type=[
            "pdf",
            "txt",
            "docx",
            "csv",
            "png",
            "jpg",
            "jpeg"
        ],
        accept_multiple_files=True
    )

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages=[]

# =========================
# CHAT DISPLAY
# =========================
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# CHAT INPUT
# =========================
prompt=st.chat_input("Ask anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        placeholder=st.empty()

        placeholder.markdown("⏳ Thinking...")

        # AI response will be added in Part 2    
    try:
    response_text = ""

    stream = client.chat.completions.create(
        model="gpt-5",
        messages=st.session_state.messages,
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content
            placeholder.markdown(response_text + "▌")

    placeholder.markdown(response_text)
    response = response_text

except Exception as e:
    response = f"❌ Error: {e}"
    placeholder.markdown(response)

        

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )

# =========================
# FOOTER
# =========================
st.markdown("---")

st.markdown(
"""
<div class='footer'>
Developed by Arhaan
</div>
""",
unsafe_allow_html=True
)
