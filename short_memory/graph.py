import os
from typing import Annotated
from typing_extensions import TypedDict

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()


class TravelState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)


def travel_agent(state: TravelState):
    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }


builder = StateGraph(TravelState)

builder.add_node("travel_agent", travel_agent)

builder.add_edge(START, "travel_agent")

memory = InMemorySaver()

graph = builder.compile(checkpointer=memory)