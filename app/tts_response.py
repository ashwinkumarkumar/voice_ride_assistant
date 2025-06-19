"""
Text-to-speech feedback module using pyttsx3.
"""

import pyttsx3

engine = pyttsx3.init()

def speak_text(text):
    """
    Convert text to speech and play it.
    Args:
        text (str): Text to be spoken.
    """
    engine.say(text)
    engine.runAndWait()
