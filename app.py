import streamlit as st
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

st.set_page_config(
    page_title="Local AI Lab",
    page_icon="🤖",
    layout="centered"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.sidebar.title("⚙️ Local AI Settings")

model_name = st.sidebar.selectbox(
    "Select Model",
    ["qwen2.5:0.5b"]
)

st.sidebar.caption("Running locally through Ollama")

if st.sidebar.button("🗑️ Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

st.title("🤖 Local AI Lab")
st.caption("Chat with your locally running LLM using Ollama")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask your local AI anything...")

if prompt:
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("assistant"):
        with st.spinner("AI is thinking..."):
            try:
                response = requests.post(
                    OLLAMA_URL,
                    json={
                        "model": model_name,
                        "messages": st.session_state.messages,
                        "stream": False
                    },
                    timeout=300
                )

                response.raise_for_status()

                answer = response.json()["message"]["content"]

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except requests.exceptions.ConnectionError:
                answer = "Cannot connect to Ollama. Make sure Ollama is running."
                st.error(answer)

            except Exception as e:
                st.error(f"Error: {e}")