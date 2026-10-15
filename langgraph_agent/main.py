import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition

from tools import calculator, get_user_data, calculat_currency

load_dotenv()

tools = [
    calculator,
    get_user_data,
    calculat_currency
]

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

llm_with_tools = llm.bind_tools(tools)


def agent(state: MessagesState):
    messages = [
        (
            "system",
            "You are a helpful assistant. Use get_user_data when the user asks about the user's name, company, or age. Use calculator for mathematical calculations. Use calculat_currency for currency conversion."
        )
    ] + state["messages"]

    response = llm_with_tools.invoke(messages)

    return {"messages": [response]}


new = StateGraph(MessagesState)

new.add_node("agent", agent)
new.add_node("tools", ToolNode(tools))

new.add_edge(START, "agent")
new.add_conditional_edges("agent", tools_condition)
new.add_edge("tools", "agent")

graph = new.compile()

result = graph.invoke({
    "messages": [
        ("user", "What is the value of 3165465 in euro")
    ]
})

print(result["messages"][-1].content)