# testing/text_test.py

from src.text.text import QueryAnswering

def test_query_answering():
    qa = QueryAnswering()
    response = qa.get_query_answering("What is the capital of France?")
    print(response)

if __name__ == "__main__":
    test_query_answering()
