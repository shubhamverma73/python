# Local Ollama Chat WebApp

A small browser-based chat UI for your local `llama3:8b` assistant using Flask + LangChain + Ollama.

## Run steps

1. Install Ollama and pull the model:
   ```bash
   ollama pull llama3:8b
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   python app.py
   ```
4. Open in browser:
   ```
   http://127.0.0.1:5000
   ```

## Features

- Clean browser UI
- Chat history maintained on server
- Reset chat button
- Enter to send, Shift+Enter for newline
- Uses your existing local Ollama setup
