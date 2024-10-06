# OmniHubAI/__init__.py

__version__ = '0.1.0'  # Define the package version

# Import key modules to expose at the package level
from .text import TextModule  # Import your text processing module
from .image import ImageModule  # Import your image processing module
from .audio import AudioModule  # Import your audio processing module
from .video import VideoModule  # Import your video processing module
from .gemini import GeminiClient  # Import the Gemini API client

# Specify the public API
__all__ = [
    'TextModule', 'ImageModule', 'AudioModule', 'VideoModule', 'GeminiClient'
]
