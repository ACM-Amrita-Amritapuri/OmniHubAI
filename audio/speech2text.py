import requests


class AudioToText:
    def __init__(self, token: str ,api_url: str ="https://api-inference.huggingface.co/models/openai/whisper-large-v3") -> None:
        self.api_url = api_url
        self.token = token

    def SpeechRecognition(self, filename: str) -> dict:
        """Extract audio file information using Automatic Speech Recognition API"""
        
        try:
            with open(filename, "rb") as audio_file:
                response = requests.post(self.api_url, data=audio_file)
            
            # Raise an exception if the response was not successful
            response.raise_for_status()
            return response.json()
        
        except FileNotFoundError:
            return {"error": "File not found", "filename": filename}
        
        except requests.exceptions.RequestException as e:
            return {"error": "Request failed", "message": str(e)}
    

