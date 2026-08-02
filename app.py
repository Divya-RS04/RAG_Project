import streamlit as st
from rag_engine import answer_question

# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------

st.markdown("""
<style>

.main{
    padding-top:2rem;
}

.stChatMessage{
    border-radius:15px;
    padding:15px;
}

div[data-testid="stSidebar"]{
    background-color:#0E1117;
}

div[data-testid="stSidebar"] *{
    color:white;
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------

with st.sidebar:

    st.title("🤖 AI Knowledge Assistant")

    st.markdown("---")

    st.markdown("### ⚙️ Model")
    st.success("Google FLAN-T5")

    st.markdown("### 🧠 Embeddings")
    st.success("all-MiniLM-L6-v2")

    st.markdown("### 📚 Vector Database")
    st.success("FAISS")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages=[]

    st.markdown("---")

    st.write("👨‍💻 Developed by")
    st.write("**Divya R S**")

# -------------------- TITLE --------------------

st.title("🤖 AI Knowledge Assistant")

st.caption("Ask anything from your knowledge base")

# -------------------- CHAT HISTORY --------------------

if "messages" not in st.session_state:
    st.session_state.messages=[]

# Display old messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# -------------------- USER INPUT --------------------

prompt=st.chat_input("Type your question...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Searching knowledge base..."):

        answer,context=answer_question(prompt)

    with st.chat_message("assistant"):

        st.markdown(answer)

        with st.expander("📄 Retrieved Context"):

            st.write(context)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

