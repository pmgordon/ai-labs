from labs.tools.movie_search import movie_search


def test_movie_search():
    """Test for movie search"""

    results = movie_search.invoke(input="batman")
    pass