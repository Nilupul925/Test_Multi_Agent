# This is a multi-agent ai platform to practice :)
import os

from crewai import LLM, Agent, Crew, Process, Task
from dotenv import load_dotenv

# Getting API key
load_dotenv()

# Setup Gemni AI model for CewAI
llm = LLM(model="gemini-3.5-flash-lite", api_key=os.getenv("GEMINI_API_KEY"))

print("🚀 Agents are starting there works...")

# First agent: Researcher
researcher = Agent(
    role="Senior Cloud Researcher",
    goal="Finding clear technical information regarding Docker and Containerization technology.",
    backstory="You are a researcher with many years of experience in cloud technology, who studies modern technologies in depth.",
    verbose=True,  # Show there works in terminal
    allow_delegation=False,
    llm=llm,
)

# Second Agent: Writer
writer = Agent(
    role="Technical Writer",
    goal="Transforming complex technical information provided by a researcher into simple article that is understandable to the general public.",
    backstory="You are a talented writer capable of explaining complex technical matters in a very simple and engaging way.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

# Creating duties to be performed
researcher_task = Task(
    description="Outline 3 key points regarding what Docker is and why it is important for software engineers.",
    expected_output="A short technical report containing 3 clear points about Docker.",
    agent=researcher,
)

write_task = Task(
    description="Using the technical report provided by the researcher, write a short blog post about Docker, tailored for beginners. It should consist of three paragraphs.",
    expected_output="A simple blog post with an engaging title and 3 paragraphs.",
    agent=writer,
)

# Setup crew and starting their duties
tech_crew = Crew(
    agents=[researcher, writer],
    tasks=[researcher_task, write_task],
    process=Process.sequential,  # Complete tasks properly step by step
)

result = tech_crew.kickoff()

print("\n" + "=" * 50)
print("✅ Final Result (Written by Technical Writer): ")
print("=" * 50 + "\n")
print(result)
