import os
from html_to_pdf import convert_htmls_and_collect_csvs
from config import FILE_PATH, MODEL_PATH, PDF_FILE_PATH, FAISS_INDEX_FILE
from load_files import load_documents_from_folder
from split_docs import split_documents
from create_embeddings import create_embeddings_for_chunks
from create_vector_store import create_and_save_vector_store
from ask_question import ask_question

if os.path.exists(FAISS_INDEX_FILE):
    print("✅ Vector store exists. Skipping document processing.")
else:
    print("⚠️ Vector store not found. Processing documents...")

    # convert_htmls_and_collect_csvs(FILE_PATH, PDF_FILE_PATH)

    all_docs = load_documents_from_folder(PDF_FILE_PATH)
    docs_chunks = split_documents(all_docs)
    
    embeddings, texts = create_embeddings_for_chunks(docs_chunks)
    create_and_save_vector_store(texts, embeddings)

print("✅ Setup complete. Ready for queries!")

# --- Interactive QA loop ---
while True:
    query = input("\n❓ Ask a question (type 'exit' to quit): ").strip()
    if query.lower() == "exit":
        print("👋 Exiting. Goodbye!")
        break

    response = ask_question(query)
    print(f"💡 Answer: {response}")
