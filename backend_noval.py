from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "RAG API is running"}


from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
) 

from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3:8b")

from langchain_community.vectorstores import FAISS

vector_db = FAISS.load_local(
    "faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)

def ask_question(query):

    relevant_docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in relevant_docs]
    )

    prompt = f"""
    You are a helpful AI assistant.

    Answer the question using ONLY the context.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    response = llm.invoke(prompt)

    return response

@app.post("/ask")
def ask_question_api(request: QuestionRequest):
    question = request.question

    answer = ask_question(question)

    return {
        "question": question,
        "answer": answer
    }