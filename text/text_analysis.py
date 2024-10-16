from assistants.gemini import Gemini

class TextAnalysis :
    def __init__(self):
        API_KEY = "your_api_key"
        MODEL_ID = "gemini-1.5-flash"
        system_instruction = "You are a helpful assistant to handle big texts and paragraphs."
        self.gemini = Gemini(API_KEY, MODEL_ID, system_instruction)

    def summarize(self, text):
        instruction = "Please provide a concise summary of the following text in best 3 sentences."
        prompt = f"{instruction}\n\nText to summarize:\n{text}"

        response = self.gemini.get_gemini_responses_text(prompt)

        if response._result and response._result.candidates:
            parts = response._result.candidates[0].content.parts
            return parts[0].text if parts else "No summary found"
        else:
            return "No valid summary found in the response."

    def answer_mcq(self,):
        pass

    def answer_question(self,):
        pass
    
    def generate_mcqs(self,):
        pass

    def sentiment_analysis(self,text):
        instruction = "Please analyze the sentiment of this text and classify it as Positive, Negative, or Neutral."
        prompt = f"{instruction}\n\nText to analyze:\n{text}"
        
        response = self.gemini.get_gemini_responses_text(prompt)
        
        if response._result and response._result.candidates:    
            content = response._result.candidates[0].content.parts
            return content[0].text if content else "No sentiment analysis found"
        else:
            return "No valid sentiment analysis found in the response."


    def translate(self,text):        
        instruction = "Please translate the following text to English."
        prompt = f"{instruction}\n\nText to translate:\n{text}"

        response = self.gemini.get_gemini_responses_text(prompt)

        if response._result and response._result.candidates:
            parts = response._result.candidates[0].content.parts
            return parts[0].text if parts else "No translation found"
        else:
            return "No valid translation found in the response."

    def text_correction(self,text):        
        instruction = "Please correct the spelling and grammar in this text."
        prompt = f"{instruction}\n\nText to correct:\n{text}"
        
        response = self.gemini.get_gemini_responses_text(prompt)    
   
        if response._result and response._result.candidates:
            parts = response._result.candidates[0].content.parts
            return parts[0].text if parts else "No content found"
        else:
            return "No valid content found in the response."

    
    

