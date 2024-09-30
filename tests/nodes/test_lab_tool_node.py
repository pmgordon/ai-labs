from typing import List
from langgraph.graph import StateGraph, END, START
from typing_extensions import Annotated, TypedDict
from langgraph.checkpoint.memory import MemorySaver

from langchain_core.messages import BaseMessage, AIMessage, HumanMessage
from langgraph.prebuilt import InjectedState, ToolNode
from labs.utils.utils import get_llm

from labs.nodes.lab_tool_node import get_tool_node
from labs.tools.movie_search import movie_search


class AgentState(TypedDict):
    messages: List[BaseMessage]

def test_llm_with_tools():
    llm = get_llm()
    llm_with_tools = llm.bind_tools([movie_search])

    response = llm_with_tools.invoke("Do I have the movie batman")
    assert response.tool_calls[0]['name'] == "movie_search"
    assert response.tool_calls[0]['args']['query'] == "batman"

def test_tool_node():
    llm = get_llm()
    llm_with_tools = llm.bind_tools([movie_search])
    tool_node = get_tool_node()
    response = tool_node.invoke({"messages": [llm_with_tools.invoke("Do I have the movie batman")]})
    
    assert "Here is a json list" in response['messages'][0].content 







