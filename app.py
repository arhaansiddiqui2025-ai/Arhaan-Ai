import streamlit as st

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Arhaanio", page_icon="🤖")

st.title("🤖 Arhaanio")
st.write("Your AI Chatbot Assistant")

# ----------------------------
# Session State (Chat Memory)
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ----------------------------
# User Input
# ----------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # ----------------------------
    # BOT RESPONSE (Placeholder)
    # ----------------------------
    def get_bot_response(prompt: str):
        return f"Arhaanio: I received -> {prompt} 🤖"

    response = get_bot_response(user_input)

    # Store bot message
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.markdown("**Developed By Arhaan** 🚀")
