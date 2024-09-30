from labs.retrievers.opensearch import get_opensearch_reteriver

def retrieve(state):
    """
    Retrieve documents from vectorstore

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, documents, that contains retrieved documents
    """
    print("---RETRIEVE---")
    question = state["question"]

    # Write retrieved documents to documents key in state
    retriever = get_opensearch_reteriver()
    documents = retriever.similarity_search(question)
    return {"documents": documents}