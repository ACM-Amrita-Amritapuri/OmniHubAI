from .gemini import Gemini


class QueryAnswering:

    def __init__(self):
        API_KEY = "<API KEY>"
        MODEL_ID = "gemini-1.5-flash"
        system_instruction = "You are a helpful assistant hanf big texts and paragraphs."
        self.gemini = Gemini(API_KEY, MODEL_ID, system_instruction)
    
    def get_query_answering(self, text):
        return self.gemini.get_gemini_responses_text(text)
    
