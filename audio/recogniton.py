from assistants.hugging_face import HuggingFaceInference

def AudioSummarize():
    pass


def SpeechRecognition():
    # speech to text
    pass


def LanguageRecognition(audio_path):
    model = HuggingFaceInference(
        api_token="<API TOKEN>", 
        model_name="speechbrain/lang-id-voxlingua107-ecapa"
    )
    inputs = {
        "audio": audio_path  
    }
    response = model.inference(inputs)
    return response 


def GenderRecognition():
    pass


def EmotionRecognition():
    pass


def MusicGenreClassification():
    pass


def SpeakerDiarization():
    pass





