from text.code import CodeHandling
from text.text_analysis import TextAnalysis

code_handling = CodeHandling()
prompt = "Generate clean, efficient, and well-documented code based on user requirements. Provide detailed explanations, debugging help, and comprehensive documentation when requested."
code = code_handling.generate_code(prompt)
assert code
#print(code)

#Code Documentation
input_code = """
#Function to clean a grid
def clean_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'dirty':
                grid[i][j] = 'clean'
"""
documentation = code_handling.code_documentation(input_code)
print(documentation)


#Testing Answering multiple choice question
text_analysis = TextAnalysis()
mcq_question = "What is the largest planet in our solar system?"
mcq_options = ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"]
mcq_context = "This question tests knowledge about the planets in our solar system."
mcq_answer = text_analysis.answer_mcq(mcq_question, mcq_options, mcq_context)
print("MCQ Answer:", mcq_answer)

# Testing the answer_question method
text_analysis = TextAnalysis()
question = "What is the capital of France?"
context = "France is a country in Europe. It has a rich history and is known for its culture, art, and cuisine. The capital city is famous for its landmarks like the Eiffel Tower and Notre-Dame Cathedral."
answer = text_analysis.answer_question(question, context)
print("Answer:", answer)