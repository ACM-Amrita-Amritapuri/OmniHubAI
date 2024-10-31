import librosa
import noisereduce as nr
import soundfile as sf

class AudioDenoiser:
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.audio_data = None
        self.sample_rate = None

    def load_audio(self):
        """Load audio file."""
        self.audio_data, self.sample_rate = librosa.load(self.audio_file, sr=None)

    def denoise_audio(self):
        """Denoise the audio using noise reduction."""
        if self.audio_data is None:
            raise ValueError("Audio data not loaded. Call load_audio() first.")
        
        # Perform noise reduction
        self.audio_data = nr.reduce_noise(y=self.audio_data, sr=self.sample_rate)

    def save_audio(self, output_file):
        """Save the denoised audio to a file."""
        if self.audio_data is None:
            raise ValueError("No audio data available to save.")
        
        sf.write(output_file, self.audio_data, self.sample_rate)

