from hugging_face_inference import HuggingFaceInference

def image_captioning(filename):
    api_token = "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"
    model_name = "nlpconnect/vit-gpt2-image-captioning"
    
    inference_client = HuggingFaceInference(api_token, model_name)

    # Read the image file
    with open(filename, "rb") as f:
        image_data = f.read()

    # Prepare inputs according to the model's expected format
    inputs = {"inputs": image_data}

    # Call the inference method and return the result
    output = inference_client.inference(inputs)
    return output

# Example usage
output = image_captioning(r"d:/work space/Club october/cat.jpeg")
print(output)
