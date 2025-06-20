import speech_recognition as sr

def capture_voice_to_text():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Please speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized text: {text}")
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

if __name__ == "__main__":
    text = capture_voice_to_text()
    if text:
        print("Final recognized text:", text)
    else:
        print("No text recognized from voice input.")
