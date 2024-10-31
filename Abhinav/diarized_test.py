from Abhinav.diarization import SpeakerDiarization

API_KEY = "YOUR-API-KEY"
FILE_URL = "Abhinav/diarization_test.wav"
sd = SpeakerDiarization(API_KEY)
transcript_diarized = sd.SpeakerDiarization(FILE_URL)
