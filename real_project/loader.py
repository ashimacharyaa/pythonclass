from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_pdf(file_path="transformerai.pdf"):
    print(f"📄 Reading {file_path}...")
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    
    # Split text into chunks to fit into the LLM context window
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)
    print(f"✂️ Sliced PDF into {len(chunks)} chunks.")
    return chunks