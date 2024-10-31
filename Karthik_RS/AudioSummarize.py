import requests

class AudioTextProcessor:
    def __init__(self, api_key):
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.audio_model_url = "https://api-inference.huggingface.co/models/openai/whisper-large-v3-turbo"
        self.summarizer_model_url = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"

    def audio_to_text(self, filename):
        """Converts audio file to text using Hugging Face's API."""
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(self.audio_model_url, headers=self.headers, data=data)
        response_data = response.json()
        if "text" in response_data:
            return response_data["text"]
        else:
            raise ValueError(f"Error in transcription: {response_data}")

    def summarize_text(self, text):
        """Summarizes text using Hugging Face's API."""
        payload = {"inputs": text}
        response = requests.post(self.summarizer_model_url, headers=self.headers, json=payload)
        return response.json()

    def process_audio_file(self, filename):
        """Processes an audio file to return a summarized version of its transcribed text."""
        transcription_text = self.audio_to_text(filename)
        summary = self.summarize_text(transcription_text)
        return summary
