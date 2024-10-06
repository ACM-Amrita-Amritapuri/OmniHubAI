# OmniHubAI

Welcome to **OmniHubAI** – Your Ultimate AI Library!

## Overview

**OmniHubAI** is a comprehensive library designed for various AI-related tasks, including text processing, image manipulation, audio processing, video tasks, and interactions with the Gemini API. It aims to provide an easy-to-use interface for developers and researchers alike.

## Table of Contents

- Features
- Installation
- Usage
  - Using the Chatbot Module
- Directory Structure
- Contributing
- License

## Features

- **Text Module**: Includes functionalities for query answering, chatbots, and code generation.
- **Image Module**: Tasks related to images, such as captioning and manipulation.
- **Audio Module**: Handles audio tasks like transcription and speech generation.
- **Video Module**: Processes video-related tasks and generation.
- **Gemini Module**: Provides functionalities for interacting with the Gemini API.

## Installation

To install the library, clone the repository and install the required dependencies:

```bash
git clone https://github.com/ACM-Amrita-Amritapuri/OmniHubAI.git
cd OmniHubAI
pip install -r requirements.txt
```

## Usage

### Using the Chatbot Module

To use the `Chatbot` class and its `respond` function from the `text` module, follow these steps:

1. **Import the necessary class**:

   ```python
   from OmniHubAI import TextModule
   ```

2. **Create an instance of the `Chatbot` class**:

   ```python
   chatbot = TextModule.Chatbot()
   ```

3. **Call the `respond` method**:

   ```python
   user_input = "Hello, how are you?"
   response = chatbot.respond(user_input)
   ```

4. **Print the response**:
   ```python
   print(response)
   ```

Here’s the complete example code:

```python
from OmniHubAI import TextModule

# Create an instance of the Chatbot class
chatbot = TextModule.Chatbot()

# Get a response from the chatbot
user_input = "Hello, how are you?"
response = chatbot.respond(user_input)

# Print the response
print(response)
```

### Running the Script

To run the script:

1. Save the script in a `.py` file, for example, `chatbot_example.py`.
2. Run the script from your terminal or command prompt:
   ```bash
   python chatbot_example.py
   ```

### Expected Output

The expected output for the example provided will be something like:

```
Chatbot response to: Hello, how are you?
```

## Directory Structure

```
OmniHubAI/
├── .gitignore
├── LICENSE
├── README.md
├── setup.py
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── text/
│   │   ├── __init__.py
│   │   ├── text_processing.py
│   │   ├── chatbot.py
│   │   └── ...
│   ├── image/
│   │   ├── __init__.py
│   │   ├── image_processing.py
│   │   ├── captioning.py
│   │   └── ...
│   ├── audio/
│   │   ├── __init__.py
│   │   ├── audio_processing.py
│   │   ├── transcription.py
│   │   └── ...
│   ├── video/
│   │   ├── __init__.py
│   │   ├── video_processing.py
│   │   ├── video_editing.py
│   │   └── ...
│   └── gemini/
│       ├── __init__.py
│       ├── gemini_client.py
│       ├── market_data.py
│       └── ...
└── tests/
    ├── __init__.py
    ├── test_text.py
    ├── test_image.py
    ├── test_audio.py
    ├── test_video.py
    └── test_gemini.py
```

## Contributing

We welcome contributions from developers around the globe! To contribute, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button on the top right of this page.
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/ACM-Amrita-Amritapuri/OmniHubAI.git
   ```
3. **Create a Branch**:
   ```bash
   cd OmniHubAI
   git checkout -b my-feature-branch
   ```
4. **Make Your Changes**: Implement your changes and test them.
5. **Check the Changed Files**:
   ```bash
   git status
   ```
6. **Commit Your Changes**:
   ```bash
   git add .
   git commit -m "<EXPLAIN-YOUR-CHANGES>"
   ```
7. **Push to Your Forked Repository**:
   ```bash
   git push origin my-feature-branch
   ```
8. **Create a Pull Request**: Go to your forked repository on GitHub and click the "Compare & pull request" button.

## License

This project is licensed under the MIT License – see the LICENSE file for more details.

---

Thank you for checking out **OmniHubAI**! We hope this library is useful for your AI projects.
