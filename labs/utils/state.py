import operator
from typing_extensions import TypedDict
from typing import List, Annotated, Sequence
from langchain_core.documents.base import Document
from langchain_core.messages import BaseMessage

class GraphState(TypedDict):
    """
    Graph state is a dictionary that contains information we want to propagate to, and modify in, each graph node.
    """
    question : str # User question
    documents : List[Document] # List of retrieved documents
    loop_step : int
    generation : str # LLM generation
    messages: Annotated[Sequence[BaseMessage], operator.add]