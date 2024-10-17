from gemini import Gemini

class QueryAnswering:

    def __init__(self):
        API_KEY = "AIzaSyDQ5MEv3oUkEzGbNL56VYaXP4YmIPV9qQI"
        MODEL_ID = "gemini-1.5-flash"
        system_instruction = "You are a helpful assistant to handle big texts and paragraphs."
        self.gemini = Gemini(API_KEY, MODEL_ID, system_instruction)

    def get_query_answering(self, text):
        return self.gemini.get_gemini_responses_text(text)

    def code_debugging(self, code):
        system_instruction = (
            "Please help me to debug this code. Display the error message and give the best corrected code."
        )        
        response = self.gemini.get_gemini_responses_text(code)        
        if response._done and response._result.candidates:
            debug_info = response._result.candidates[0].content.parts[0].text
            return debug_info
        else:
            return "No valid response received."
    
    def data_structuring(self, input_text):
        """Structure data based on the input text."""
        prompt = f"Structure the following text into key-value pairs: {input_text}"

        response = self.gemini.get_gemini_responses_text(prompt)

        if response._done and response._result.candidates:
            structured_data = response._result.candidates[0].content.parts[0].text
            return structured_data
        else:
            return "No valid response received."

# Example Usage
if __name__ == "__main__":
    qa = QueryAnswering()
    
    # Example for query answering
    text_query = "What are the benefits of using the Gemini API?"
    answer = qa.get_query_answering(text_query)
    print("Query Answer:", answer)

    # Example for debugging code
    code_to_debug = "print('Hello World"  # Intentional syntax error
    debug_info = qa.code_debugging(code_to_debug)
    print("Debugging Info:", debug_info)

    # Example for data structuring
    data_to_structure = "hi hello name:madhu"
    structured_result = qa.data_structuring(data_to_structure)
    print("Structured Data:", structured_result)
