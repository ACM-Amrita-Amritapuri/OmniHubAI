from assistants.hugging_face import HuggingFaceInference


def ImageCaptioning(image_path):
    model = HuggingFaceInference(
        api_token="<API TOKEN>", model_name="nlpconnect/vit-gpt2-image-captioning"
    )
    inputs = {
        "image": image_path,
        "max_length": 20,
        "num_beams": 4,
    }
    response = model.inference(inputs)
    return response

