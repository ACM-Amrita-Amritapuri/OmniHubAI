from Abhinav.audioDenoise import AudioDenoiser


input_audio = 'path/to/your/input_audio.wav'
output_audio = 'path/to/your/output_audio.wav'
denoiser = AudioDenoiser(input_audio)

denoiser.load_audio()
denoiser.denoise_audio()
denoiser.save_audio(output_audio)
print("Denoising complete. Output saved to:", output_audio)

