from .gemini import Gemini


class QueryAnswering:

    def __init__(self):
        API_KEY = "place_holder for API_KEY"
        MODEL_ID = "place_holder for Model_ID"
        system_instruction = "You are a helpful assistant hanf big texts and paragraphs."
        self.gemini = Gemini(API_KEY, MODEL_ID, system_instruction)
    
    def get_query_answering(self, text):
        return self.gemini.get_gemini_responses_text(text)
    





# CodeGen class

class CodeGeneration:
    def __init__(self):
        API_KEY = "api-key-placeholder-to-avoid-checks"
        MODEL_ID = "gemini-1.5-flash"
        system_instruction = """You are an expert programmer assistant. 
        Generate clean, efficient, and well-documented code based on user requirements.
        Provide detailed explanations, debugging help, and comprehensive documentation when requested."""
        self.gemini = Gemini(API_KEY, MODEL_ID, system_instruction)
    
    def generate_code(self, prompt):
        return self.gemini.get_gemini_responses_text(prompt)
    
    def improve_code(self, existing_code, instructions):
        prompt = f"Original code:\n{existing_code}\n\nImprovement instructions:\n{instructions}"
        return self.gemini.get_gemini_responses_text(prompt)
    
    def explain_code(self, code):
        prompt = f"Please explain the following code in detail:\n{code}"
        return self.gemini.get_gemini_responses_text(prompt)
    
    def debug_code(self, code, error_message=None, expected_behavior=None):
        prompt = f"Please help debug this code:\n{code}\n"
        if error_message:
            prompt += f"Error message received:\n{error_message}\n"
        if expected_behavior:
            prompt += f"Expected behavior:\n{expected_behavior}\n"
        return self.gemini.get_gemini_responses_text(prompt)
    
    def add_docstrings(self, code):
        prompt = f"Add comprehensive docstrings to the following code:\n{code}"
        return self.gemini.get_gemini_responses_text(prompt)
    
    def generate_markdown_documentation(self, code, project_name=None):
        prompt = f"""Generate comprehensive markdown documentation for this code:
        {code}
        
        Include:
        1. Overview
        2. Installation instructions
        3. Usage examples
        4. API documentation for each function/class
        5. Any dependencies
        6. Contributing guidelines
        """
        if project_name:
            prompt = f"Project Name: {project_name}\n\n" + prompt
        return self.gemini.get_gemini_responses_text(prompt)
    
    def optimize_code(self, code, optimization_goal):
        prompt = f"""Optimize this code for {optimization_goal}:
        {code}
        
        Explain the optimizations made.
        """
        return self.gemini.get_gemini_responses_text(prompt)
    
    def generate_test_cases(self, code):
        prompt = f"""Generate comprehensive test cases for this code:
        {code}
        
        Include:
        1. Unit tests
        2. Edge cases
        3. Integration tests if applicable
        4. Test explanations
        """
        return self.gemini.get_gemini_responses_text(prompt)
    
    def convert_code_to_language(self, code, source_language, target_language):
        prompt = f"""Convert this {source_language} code to {target_language}:
        {code}
        
        Explain any significant differences or special considerations.
        """
        return self.gemini.get_gemini_responses_text(prompt)
