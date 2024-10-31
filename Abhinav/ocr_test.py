from Abhinav.ocr import OCRSpaceAPI
if __name__ == "__main__":
    api_key = 'YOUR-API-KEY'
    image_path = 'Abhinav/ocr_test_image.png'

    ocr = OCRSpaceAPI(api_key)
    text = ocr.extract_text(image_path)

    if text:
        print(text)