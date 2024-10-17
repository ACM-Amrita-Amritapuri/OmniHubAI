from assistants.hugging_face import HuggingFaceInference
from speech2text.AudioToText import AudioToText
import requests

def AudioSummarize():
    pass



def SpeechRecognition(audio_path: str):
    # Replace `<API_TOKEN>` with your actual Hugging Face API token
    api_token = "<API_TOKEN>"
    
    # Create an instance of the AudioToText class
    audio_to_text = AudioToText(token=api_token)
    
    # Call the SpeechRecognition method and pass the audio file path
    response = audio_to_text.SpeechRecognition(audio_path)
    
    # Process the response
    if "error" in response:
        print(f"Error: {response['error']}")
        if "message" in response:
            print(f"Message: {response['message']}")
    else:
        print("Transcription Result:", response)

def LanguageRecognition(audio_path):
    model = HuggingFaceInference(
        api_token="<API TOKEN>",
        model_name="speechbrain/lang-id-voxlingua107-ecapa"
    )
    inputs = {
        "audio": audio_path
    }


def GenderRecognition():
    pass


def EmotionRecognition():
    pass


def MusicGenreClassification():
    pass


def SpeakerDiarization():
    pass





