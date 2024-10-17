
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
    
    def generate_mcqs(self, input_topic, num_questions=5):
        """Generate multiple-choice questions based on the given topic."""
        prompt = (
        "Please generate multiple-choice questions (MCQs) for the following topic. "
        f"Each question should include one correct answer and three distractors. "
        f"Generate {num_questions} questions.\n\n"
        f"{input_topic}\n\n"
        "Output format should be:\n"
        "Question 1: [Question text] \n"
        "A. [Option A] \n"
        "B. [Option B] \n"
        "C. [Option C] \n"
        "D. [Option D] \n\n"
        )

        
        for i in range(2, num_questions + 1):
            prompt += f"Question {i}: [Question text] \n" \
                f"A. [Option A] \n" \
                f"B. [Option B] \n" \
                f"C. [Option C] \n" \
                f"D. [Option D] \n\n"
     
    
    
        response = self.gemini.get_gemini_responses_text(prompt)


        if response and response._done and hasattr(response._result, 'candidates'):
            candidates = response._result.candidates
            if candidates and hasattr(candidates[0], 'content') and hasattr(candidates[0].content.parts[0], 'text'):
                mcq_data = candidates[0].content.parts[0].text
                return mcq_data
            else:
                return "No valid content found in response."
        else:
            return "No valid response received."


   
         
    
    def sentiment_analysis(self):
        pass
        


    def translate(self):
        # from X lang to english
        pass

    def text_correction(self):
        pass

    def data_structuring(self, input_text):
        """Structure data based on the input text into key-value pairs, adding spaces if needed."""
        prompt = (
        "Please analyze the following text and attempt to structure it into key-value pairs. "
        "If there are any concatenated words without spaces, add spaces between them. "
        "If the text cannot be converted into key-value pairs, return the corrected text with spaces added:\n\n"
        f"{input_text}\n\n"
        "Output should be in key-value pair format or the modified text if conversion is not possible."
    )
    
   
        response = self.gemini.get_gemini_responses_text(prompt)
        if response._done and response._result.candidates:
            structured_data = response._result.candidates[0].content.parts[0].text
            return structured_data
        else:
            return "No valid response received."
        
        
    
        
    

   
   
    
        

        
    
    

