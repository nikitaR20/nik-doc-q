from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader, CSVLoader
from langchain.document_loaders import PyMuPDFLoader, CSVLoader
from langchain.docstore.document import Document
import os

def load_documents_from_folder(folder_path):
    folder_path = Path(folder_path)
    docs = []

    for file_path in folder_path.rglob("*"):
        if file_path.suffix.lower() == ".pdf":
            try:
                loader = PyMuPDFLoader(str(file_path))
                docs.extend(loader.load())
                #print(f"Loaded PDF: {file_path}")
            except Exception as e:
                print(f"Error loading PDF {file_path}: {e}")
        
        elif file_path.suffix.lower() == ".csv":
            try:
                loader = CSVLoader(str(file_path))
                docs.extend(loader.load())
                print(f"Loaded CSV: {file_path}")
            except Exception as e:
                print(f"Error loading CSV {file_path}: {e}")

    print(f"✅ Total documents loaded: {len(docs)}")
    return docs
