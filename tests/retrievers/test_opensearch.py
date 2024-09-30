from labs.retrievers.opensearch import get_opensearch_reteriver


def test_opensearch_similary_search():
    retriever = get_opensearch_reteriver()
    documents = retriever.similarity_search("Batman", k=5)
    for doc in documents:
        print(doc.page_content)
    assert len(documents) == 5

def test_opensearch_similary_search_with_score():
    retriever = get_opensearch_reteriver()
    documents = retriever.similarity_search_with_score("LOTR", k=5)
    for doc in documents:
        print(f"Title: {doc[0].page_content}, Score: {doc[1]}")

    assert len(documents) == 5