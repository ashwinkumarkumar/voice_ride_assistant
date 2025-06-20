import os
import json
import pytest
from app.nlp_parser import parse_ride_details
from app.fare_simulator import estimate_fares
from app.recommender import recommend_ride
from app.tts_response import speak_text
from app.booking import confirm_booking

def test_full_ride_flow(tmp_path):
    # Sample input text simulating voice input
    sample_text = "I want to go from MG Road to Koramangala at 5 PM by Uber"

    # Parse ride details
    ride_details = parse_ride_details(sample_text)
    assert ride_details is not None
    assert "pickup" in ride_details
    assert "drop" in ride_details

    # Estimate fares
    fares = estimate_fares(ride_details)
    assert "uber" in fares and "rapido" in fares

    # Recommend ride
    recommendation = recommend_ride(fares)
    assert "service" in recommendation

    # Test TTS (just call function, no assertion)
    speak_text("Testing text to speech output.")

    # Confirm booking
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

    # Check booking log file contains the booking
    log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "booking_log.txt")
    assert os.path.exists(log_file)
    with open(log_file, "r") as f:
        lines = f.readlines()
        # Filter out lines that are not valid JSON (e.g., empty or comment lines)
        valid_lines = []
        for line in lines:
            line = line.strip()
            if line.startswith("{") and line.endswith("}"):
                valid_lines.append(line)
        assert any(json.loads(line)["booking_time"] == booking["booking_time"] for line in valid_lines)

if __name__ == "__main__":
    pytest.main([__file__])
