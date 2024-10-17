from text.code import CodeHandling
from text.text_analysis import TextAnalysis

# code_handling = CodeHandling()

prompt = "Generate clean, efficient, and well-documented code based on user requirements. Provide detailed explanations, debugging help, and comprehensive documentation when requested."

#code = code_handling.generate_code(prompt)

#assert code

#print(code)

text_analysis = TextAnalysis()
#testing text correction
incorrect_text = "She dont know where the meeting are being held."
corrected_text = text_analysis.text_correction(incorrect_text)
print("Corrected Text:", corrected_text)

# testing sentiment analysis
text = "The presentation didn't go as planned, and I feel frustrated."
sentiment = text_analysis.sentiment_analysis(text)
print(sentiment)

# testing text translation
text_to_translate = "Bonjour, comment ça va?"
translated_text = text_analysis.translate(text_to_translate)
print(translated_text)

# testing text summarization
long_text = """
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. 
Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. 
Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving". 
As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.
"""
summary = text_analysis.summarize(long_text)
print("Summary:", summary)



=======
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

