"""This is a main file"""
from typing import Literal

from langgraph.graph import StateGraph, MessagesState
from labs.utils.utils import get_llm
from labs.tools.movie_search import movie_search
from labs.nodes.lab_tool_node import get_tool_node
LLM = get_llm()
LLM_WITH_TOOLS = LLM.bind_tools([movie_search])

def should_continue(state: MessagesState) -> Literal["tools", "__end__"]:
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return "__end__"

def call_model(state: MessagesState):
    messages = state["messages"]
    response = LLM_WITH_TOOLS.invoke(messages)
    return {"messages": [response]}

def main():
    """This is the main Function"""

    workflow = StateGraph(MessagesState)

    # Define the two nodes we will cycle between
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", get_tool_node())

    workflow.add_edge("__start__", "agent")
    workflow.add_conditional_edges(
        "agent",
        should_continue,
    )
    workflow.add_edge("tools", "agent")
    
    prompt = """
       You are an assistant helping Paul with his movie collection. He will ask about the availabity of movies in his collection.
       If using the movie_search tool, movies must be searched one at a time as a string, not as a list or array
    """
    app = workflow.compile()

    while True:
        print(":")
        question = input()
        query =  {"messages": [
            ("system", prompt),
            ("human", question)]}
        
        result = app.invoke(query)
        # for chunk in app.stream(query, stream_mode="values"):
        #     chunk["messages"][-1].pretty_print()
        print(result["messages"][-1].content)



    