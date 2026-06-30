import streamlit as st

st.set_page_config(page_title="Arhaanio", page_icon="🤖")

st.title("🤖 Arhaanio")
st.caption("Developed by Arhaan")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages=[]

with st.sidebar:
    st.header("Files")
    uploaded = st.file_uploader("Upload files", accept_multiple_files=True)
    if uploaded:
        for f in uploaded:
            st.write("📄", f.name)
    if st.button("Clear Chat"):
        st.session_state.messages=[]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

prompt = st.chat_input("Ask anything...")

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        ph = st.empty()
        reply=""
        try:
            stream = client.chat.completions.create(
                model="gpt-5",
                messages=st.session_state.messages,
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    reply += delta
                    ph.markdown(reply+"▌")
            ph.markdown(reply)
        except Exception as e:
            reply=f"Error: {e}"
            ph.markdown(reply)
    st.session_state.messages.append({"role":"assistant","content":reply})

st.divider()
st.markdown("<div style='text-align:center;color:gray'>Developed by Arhaan</div>", unsafe_allow_html=True)
