# AI Chatbot

An AI-powered conversational chatbot built with Python, LangChain, and Google Gemini. The application maintains conversation history and generates context-aware responses, providing a continuous conversational experience.

## Features

- Integration with Google Gemini LLM.
- Prompt templates for controlling AI responses.
- Conversation history management.
- Context-aware responses based on previous messages.
- Unique conversation IDs for maintaining separate conversations.
- REST API for handling chat requests.
- FastAPI backend.

## Tech Stack

- **Language:** Python
- **Backend:** FastAPI
- **AI Framework:** LangChain
- **LLM:** Google Gemini
- **API Communication:** REST API

## How It Works

1. The user sends a message along with a conversation ID.
2. The backend retrieves the relevant conversation history.
3. LangChain prepares the prompt using the conversation context.
4. Google Gemini generates a response.
5. The response is returned to the user.
6. The conversation is updated with the new messages.

## Project Structure

```text
AI-Chatbot/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

**1. Clone the repository**

```bash
git clone <repository-url>
cd AI-Chatbot
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Configure environment variables**

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

**6. Run the application**

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Learning Objectives

- Understanding LLM integration.
- Working with LangChain and Google Gemini.
- Designing prompts using prompt templates.
- Managing conversation history.
- Implementing context-aware AI responses.
- Building AI-powered REST APIs with FastAPI.

## Author

**Jibran Shah**

- GitHub: https://github.com/Jibran-shah
- LinkedIn: https://linkedin.com/in/jibran-shah-0a6240283
