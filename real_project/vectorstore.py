from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

def create_vector_store(chunks):
    print("🧠 Generating text embeddings using Google Gemini and storing in Vector DB...")
    
    # Initialize the Google embedding engine
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
    
    # Clean out any empty text fragments to guarantee safety
    valid_chunks = [chunk for chunk in chunks if chunk.page_content.strip()]
    
    # Build a secure, bulletproof in-memory database
    vectorstore = InMemoryVectorStore.from_documents(valid_chunks, embeddings)
    return vectorstore