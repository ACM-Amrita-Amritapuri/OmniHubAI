import requests

class GenderRecognition:
    def __init__(self, api_url, token):
        self.api_url = api_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def query(self, filename): 
        with open(filename, "rb") as f: 
            data = f.read() 
        response = requests.post(self.api_url, headers=self.headers, data=data) 
        return response.json()