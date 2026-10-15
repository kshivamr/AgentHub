import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()

model_client = OpenAIChatCompletionClient(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "family": "unknown",
        "structured_output": True
    }
)

agent = AssistantAgent(
    name="assistant",
    model_client=model_client
)

research_agent = AssistantAgent(
    name="researcher",
    model_client=model_client,
    system_message="You are a research specialist. Provide accurate and well-structured research information."
)