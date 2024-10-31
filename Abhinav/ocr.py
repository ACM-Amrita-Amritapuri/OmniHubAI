import requests

class OCRSpaceAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = 'https://api.ocr.space/parse/image'

    def process_image(self, image_path):
        with open(image_path, 'rb') as f:
            response = requests.post(
                self.endpoint,
                files={'filename': f},
                data={'apikey': self.api_key}
            )
        
        return response.json()

    def extract_text(self, image_path):
        result = self.process_image(image_path)
        if result['IsErroredOnProcessing']:
            print("Error:", result['ErrorMessage'])
            return None
        
        return result['ParsedResults'][0]['ParsedText']


