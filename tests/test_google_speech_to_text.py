import os
import io
import pytest
import time
from google.cloud import speech
import pyaudio
import wave

def record_audio_to_file(filename, record_seconds=5, sample_rate=16000, channels=1):
    chunk = 1024
    format = pyaudio.paInt16
    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk)

    print(f"Recording audio for {record_seconds} seconds...")
    frames = []

    for _ in range(0, int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe_audio_file(speech_file):
    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    transcripts = []
    for result in response.results:
        transcripts.append(result.alternatives[0].transcript)
    return " ".join(transcripts)

def test_google_speech_to_text_live_mic():
    audio_filename = "tests/live_mic_audio.wav"
    record_audio_to_file(audio_filename, record_seconds=5)
    transcript = transcribe_audio_file(audio_filename)
    print(f"Transcript: {transcript}")
    assert transcript is not None and len(transcript) > 0

if __name__ == "__main__":
    pytest.main([__file__])
