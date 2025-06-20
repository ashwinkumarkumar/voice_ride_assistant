import pytest
from app.voice_input import capture_voice_input

def test_capture_voice_input(monkeypatch):
    # Mock the capture_voice_input function to return a fixed string
    def mock_capture():
        return "I want to go from MG Road to Koramangala at 5 PM by Uber"
    monkeypatch.setattr("app.voice_input.capture_voice_input", mock_capture)

    result = capture_voice_input()
    assert result == "I want to go from MG Road to Koramangala at 5 PM by Uber"

if __name__ == "__main__":
    pytest.main([__file__])
