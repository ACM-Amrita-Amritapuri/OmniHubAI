from text.code import CodeHandling


code_handling = CodeHandling()

prompt = "Generate clean, efficient, and well-documented code based on user requirements. Provide detailed explanations, debugging help, and comprehensive documentation when requested."

code = code_handling.generate_code(prompt)

assert code

print(code)


