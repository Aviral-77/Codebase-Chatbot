# Codebase-Chatbot

An interactive chatbot built using Chainlit, LlamaIndex, and Ollama, designed to answer natural language questions over any GitHub repository. It uses Retrieval-Augmented Generation (RAG) with local LLMs and embeddings to provide context-aware answers based on source code files.

✨ Features
🔍 Ingests GitHub Repositories (skips media files)

🧠 Vector-based Indexing using LlamaIndex

💬 Conversational Chat UI powered by Chainlit

🧩 Embeddings via HuggingFace

🦙 Local LLM support via Ollama (e.g., llama3)

🗃️ Persistent Index Storage for faster reloads

🛠️ Installation
1. Clone this repository
`git clone https://github.com/Aviral-77/Codebase-Chatbot.git`
`cd Codebase-Chatbot`

2. Install dependencies:
`pip install -r requirements.txt`


⚙️ Configuration
Set your credentials and repo information in config.py:

```
OPENAI_API_KEY = "your-openai-api-key"  # Optional, if using OpenAI
GITHUB_TOKEN = "your-github-token"

GITHUB_OWNER = "your-github-username"
GITHUB_REPO = "target-repository-name"
GITHUB_BRANCH = "main"  # or another branch
```

🧪 Running the Bot
Make sure you have Ollama running locally and the desired model (like llama3) installed:
`ollama run llama3`


Then, start the chatbot:
`chainlit run app.py`
Open the browser window that Chainlit provides. You're ready to chat!
