from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

def create_rag_chain(vectorstore):
    # FIX: Switched from gemini-1.5-flash to gemini-2.5-flash
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    
    system_prompt = (
        "You are a helpful assistant. Answer the question using ONLY the provided PDF context below. "
        "If you do not know the answer based on the context, say that you don't know.\n\n"
        "Context:\n{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain