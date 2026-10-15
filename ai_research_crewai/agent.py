import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

llm = LLM(
    model = "openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

research_agent = Agent(
    role = "AI Researcher",
    goal = "Research a given topic and provide accurate and useful information.",
    backstory = "You are an experienced AI resercher who specializes in finding and organizing important information.",
    llm = llm,
    verbose = True
)