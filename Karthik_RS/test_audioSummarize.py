from AudioSummarize import AudioTextProcessor
if __name__ == "__main__":
    api_key = "your_api_key_here"
    processor = AudioTextProcessor(api_key)
    try:
        output = processor.process_audio_file("path/to/your/audiofile.flac")
        print(output)
    except ValueError as e:
        print(e)
