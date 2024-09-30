import operator
from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import MemorySaver
from labs.nodes.grader import grade_documents
from typing_extensions import TypedDict
from typing import List, Annotated
from langchain_core.documents.base import Document

class GraphState(TypedDict):
    """
    Graph state is a dictionary that contains information we want to propagate to, and modify in, each graph node.
    """
    question : str # User question
    documents : List[str] # List of retrieved documents

def test_retrieve():
    workflow = StateGraph(GraphState)
    workflow.add_node("grade", grade_documents) # retrieve
    memory = MemorySaver()

    number_of_batman_movies = 3

    documents = [
        Document("Batman Begins"),
        Document("The Dark Knight"),
        Document("The Dark Knight Rises"),
        Document("The Bourne Identity"),   # This is not a batman movie...
    ]

    workflow.set_entry_point("grade")
    workflow.add_edge("grade", END)
    graph = workflow.compile(checkpointer=memory)

    inputs = {"question": "Are these batman movies", "documents" : documents}
    config = {"configurable": {"thread_id": "1"}} # This is just so I can view the state later

    graph.invoke(inputs, config)
    graph_state = graph.get_state(config)
    print(graph_state.values['documents'])
    assert len(graph_state.values['documents']) == number_of_batman_movies






