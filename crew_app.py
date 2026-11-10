import os

from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Getting API key
load_dotenv()

# Setup Gemni AI model for CewAI
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY")
)

print("🚀 Agents are starting there works...")

# First agent: Researcher
researcher = Agent(
    role="Senior Cloud Researcher",
    goal="Finding clear technical information regarding Cybersecurity and Networking technology.",
    backstory="You are a researcher with many years of experience in Cybersecurity and Networking technology, who studies modern technologies in depth.",
    verbose=True,  # Show there works in terminal
    allow_delegation=False,
    llm=llm,
)
