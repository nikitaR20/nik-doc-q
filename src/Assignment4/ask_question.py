from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import LlamaCpp
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import MODEL_PATH, FAISS_INDEX_FILE

def load_llm():
    return LlamaCpp(
        model_path=MODEL_PATH,
        n_ctx=2048,
        n_threads=8,
        n_gpu_layers=0,
        temperature=0.1,
        max_tokens=512,
        verbose=False
    )

def load_vector_store():
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(FAISS_INDEX_FILE, embedding_model, allow_dangerous_deserialization=True)
    return vectorstore

def ask_question(question: str):
    llm = load_llm()
    vectorstore = load_vector_store()

    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )

    response = qa_chain.invoke(question)  # use invoke instead of run
    return response
