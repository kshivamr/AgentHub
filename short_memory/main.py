from graph import graph


config = {
    "configurable": {
        "thread_id": "travel-1"
    }
}


result = graph.invoke(
    {
        "messages": [
            ("user", "I want to travel from Delhi to Dubai.")
        ]
    },
    config
)

print("\nFirst response:")
print(result["messages"][-1].content)


result = graph.invoke(
    {
        "messages": [
            ("user", "What was my destination?")
        ]
    },
    config
)

print("\nSecond response:")
print(result["messages"][-1].content)