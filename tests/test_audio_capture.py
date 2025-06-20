import speech_recognition as sr
import time

def test_audio_capture_from_played_audio():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Please play the audio now for testing audio capture...")
    time.sleep(3)  # Give user time to start playing audio

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10)

    try:
        text = recognizer.recognize_google(audio)
        print(f"Captured text: {text}")
        assert text is not None and len(text) > 0
    except sr.UnknownValueError:
        assert False, "Could not understand audio"
    except sr.RequestError as e:
        assert False, f"Could not request results; {e}"

if __name__ == "__main__":
    import pytest
