from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama

import re

# ✅ LLM (Ollama - NO API KEY needed)
#llm = Ollama(model="llama3")
llm = Ollama(model="llama3:8b")

# ✅ Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ✅ Data store
application_info = {
    "name": None,
    "email": None,
    "skills": None
}

# ✅ Tool 1
def extract_application_info(text: str) -> str:
    name_match = re.search(r"(?:my name is|i am)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)", text, re.IGNORECASE)
    email_match = re.search(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)
    skills_match = re.search(r"(?:skills are|i know|i can use)\s+(.+)", text, re.IGNORECASE)

    response = []

    if name_match:
        application_info["name"] = name_match.group(1).title()
        response.append("✅ Name saved.")

    if email_match:
        application_info["email"] = email_match.group(0)
        response.append("✅ Email saved.")

    if skills_match:
        application_info["skills"] = skills_match.group(1).strip()
        response.append("✅ Skills saved.")

    if not any([name_match, email_match, skills_match]):
        return "❓ I couldn't extract any info."

    return " ".join(response)


# ✅ Tool 2
def check_application_goal(_: str) -> str:
    if all(application_info.values()):
        return f"✅ You're ready! Name: {application_info['name']}, Email: {application_info['email']}, Skills: {application_info['skills']}."
    else:
        missing = [k for k, v in application_info.items() if not v]
        return f"⏳ Still need: {', '.join(missing)}."


# ✅ Tools
tools = [
    Tool(
        name="extract_application_info",
        func=extract_application_info,
        description="Extract name, email, and skills from user input."
    ),
    Tool(
        name="check_application_goal",
        func=check_application_goal,
        description="Check if all required info is collected."
    )
]

# ✅ Agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# ✅ Start
print("📝 Hi! Tell me your name, email, and skills.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Bye!")
        break

    response = agent.invoke({"input": user_input})
    print("Bot:", response["output"])

    if "you're ready" in response["output"].lower():
        print("🎉 Application complete!")
        break