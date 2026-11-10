import os

from crewai import LLM
from dotenv import load_dotenv

# Getting API keys
load_dotenv()
llm = LLM(model="gemini-3.5-flash-lite", api_key=os.getenv("GEMINI_API_KEY"))
