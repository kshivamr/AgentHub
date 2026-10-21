from graph import graph


user_a = {
    "configurable": {
        "thread_id": "user-A"
    }
}

user_b = {
    "configurable": {
        "thread_id": "user-B"
    }
}


graph.invoke(
    {
        "messages": [
            ("user", "I want to travel from Delhi to Dubai.")
        ]
    },
    user_a
)


graph.invoke(
    {
        "messages": [
            ("user", "I want to travel from Mumbai to London.")
        ]
    },
    user_b
)


result_a = graph.invoke(
    {
        "messages": [
            ("user", "What was my destination?")
        ]
    },
    user_a
)


result_b = graph.invoke(
    {
        "messages": [
            ("user", "What was my destination?")
        ]
    },
    user_b
)


print("\nUser A:")
print(result_a["messages"][-1].content)

print("\nUser B:")
print(result_b["messages"][-1].content)