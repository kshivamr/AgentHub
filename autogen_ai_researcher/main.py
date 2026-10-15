import asyncio
from agents import agent, research_agent

async def main():
    first_result = await agent.run(
        task="Explain what RAG is in simple terms."
    )

    assistant_response = first_result.messages[-1].content

    second_result = await research_agent.run(
        task=f"Review this explanation and provide additional important information:\n\n{assistant_response}"
    )

    print("\nAssistant Agent:")
    print(assistant_response)

    print("\nResearch Agent:")
    print(second_result.messages[-1].content)

asyncio.run(main())