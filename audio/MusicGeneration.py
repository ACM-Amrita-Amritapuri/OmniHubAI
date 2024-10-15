from assistants.hugging_face import HuggingFaceInference

def MusicGeneration(inputs):
    model = HuggingFaceInference(
        api_token="<API TOKEN>", 
        model_name="facebook/musicgen-small"
    )
    response = model.inference({"inputs": inputs})
    return response