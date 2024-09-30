"""Search For Movies"""
import json
from typing import Annotated, List
from langchain_core.documents.base import Document
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage

from labs.retrievers.opensearch import get_opensearch_reteriver
from labs.utils.utils import get_json_llm


def _grader(documents: List[Document], movie:str) -> List[Document]:
    # Grader Instructions
    doc_grader_instructions = """You are a grader assessing relevance of a retrieved document to a movie a user requested.

        If the document relates to the movie requested by match or semantic meaning, grade it as relevant.
        """

    # Grader prompt
    doc_grader_prompt = """Here is the retrieved document: \n\n {document} \n\n Here is the movie requested: \n\n {movie}. 

    This carefully and objectively assess whether the document contains at least some information that is relevant to the movie.

    Return JSON with single key, binary_score, that is 'yes' or 'no' score to indicate whether the document contains at least some information that is relevant to the question."""

    
    llm_json_mode = get_json_llm()

    print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
    
    # Score each doc
    filtered_docs = []

    for d in documents:
        doc_grader_prompt_formatted = doc_grader_prompt.format(document=d.page_content, movie=movie)
        result = llm_json_mode.invoke([SystemMessage(content=doc_grader_instructions)] + [HumanMessage(content=doc_grader_prompt_formatted)])
        grade = json.loads(result.content)['binary_score']
        # Document relevant
        if grade.lower() == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            filtered_docs.append(d)
    return filtered_docs

@tool
def movie_search(query: Annotated[str, "a single movie title"]) -> str:
    """Search the movies in your collection. Movies must be searched one at a time as a string, not as a list or array"""
    vector_store = get_opensearch_reteriver()
    docs = vector_store.similarity_search(query, k=10)

    filtered_list = _grader(docs, query)

    if not filtered_list:
        return f"You do not have the movie: {query}"

    movies_list = []
    for doc in filtered_list:
        movies_list.append({ "title" : doc.page_content, "format": doc.metadata['format']})
    
    movies = json.dumps(movies_list)
    observation = f"Here is a json list of movies and formats in the collection: \n {movies}"
    return observation