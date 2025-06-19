"""
Module to capture and convert voice input to text using SpeechRecognition.
"""

import speech_recognition as sr

def capture_voice_input(timeout=5, phrase_time_limit=10):
    """
    Capture voice input from the microphone and convert to text.
    Args:
        timeout (int): Maximum seconds to wait for phrase to start.
        phrase_time_limit (int): Maximum seconds for phrase length.
    Returns:
        str: Transcribed text from voice input or None if failed.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak your ride request...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = recognizer.recognize_google(audio)
            print(f"Captured text: {text}")
            return text
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    return None
