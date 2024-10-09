import requests

class HuggingFaceInference:
    def __init__(self, api_token, model_name):
        self.api_token = api_token
        self.model_name = model_name
        self.base_url = "https://api-inference.huggingface.co/models/"

    def inference(self, inputs):
        headers = {"Authorization": f"Bearer {self.api_token}"}
        url = f"{self.base_url}{self.model_name}"

        response = requests.post(url, headers=headers, json=inputs)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Inference failed with status code {response.status_code}: {response.text}")
