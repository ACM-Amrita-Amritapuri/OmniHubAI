import requests

class EmotionRecognition:
    def __init__(self, token: str ,api_url: str ="https://api-inference.huggingface.co/models/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition") -> None:
        self.api_url = api_url
        self.token = token

    def EmotionRecognition(self, filename):
        try:
            with open(filename, "rb") as audio_file:
                data = audio_file.read()
            response = requests.post(self.api_url, headers=self.headers, data=data)
            return response.json()
        except FileNotFoundError:
            return {"error": "File not found", "filename": filename}
        
        except requests.exceptions.RequestException as e:
            return {"error": "Request failed", "message": str(e)}