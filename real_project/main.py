import config  # This triggers the automatic .env key verification
from loader import load_and_split_pdf
from vectorstore import create_vector_store
from chain import create_rag_chain

def run_chatbot():
    # 1. Process the PDF
    chunks = load_and_split_pdf("transformerai.pdf")
    
    # 2. Build the database
    vectorstore = create_vector_store(chunks)
    
    # 3. Create the AI brain chain
    bot = create_rag_chain(vectorstore)
    
    print("\n🚀 Chatbot is ready! Ask your PDF anything (Type 'exit' to quit)...\n")
    
    # 4. Interactive loop for chatting
    while True:
        user_query = input("You: ")
        if user_query.lower() in ['exit', 'quit']:
            print("Goodbye! 👋")
            break
            
        if not user_query.strip():
            continue
            
        print("🤖 Thinking...")
        response = bot.invoke({"input": user_query})
        print(f"\nAI: {response['answer']}\n" + "-"*40)

if __name__ == "__main__":
    run_chatbot()