# import os
# from dotenv import load_dotenv
# from agents import (
#     Agent,
#     Runner,
#     OpenAIChatCompletionsModel,
#     AsyncOpenAI,
#     set_tracing_disabled
# )

# load_dotenv()
# from tools import calculator,get_user_data,currency_calculator

# set_tracing_disabled(True)

# client = AsyncOpenAI(
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url="https://api.groq.com/openai/v1"
# )

# model = OpenAIChatCompletionsModel(
#     model="gpt-5-mini",
#     openai_client=client
# )

# agent = Agent(
#     name="MultiTool Agent",
#     instructions="You are a helpful AI assistant. Use the calculator tool whenever mathematical calculation is required.",
#     model=model,
#     tools = [calculator, get_user_data, currency_calculator]

# )

# result = Runner.run_sync(
#     agent,
#     "What is 125 multiplied by 24?",
#     "What is the value of 24 rupees in dollar",
#     "What is the name of company"
# )

# print(result.final_output)

import os
from dotenv import load_dotenv
from agents import Agent, Runner, set_tracing_disabled
from tools import calculator, get_user_data, currency_calculator

load_dotenv()

agent = Agent(
    name="MultiTool Agent",
    instructions="You are a helpful AI assistant. Use the appropriate tool whenever required.",
    model="gpt-5-mini",
    tools=[calculator, get_user_data, currency_calculator]
)

result = Runner.run_sync(
    agent,
    "What is 125 multiplied by 24?"
)

print(result.final_output)