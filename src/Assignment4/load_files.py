'''
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader, CSVLoader
#from langchain.document_loaders import PyMuPDFLoader, CSVLoader
from langchain_community.docstore.document import Document

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
'''
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader, CSVLoader
from langchain_community.docstore.document import Document
import pandas as pd
import os

def load_csv_as_documents(path):
    """Fallback CSV loader using pandas."""
    df = pd.read_csv(path)
    documents = []
    for idx, row in df.iterrows():
        content = row.to_string()
        documents.append(Document(page_content=content, metadata={"row": idx}))
    return documents

def load_documents_from_folder(folder_path):
    folder_path = Path(folder_path)
    docs = []

    for file_path in folder_path.rglob("*"):
        if file_path.suffix.lower() == ".pdf":
            try:
                loader = PyMuPDFLoader(str(file_path))
                docs.extend(loader.load())
                # print(f"Loaded PDF: {file_path}")
            except Exception as e:
                print(f"❌ Error loading PDF {file_path}: {e}")
        
        elif file_path.suffix.lower() == ".csv":
            try:
                loader = CSVLoader(file_path=str(file_path), csv_args={"delimiter": ","}, encoding="utf-8")
                loaded_docs = loader.load()
                if not loaded_docs:
                    raise ValueError("CSVLoader returned no documents")
                docs.extend(loaded_docs)
                print(f"✅ Loaded CSV using CSVLoader: {file_path}")
            except Exception as e:
                print(f"⚠️ CSVLoader failed: {e}. Using pandas fallback.")
                try:
                    fallback_docs = load_csv_as_documents(str(file_path))
                    docs.extend(fallback_docs)
                    print(f"✅ Loaded CSV using pandas fallback: {file_path}")
                except Exception as fallback_error:
                    print(f"❌ Fallback also failed for {file_path}: {fallback_error}")

    print(f"\n✅ Total documents loaded: {len(docs)}")
    return docs
