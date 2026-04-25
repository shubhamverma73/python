from flask import Flask, render_template, request, jsonify
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

app = Flask(__name__)

llm = ChatOllama(model="llama3:8b")

chat_history = [
    SystemMessage(content="You are a helpful AI assistant. Answer clearly and accurately.")
]

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/chat")
def chat():
    global chat_history
    data = request.get_json(silent=True) or {}
    user_input = (data.get("message") or "").strip()

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    chat_history.append(HumanMessage(content=user_input))

    try:
        response = llm.invoke(chat_history)
        answer = response.content if hasattr(response, "content") else str(response)
        chat_history.append(AIMessage(content=answer))
        return jsonify({"reply": answer})
    except Exception as e:
        if chat_history and isinstance(chat_history[-1], HumanMessage):
            chat_history.pop()
        return jsonify({"error": str(e)}), 500

@app.post("/reset")
def reset():
    global chat_history
    chat_history = [
        SystemMessage(content="You are a helpful AI assistant. Answer clearly and accurately.")
    ]
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
