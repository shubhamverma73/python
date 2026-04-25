# Ollama SQL Chat WebApp

A browser-based Flask app that lets you ask MySQL database questions in natural language using:
- Ollama (`llama3:8b` by default)
- LangChain SQL query generation
- MySQL via SQLAlchemy + PyMySQL

## What this app does

1. User asks a question in the browser.
2. The LLM generates a SQL query for allowed tables.
3. The app runs that query on MySQL.
4. The LLM converts the SQL result into a human-friendly answer.

## Important security rule

Use a **READ-ONLY** MySQL user.
Do **not** use root or any user with write/delete permissions.

## Suggested tables

The app is preconfigured for these tables:
- `users`
- `users_plan`
- `recharge_plan`

You can change `ALLOWED_TABLES` in `app.py`.

## Setup

### 1) Pull the Ollama model

```bash
ollama pull llama3:8b
```

### 2) Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3) Set environment variables

Linux/macOS:

```bash
export DB_USER=readonly_user
export DB_PASSWORD=your_password
export DB_HOST=127.0.0.1
export DB_PORT=3306
export DB_NAME=my_database
export OLLAMA_MODEL=llama3:8b
```

Windows PowerShell:

```powershell
$env:DB_USER="readonly_user"
$env:DB_PASSWORD="your_password"
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="3306"
$env:DB_NAME="my_database"
$env:OLLAMA_MODEL="llama3:8b"
```

### 4) Run the Flask app

```bash
python app.py
```

### 5) Open in the browser

```text
http://127.0.0.1:5000
```

## Example questions

- Which recharge plan has the highest price?
- How many users are on active plans?
- Show users with their selected plans.
- What is the cheapest recharge plan?

## Notes

- This project uses a global in-memory chat history for simplicity.
- For production, use per-user session storage.
- Query safety is partially checked in code, but **DB permissions are the real protection**.
