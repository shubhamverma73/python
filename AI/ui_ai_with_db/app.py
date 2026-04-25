"""
Flask web app for chatting with a MySQL database using:
- Flask for browser-based UI and API routes
- LangChain + ChatOllama for local LLM access
- SQLDatabase + create_sql_query_chain for natural-language-to-SQL

What this app does:
1. Shows a chat UI in the browser.
2. Accepts a user question.
3. Uses the LLM to create a SQL query for allowed MySQL tables.
4. Executes the SQL query on a read-only database connection.
5. Uses the LLM again to convert raw SQL results into a human-friendly answer.

IMPORTANT SECURITY NOTES:
- Use a READ-ONLY MySQL user.
- Only allow required tables.
- This sample blocks obvious write/delete statements, but DB permissions are the real protection.
"""

import os
from dotenv import load_dotenv
load_dotenv()
import re
from flask import Flask, render_template, request, jsonify
from langchain_ollama import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain_classic.chains import create_sql_query_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

app = Flask(__name__)

# -----------------------------------------------------------------------------
# 1) APP CONFIGURATION
# -----------------------------------------------------------------------------
# Put your MySQL details in environment variables before running the app.
# Example:
#   export DB_USER=readonly_user
#   export DB_PASSWORD=your_password
#   export DB_HOST=127.0.0.1
#   export DB_PORT=3306
#   export DB_NAME=my_database
#   export OLLAMA_MODEL=llama3:8b
#
# If you don't set OLLAMA_MODEL, the app will default to llama3:8b.
#
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "python")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3:8b")

# Restrict the app to only the tables that are needed.
# You can edit this list based on your schema.
ALLOWED_TABLES = ["users", "users_plan", "plans"]

# -----------------------------------------------------------------------------
# 2) DATABASE SETUP
# -----------------------------------------------------------------------------
# LangChain uses SQLAlchemy under the hood. For MySQL, PyMySQL is a common driver.
# Connection URI format:
#   mysql+pymysql://username:password@host:port/db_name
#
DATABASE_URI = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("DB_PASSWORD =", repr(DB_PASSWORD))
print("DB_HOST =", DB_HOST)
print("DB_PORT =", DB_PORT)
print("DB_NAME =", DB_NAME)
print("DATABASE_URI =", DATABASE_URI)

# -----------------------------------------------------------------------------
# 3) LLM SETUP
# -----------------------------------------------------------------------------
# This is the same local model you were already using in your terminal app.
# Now it will be used inside a browser-based web app.
#
llm = ChatOllama(model=OLLAMA_MODEL)

# Basic chat history for conversational continuity in the browser.
# This is global for simplicity in a local demo app.
# For multi-user production apps, use per-user sessions or a database.
chat_history = [
    SystemMessage(
        content=(
            "You are a helpful AI assistant connected to a SQL database. "
            "Answer clearly. Use the SQL result provided to you. "
            "Do not invent facts that are not present in the database result."
        )
    )
]

# Create the database wrapper.
# sample_rows_in_table_info helps the LLM understand the table structure better.
# include_tables restricts schema exposure to only the tables you approve.
#
try:
    db = SQLDatabase.from_uri(
        DATABASE_URI,
        include_tables=ALLOWED_TABLES,
        sample_rows_in_table_info=2,
    )
    print("Database connected successfully in LangChain")
except Exception as e:
    print("Database connection error:", str(e))
    db = None

# -----------------------------------------------------------------------------
# 4) SQL GENERATION CHAIN
# -----------------------------------------------------------------------------
# This chain converts a natural-language question into a SQL query.
# We keep it focused on allowed tables and read-only style usage.
#
sql_prompt = ChatPromptTemplate.from_template(
    """
You are a careful SQL assistant.

Database dialect: {dialect}

Only use the following tables:
{table_info}

Rules:
- Generate only one syntactically correct SELECT query.
- Never generate INSERT, UPDATE, DELETE, DROP, TRUNCATE, ALTER, CREATE, REPLACE, GRANT, or REVOKE.
- Use only the tables and columns that are visible in the provided schema.
- Never use columns that are not present in the schema.
- Do not use SELECT * unless absolutely necessary.
- Return at most {top_k} rows unless the question clearly requires a count or aggregation.
- If the question asks for highest, lowest, cheapest, most expensive, latest, oldest, biggest, smallest, or top item, include:
  1. the main descriptive column (such as name/title/type), and
  2. the compared numeric/date column (such as price, amount, validity, created_at, count).
- For pricing-related questions, always include the plan/item name and price in the SELECT clause.
- For count-related questions, use COUNT(...) and return only the count column unless extra detail is explicitly needed.
- If a join is needed, infer it carefully from matching key columns.
- Return only raw SQL.
- Do not return markdown.
- Do not return explanation text.

Question: {input}
SQLQuery:
"""
)

sql_query_chain = create_sql_query_chain(llm, db, prompt=sql_prompt) if db else None

# -----------------------------------------------------------------------------
# 5) RESULT-TO-ANSWER CHAIN
# -----------------------------------------------------------------------------
# After SQL runs, we ask the LLM to explain the result in plain language.
# This keeps the browser output user-friendly instead of showing raw tuples.
#
answer_prompt = ChatPromptTemplate.from_template(
    """
You are a helpful data assistant.

User question:
{question}

Generated SQL:
{query}

SQL result:
{result}

Instructions:
- Answer in clear, user-friendly language.
- Base the answer only on the SQL result.
- If the result contains price, amount, count, date, validity, or any important numeric field, mention it explicitly in the answer.
- If the result is empty, clearly say that no matching data was found.
- If useful, present a short summary with bullet-like formatting in plain text.
"""
)

answer_chain = answer_prompt | llm | StrOutputParser()

# -----------------------------------------------------------------------------
# 6) HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def clean_sql_query(query: str) -> str:
    """
    Remove markdown fences and extra labels if the model returns them.
    The SQL chain usually returns raw SQL, but this cleanup makes the app safer.
    """
    query = query.strip()
    query = query.replace("```sql", "").replace("```", "").strip()
    query = re.sub(r"^SQLQuery:\s*", "", query, flags=re.IGNORECASE)
    return query.strip()


def is_safe_select_query(query: str) -> bool:
    """
    Very basic SQL safety check.
    This is NOT enough by itself; database permissions are the real protection.
    We only allow queries that start with SELECT or WITH and block obvious write ops.
    """
    lowered = query.lower().strip()

    dangerous_keywords = [
        "insert ", "update ", "delete ", "drop ", "truncate ", "alter ",
        "create ", "replace ", "grant ", "revoke ", "rename ", "call ",
    ]

    if not (lowered.startswith("select") or lowered.startswith("with")):
        return False

    if any(keyword in lowered for keyword in dangerous_keywords):
        return False

    return True


def answer_database_question(user_question: str) -> dict:
    """
    End-to-end database QA flow:
    1. Generate SQL from the user question.
    2. Clean and validate SQL.
    3. Run SQL on MySQL.
    4. Convert raw results into a natural-language answer.

    Returns a dict so the frontend can optionally show debug info.
    """
    if not db or not sql_query_chain:
        return {
            "ok": False,
            "error": "Database connection is not available. Check DB settings and MySQL server.",
        }

    # Tell the SQL chain which tables are allowed for this question.
    raw_query = sql_query_chain.invoke(
        {
            "question": user_question,
            "table_names_to_use": ALLOWED_TABLES,
        }
    )

    query = clean_sql_query(raw_query)

    if not is_safe_select_query(query):
        return {
            "ok": False,
            "error": "Generated query was blocked by safety rules.",
            "query": query,
        }

    # Run the SQL query and get raw DB results.
    result = db.run(query)

    # Convert SQL result into a readable answer.
    final_answer = answer_chain.invoke(
        {
            "question": user_question,
            "query": query,
            "result": result,
        }
    )

    return {
        "ok": True,
        "query": query,
        "result": str(result),
        "answer": final_answer,
    }


# -----------------------------------------------------------------------------
# 7) FLASK ROUTES
# -----------------------------------------------------------------------------
@app.route("/")
def index():
    """Render the main browser UI."""
    return render_template(
        "index.html",
        model_name=OLLAMA_MODEL,
        db_name=DB_NAME,
        allowed_tables=", ".join(ALLOWED_TABLES),
    )


@app.route("/chat", methods=["POST"])
def chat():
    """
    Main chat endpoint for the browser.

    Expected JSON body:
    {
      "message": "Which recharge plan has the highest price?"
    }

    Response JSON:
    {
      "reply": "...human friendly answer...",
      "query": "SELECT ...",
      "result": "[(...)]"
    }
    """
    global chat_history

    data = request.get_json(silent=True) or {}
    user_input = (data.get("message") or "").strip()

    if not user_input:
        return jsonify({"error": "Message is required."}), 400

    # Store user message in chat history.
    chat_history.append(HumanMessage(content=user_input))

    try:
        response = answer_database_question(user_input)

        if not response["ok"]:
            return jsonify({
                "error": response["error"],
                "query": response.get("query", "")
            }), 500

        # Store assistant answer in history.
        chat_history.append(AIMessage(content=response["answer"]))

        return jsonify({
            "reply": response["answer"],
            "query": response["query"],
            "result": response["result"],
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/reset", methods=["POST"])
def reset():
    """Reset in-memory chat history."""
    global chat_history
    chat_history = [
        SystemMessage(
            content=(
                "You are a helpful AI assistant connected to a SQL database. "
                "Answer clearly. Use the SQL result provided to you. "
                "Do not invent facts that are not present in the database result."
            )
        )
    ]
    return jsonify({"ok": True})


@app.route("/health")
def health():
    """Quick health endpoint to check if app is alive and DB object is ready."""
    return jsonify({
        "status": "ok",
        "model": OLLAMA_MODEL,
        "db_connected": db is not None,
        "allowed_tables": ALLOWED_TABLES,
    })


# -----------------------------------------------------------------------------
# 8) APP ENTRY POINT
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # debug=True is useful in local development.
    # For production, use a proper WSGI server and debug=False.
    app.run(debug=True, host="0.0.0.0", port=5000)
