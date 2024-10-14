from assistants.gemini import Gemini

class TextAnalysis :
    def __init__(self):
        API_KEY = "AIzaSyDQ5MEv3oUkEzGbNL56VYaXP4YmIPV9qQI"
        MODEL_ID = "gemini-1.5-flash"
        system_instruction = "You are a helpful assistant to handle big texts and paragraphs."
        self.gemini = Gemini(API_KEY, MODEL_ID, system_instruction)

    def summarize(self, text):
        pass

    def answer_mcq(self,):
        pass

    def answer_question(self,):
        pass
    
    def generate_mcqs(self,):
        pass

    def sentiment_analysis(self):
        pass

    def translate(self):
        # from X lang to english
        pass

    def text_correction(self,text):
        pass

