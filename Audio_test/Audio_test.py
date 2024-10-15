from audio.recogniton import LanguageRecognition

audio_file = "Audio.flac"

result = LanguageRecognition(audio_file)  


assert result is not None, "Audio processing failed!"


print(result)
