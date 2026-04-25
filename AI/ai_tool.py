from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOllama(model="llama3:8b")

chat_history = [
    SystemMessage(content="You are a helpful AI assistant. Answer clearly and accurately.")
]

print("🤖 Local Ollama Agent started. Ask your question.")
print("Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Bye!")
        break

    chat_history.append(HumanMessage(content=user_input))

    try:
        response = llm.invoke(chat_history)
        print("Bot:", response.content)
        chat_history.append(AIMessage(content=response.content))
    except Exception as e:
        print("❌ Error:", str(e))