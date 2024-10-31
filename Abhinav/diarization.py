import assemblyai as aai

class SpeakerDiarization:
    def __init__(self, api_key):
        aai.settings.api_key = api_key
        self.transcriber = aai.Transcriber()

    def transcribe(self, file_url, speaker_labels=True):
        try:
            config = aai.TranscriptionConfig(speaker_labels=speaker_labels)
            transcript = self.transcriber.transcribe(file_url, config=config)

            if not transcript.utterances:
                print("No utterances found in the transcript.")
                return

            for utterance in transcript.utterances:
                print(f"Speaker {utterance.speaker}: {utterance.text}")
        
        except aai.errors.AssemblyAIError as e:
            print(f"An error occurred while transcribing: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


