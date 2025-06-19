from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(docs, chunk_size=1000, chunk_overlap=100):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    docs_chunks = text_splitter.split_documents(docs)
    print(f"Total chunks created: {len(docs_chunks)}")
    return docs_chunks
