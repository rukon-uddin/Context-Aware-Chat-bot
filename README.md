# Context-Aware Chatbot with RAG
A lightweight and extensible Retrieval-Augmented Generation (RAG) based context-aware chatbot powered by OpenAI.
The chatbot retrieves relevant information from a vector database and supplies it as context to the LLM, allowing it to generate more accurate and grounded responses based on the user's knowledge base.

## ✨ Features

1. RAG-powered responses
2. Context-aware conversation
2. Vector database indexing & similarity search
3. Pluggable OpenAI/ChatGPT model
4. Run locally or inside Docker

## 📂 Repository Structure
```
├── main.py
├── llm_system.py
├── rag_system.py
├── utils.py
└── embed_model
│       ├── bge-base-en-v1.5-f16.gguf
```
## 🔧 Requirements
* Python 3.10+
* llama_cpp_python
* OpenAI API Key

## 🚀 Getting Started
### 1️⃣ Clone the Repository
```
git clone https://github.com/rukon-uddin/Context-Aware-Chat-bot.git

cd Context-Aware-Chat-bot
```

### 2️⃣ Download Embed Model and Install Dependencies
```
wget -P /main/embed_model https://huggingface.co/CompendiumLabs/bge-base-en-v1.5-gguf/resolve/main/bge-base-en-v1.5-f16.gguf

pip install -r requirements_local.txt
```

### 3️⃣ Set API Key
```
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

### 4️⃣ Run the Application
```
python main.py
```


## 🐳 Run with Docker

### 1️⃣ Clone the Repo
```
git clone https://github.com/rukon-uddin/Context-Aware-Chat-bot.git
cd Context-Aware-Chat-bot
```
### 2️⃣ Build the Docker Image
```
docker build -t raychatbot .
```
### 3️⃣ Run the Container
```
docker run -it raychatbot /bin/bash
```
### 4️⃣ Set API Key and Start
#### Inside the container:
```
export OPENAI_API_KEY="chatgpt api keyY"
python main.py
```

### 🧠 How It Works

1. User sends a query
2. The system searches a vector database for similar content
3. Retrieved text is passed as context to the LLM
4. The LLM generates a grounded and context-aware response


### ⚠️ Having Trouble Installing llama_cpp_python?

`llama_cpp_python` can sometimes fail to install on certain systems, especially Windows or machines missing compatible C/C++ build tools.

If you face any errors such as:
* `error: command 'gcc' failed`
* `fatal error: llama.h: No such file or directory`
* `Failed building wheel for llama_cpp_python`

👉 The easiest solution is to run the chatbot using Docker.
Docker provides a clean environment with all necessary dependencies pre-installed.

Just follow the Docker section above:
```
docker build -t raychatbot .
docker run -it raychatbot /bin/bash
export OPENAI_API_KEY="chatgpt api key"
python main.py
```

This avoids local compilation issues entirely.