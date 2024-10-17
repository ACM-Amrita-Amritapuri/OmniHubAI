from gemini import Gemini

class QueryAnswering:

    def __init__(self):

        API_KEY = "AIzaSyDQ5MEv3oUkEzGbNL56VYaXP4YmIPV9qQI"
        MODEL_ID = "gemini-1.5-flash"
        system_instruction = "You are a helpful assistant to handle big texts and paragraphs."
        self.gemini = Gemini(API_KEY, MODEL_ID, system_instruction)

    def get_query_answering(self, text):
        return self.gemini.get_gemini_responses_text(text)


    def code_documentation(self, code):
        system_instruction =  "Summarize the following code in best one sentence, mentioning only its function.  "

        try:
            response = self.gemini.get_gemini_responses_text(code)
            
            # Extracting the content from the response
            if response.candidates:
                documentation_text = response.candidates[0].content.parts[0].text
                return documentation_text
            else:
                return "No valid response received."
        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == "__main__":
    query_answering = QueryAnswering()

    simple_code_snippet = """
# Clean function to set '1' (dirty) to '0' (clean)
def clean(floor, x, y):
    if floor[x][y] == 1:
        floor[x][y] = 0
        print(f"Cleaned position ({x}, {y})")
        print_floor(floor)
# Function to move and clean the floor
def vacuum_cleaner(floor):
    rows = len(floor)
    cols = len(floor[0])

    # Simulate vacuum cleaner movement
    for x in range(rows):
        for y in range(cols):
            clean(floor, x, y)

# Function to print the current state of the floor
def print_floor(floor):
    print("Current floor state:")
    for row in floor:
        print(row)
    print("-" * 20)

# Function to take custom input for the floor
def get_custom_floor():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    floor = []
    for i in range(rows):
        row = []
        for j in range(cols):
            cell = int(input(f"Enter 1 or 0 ({i}, {j}): "))
            row.append(cell)
        floor.append(row)
    
    return floor

# Main program
if __name__ == "__main__":
    # Get custom input from the user
    floor = get_custom_floor()

    # Start the vacuum cleaner
    vacuum_cleaner(floor)

"""
    documentation = query_answering.code_documentation(simple_code_snippet)

    # Print the documentation
    print(documentation)
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
