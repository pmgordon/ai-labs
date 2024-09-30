from langgraph.prebuilt import ToolNode

from labs.tools.movie_search import movie_search

def get_tool_node():
    node = ToolNode([movie_search])
    return node