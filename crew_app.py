import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Getting API key
load_dotenv()

# Setup Gemni AI model for CewAI
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY")
)

print("🚀 Agents are starting there works...")
