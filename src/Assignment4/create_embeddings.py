from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model once globally
model = SentenceTransformer("all-MiniLM-L6-v2")  # or your local model

def create_embeddings_for_chunks(docs_chunks):
    """
    Create embeddings for split document chunks.
    Always creates embeddings fresh from docs_chunks.
    """
    texts = [doc.page_content for doc in docs_chunks]
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    print(f"✅ Created embeddings for {len(texts)} chunks. Each vector size: {embeddings[0].shape[0]}")

    # Save embeddings for later use if you want
    np.save("embeddings.npy", embeddings)
    print("Saved embeddings to embeddings.npy")

    return embeddings, texts
