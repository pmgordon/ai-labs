import operator
from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import MemorySaver
from labs.nodes.retriever import retrieve
from typing_extensions import TypedDict
from typing import List, Annotated

class GraphState(TypedDict):
    """
    Graph state is a dictionary that contains information we want to propagate to, and modify in, each graph node.
    """
    question : str # User question
    documents : List[str] # List of retrieved documents

def test_retrieve():
    workflow = StateGraph(GraphState)
    workflow.add_node("retrieve", retrieve) # retrieve
    memory = MemorySaver()

    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", END)
    graph = workflow.compile(checkpointer=memory)

    inputs = {"question": "Batman"}
    config = {"configurable": {"thread_id": "1"}} # This is just so I can view the state later

    graph.invoke(inputs, config)
    graph_state = graph.get_state(config)
    print(graph_state.values['documents'])
    assert len(graph_state.values['documents']) == 4






