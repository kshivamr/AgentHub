import argparse
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

load_dotenv()


class ResearchState(TypedDict):
    messages: Annotated[list, add_messages]
    query: str
    search_results: list[dict]
    report: str


def search_web(state: ResearchState) -> dict:
    tool = TavilySearch(max_results=5)

    raw_results = tool.invoke({
        "query": state["query"]
    })

    if isinstance(raw_results, dict):
        results = raw_results.get("results", [])
    elif isinstance(raw_results, list):
        results = raw_results
    else:
        results = []

    return {
        "search_results": results
    }


def synthesize_report(state: ResearchState) -> dict:
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0
    )

    results_text = "\n\n".join(
        f"Source: {r.get('url', 'N/A')}\n"
        f"Title: {r.get('title', 'N/A')}\n"
        f"Content: {r.get('content', '')[:500]}"
        for r in state["search_results"]
    )

    messages = [
        SystemMessage(
            content=(
                "You are a research analyst. "
                "Synthesize the search results into a clear, "
                "structured report with:\n"
                "1. Summary\n"
                "2. Key Findings (bullet points)\n"
                "3. Sources"
            )
        ),
        HumanMessage(
            content=(
                f"Research query: {state['query']}\n\n"
                f"Search results:\n{results_text}"
            )
        ),
    ]

    response = llm.invoke(messages)

    return {
        "report": response.content,
        "messages": [response]
    }


def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("search", search_web)
    graph.add_node("synthesize", synthesize_report)

    graph.set_entry_point("search")
    graph.add_edge("search", "synthesize")
    graph.add_edge("synthesize", END)

    return graph.compile()


def main():
    parser = argparse.ArgumentParser(
        description="Web Research Agent"
    )

    parser.add_argument(
        "--query",
        default="Stock price of Wipro of today",
        help="Research query"
    )

    args = parser.parse_args()

    print(f"\n🔍 Researching: {args.query}\n")

    agent = build_graph()

    result = agent.invoke({
        "query": args.query,
        "messages": [],
        "search_results": [],
        "report": ""
    })

    print("=" * 60)
    print("📄 RESEARCH REPORT")
    print("=" * 60)
    print(result["report"])


if __name__ == "__main__":
    main()
