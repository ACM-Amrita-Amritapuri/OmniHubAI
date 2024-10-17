from text.code import CodeHandling
from text.text_analysis import TextAnalysis


code_handling = CodeHandling()

prompt = "Generate clean, efficient, and well-documented code based on user requirements. Provide detailed explanations, debugging help, and comprehensive documentation when requested."

code = code_handling.generate_code(prompt)

assert code

print(code)
#data structuring
print("structuring data:")
text_analysis = TextAnalysis()

input_text = "meghanasnigdhamadhuri"

structured_result = text_analysis.data_structuring(input_text)

print(structured_result)

#generte mcq's
print("Genertaing mcq's:")
input_text = "Photosynthesis"
number_of_mcqs = 5

mcq = text_analysis.generate_mcqs(input_text,number_of_mcqs)

print(mcq)

#sentiment analysis
