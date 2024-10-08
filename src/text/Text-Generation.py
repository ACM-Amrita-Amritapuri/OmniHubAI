import google.generativeai as genai
class Code:
    def __init__(self) -> None:
        genai.configure(api_key="<your-api-key>")  
 
    def get_gemini_response(self,question):
       generative_config={"temperature":0.9,"top_p":1,"top_k":1}
       model = genai.GenerativeModel("gemini-pro",generation_config=generative_config)
       response = model.generate_content("Explain what is "+question+" In 100 words")
       return response.text

bot=Code()
print(bot.get_gemini_response("Village"))