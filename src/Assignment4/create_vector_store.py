from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import FAISS_INDEX_FILE

def create_and_save_vector_store(texts, embeddings):
    """
    Create and save a LangChain-compatible FAISS vector store.

    Args:
        texts (List[str]): List of document chunk strings.
        embeddings (np.ndarray): Corresponding vector embeddings.
    """
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    text_embeddings = list(zip(texts, embeddings))
    vectorstore = FAISS.from_embeddings(text_embeddings, embedding_model)
    vectorstore.save_local(FAISS_INDEX_FILE)
    print(f"✅ Vector store saved at: {FAISS_INDEX_FILE}")
