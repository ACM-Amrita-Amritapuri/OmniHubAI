from text import QueryAnswering

def test_query_answering():
    qa = QueryAnswering()
    response = qa.get_query_answering("What is the capital of France?")
    print(response)  # Just print the response for manual verification

if __name__ == "__main__":
    test_query_answering()
