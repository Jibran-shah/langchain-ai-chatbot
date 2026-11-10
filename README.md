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
│   ├──
