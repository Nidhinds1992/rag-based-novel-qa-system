import streamlit as st
import requests

st.set_page_config(page_title="RAG CHATBOT", page_icon="🤖")

st.title("📚 Sherlock Holmes RAG Chatbot")
st.write("Ask questions from the document")

question = st.text_input("Ask any  question:")

if st.button("Ask"):
    if question:
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": question}
        )

        if response.status_code == 200:
            result = response.json()
            st.subheader("Answer:")
            st.write(result["answer"])
        else:
            st.error("Error from FastAPI backend")
    else:
        st.warning("Please enter a question")