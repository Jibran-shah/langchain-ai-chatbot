
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from app.services import gemini_service

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(
    title="AI Chatbot API",
    description="Backend API for an AI-powered chatbot",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"message": "AI Chatbot API is running!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/chat")
def chat(request: ChatRequest):
    print("received", request.message)
    response = gemini_service.generate_response(request.message)
    print("returned")
    return {"reply": response}
