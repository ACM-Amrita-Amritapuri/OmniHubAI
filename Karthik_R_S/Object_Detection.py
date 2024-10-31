import requests

class ObjectDetector:
    API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"

    def __init__(self, token):
        self.headers = {"Authorization": f"Bearer {token}"}

    def query(self, filename):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(self.API_URL, headers=self.headers, data=data)
        return response.json()

