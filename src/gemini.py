import google.generativeai as genai

class Gemini:
    def __init__(self, API_KEY, MODEL_ID="gemini-1.5-flash", system_instruction="You are a helpful assistant."):
        
        genai.configure(api_key=API_KEY)

        self.model = genai.GenerativeModel(
            model_name=MODEL_ID,
            system_instruction=system_instruction,
        )

    def get_gemini_responses_text(self, text):
        try:
            response = self.model.generate_content(text)
            return response
        except Exception as e:
            return f"Error generating response: {e}"

    def get_gemini_responses_pdf(self, pdf_path):
        try:
            with open(pdf_path, 'rb') as f:
                response = self.model.generate_content(f.read())
            return response
        except Exception as e:
            return f"Error generating response: {e}"

    def get_gemini_responses_image(self, image_path):
        try:
            with open(image_path, 'rb') as f:
                response = self.model.generate_content(f.read())
            return response
        except Exception as e:
            return f"Error generating response: {e}"
        

