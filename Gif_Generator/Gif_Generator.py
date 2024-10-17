# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16oTlD37JyGBkxW7Kt_P7yBs2lksiVXaZ
"""

import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import imageio
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

#Unsplash API key here
UNSPLASH_ACCESS_KEY = 'BXqVoTEdBCkReLEAlsTxT3BSurSg'

# Text analysis
def analyze_text(text):
    # Tokenizing
    tokens = word_tokenize(text.lower())

    # stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    #common words (keywords)
    word_counts = Counter(filtered_tokens)
    keywords = [word for word, count in word_counts.most_common(5)]  # Top 5 keywords

    return keywords

# Function to fetch images from Unsplash API
def fetch_image_from_unsplash(keyword):
    url = f"https://api.unsplash.com/photos/random?query={keyword}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        image_url = json_data['urls']['regular']

        # Fetch the image from the URL
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))

        return img
    else:
        print(f"Error fetching image for {keyword}: {response.status_code}")
        return None

# creating a GIF from the fetched images
def create_gif_from_images(images, gif_path='output.gif'):
    # Resizing
    image_size = (500, 500)
    frames = [img.resize(image_size) for img in images if img is not None]

    if frames:
        # Saving
        imageio.mimsave(gif_path, frames, duration=0.5)
        print(f"GIF created and saved at {gif_path}")
    else:
        print("No valid images to create a GIF.")

# Main
def generate_gif_from_text(text, gif_path='output.gif'):
    # Analyzing text
    keywords = analyze_text(text)

    images = []
    for keyword in keywords:
        img = fetch_image_from_unsplash(keyword)
        if img:
            images.append(img)

    # Creating
    create_gif_from_images(images, gif_path)

# Example usage
if __name__ == "__main__":
    input_text = ""
    generate_gif_from_text(input_text)
