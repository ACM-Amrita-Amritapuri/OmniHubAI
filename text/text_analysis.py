from assistants.gemini import Gemini

class TextAnalysis :
    def __init__(self):
        API_KEY = "AIzaSyBMkJr0zdkjz5Sd6JGZSbKqga9xLzROKTQ"
        MODEL_ID = "gemini-1.5-flash"
        system_instruction = "You are a helpful assistant to handle big texts and paragraphs."
        self.gemini = Gemini(API_KEY, MODEL_ID, system_instruction)

    def summarize(self, text):
        pass

    def answer_mcq(self, question, options, context):
        """Answers a multiple-choice question based on the provided context using the Gemini API."""
        try:
            prompt = f"Answer the following multiple-choice question: '{question}'\nOptions: {', '.join(options)}\nContext: {context}"
            response = self.gemini.get_gemini_responses_text(prompt)
            if response.candidates:
                return response.candidates[0].content.parts[0].text
            else:
                return "No valid response received."
        except Exception as e:
            return f"An error occurred: {e}"

    
    def answer_question(self, question, context):
        """ Answers a question based on the provided context using the Gemini API. """
        try:
            prompt = f"Question: {question}\nContext: {context}"
            response = self.gemini.get_gemini_responses_text(prompt)
            if response.candidates:
                return response.candidates[0].content.parts[0].text
            else:
                return "No valid response received."
        except Exception as e:
            return f"An error occurred: {e}"
    
    def generate_mcqs(self,):
        pass

    def sentiment_analysis(self):
        pass

    def translate(self):
        # from X lang to english
        pass

    def text_correction(self):
        pass

