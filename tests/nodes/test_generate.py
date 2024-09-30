import operator
from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import MemorySaver
from labs.nodes.generate import generate
from typing_extensions import TypedDict
from typing import List
from langchain_core.documents.base import Document

class GraphState(TypedDict):
    """
    Graph state is a dictionary that contains information we want to propagate to, and modify in, each graph node.
    """
    question : str # User question
    documents : List[str] # List of retrieved documents
    loop_step : int
    generation : str # LLM generation

def test_generate():
    workflow = StateGraph(GraphState)
    workflow.add_node("generate", generate) # retrieve
    memory = MemorySaver()

    number_of_batman_movies = 3

    documents = [
        Document("Batman Begins"),
        Document("The Dark Knight"),
        Document("The Dark Knight Rises"),
        Document("Inception")
    ]

    workflow.set_entry_point("generate")
    workflow.add_edge("generate", END)
    graph = workflow.compile(checkpointer=memory)

    inputs = {"question": "Are these batman movies", "documents" : documents}
    config = {"configurable": {"thread_id": "1"}} # This is just so I can view the state later

    result = graph.invoke(inputs, config)
    print(result['generation'].content)
    






