import pytest
from app.voice_input import capture_voice_input
from app.nlp_parser import parse_ride_details
from app.fare_simulator import estimate_fares
from app.recommender import recommend_ride
from app.tts_response import speak_text
from app.booking import confirm_booking
from ui.interface import main as ui_main

import os
import time
import threading
import wave
import pyaudio
import pyttsx3

def play_audio_file(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()

def test_full_project_flow():
    print("Please play the audio input from your external device now.")
    # Step 1: Capture voice input from external source (microphone)
    text = capture_voice_input()

    # Since audio is from external source, no audio file cleanup needed

    # You can optionally print or assert expected text here if known
    print(f"Captured text: {text}")

    # Proceed only if text was captured
    assert text is not None and len(text) > 0

    # Step 2: Parse ride details
    ride_details = parse_ride_details(text)
    assert ride_details is not None
    assert "pickup" in ride_details
    assert "drop" in ride_details

    # Step 3: Estimate fares
    fares = estimate_fares(ride_details)
    assert "uber" in fares and "rapido" in fares

    # Step 4: Recommend ride
    recommendation = recommend_ride(fares)
    assert "service" in recommendation

    # Step 5: Text-to-speech feedback (just call, no assertion)
    speak_text("Testing text to speech output.")

    # Step 6: Confirm booking
    booking = confirm_booking({
        "service": recommendation["service"],
        "fare": recommendation.get("fare"),
        "time": recommendation.get("time"),
        "pickup": ride_details.get("pickup"),
        "drop": ride_details.get("drop"),
        "time_requested": ride_details.get("time")
    })
    assert "booking_time" in booking
    assert "ride" in booking

    # Step 7: Run UI main function to check for errors (no assertion)
    try:
        ui_main()
    except Exception as e:
        pytest.fail(f"UI interface failed to run: {e}")

if __name__ == "__main__":
    pytest.main([__file__])
