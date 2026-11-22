# Local LLM Chat

A lightweight local AI chatbot built with **Python, Streamlit, and Ollama**, powered by Qwen2.5 0.5B Instruct. Chat with a locally running LLM through a simple web interface without paid API access.

## Features

- Local LLM inference
- Interactive chat interface
- Conversation history
- Model selection
- Clear conversation option
- Python integration with Ollama API
- No paid LLM API required

## Tech Stack

- Python
- Streamlit
- Requests
- Ollama
- Qwen2.5-0.5B-Instruct

## Project Structure

```text
local-llm-chat/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Installation & Setup (Windows)

### Step 1: Install Ollama

Download and install Ollama for Windows:

https://ollama.com/download   or 
 
Run in powershell 

irm https://ollama.com/install.ps1 | iex

Verify the installation using Command Prompt:

```cmd
ollama --version
```

### Step 2: Download the LLM locally

Download Qwen2.5 0.5B using Ollama:

```cmd
ollama pull qwen2.5:0.5b
```

The model will be downloaded and stored locally on your computer.

### Step 3: Run the model

```cmd
ollama run qwen2.5:0.5b
```

Test the model by entering a prompt in the terminal.

Exit the model using:

```text
/bye
```

### Step 4: Clone the repository

```cmd
git clone https://github.com/YOUR-USERNAME/local-llm-chat.git
```

Navigate into the project directory:

```cmd
cd local-llm-chat
```

### Step 5: Install Python dependencies

```cmd
pip install -r requirements.txt
```

### Step 6: Run the application

```cmd
streamlit run app.py
```

Streamlit will launch the application in your browser, usually at:

http://localhost:8501

## How It Works

```text
User Input
    ↓
Streamlit Chat Interface
    ↓
Python Application
    ↓
Ollama Local API
    ↓
Qwen2.5 0.5B Model
    ↓
Generated Response
    ↓
Chat Interface
```

The application sends user prompts and conversation history to Ollama's local API. Ollama performs inference using the locally downloaded model and returns the generated response to the Streamlit interface.

## License

This project is licensed under the MIT License.
