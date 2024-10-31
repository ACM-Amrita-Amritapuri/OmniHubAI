from GenderRecognition import GenderRecognition

token = "API TOKEN"
recognizer = GenderRecognition("https://api-inference.huggingface.co/models/alefiury/wav2vec2-large-xlsr-53-gender-recognition-librispeech", token)

output = recognizer.query(r"C:\Users\LENOVO\Desktop\Omni_HUB\OmniHubAI\Karthik_RS\Test_audio.flac")
print(output)

