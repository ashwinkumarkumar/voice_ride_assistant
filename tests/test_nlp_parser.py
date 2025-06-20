import pytest
from app.nlp_parser import parse_ride_details

def test_parse_ride_details_basic():
    text = "I want to go from MG Road to Koramangala at 5 PM by Uber"
    details = parse_ride_details(text)
    assert details is not None
    assert "pickup" in details
    assert "drop" in details
    assert "time" in details
    assert "ride_type" in details

def test_parse_ride_details_edge_cases():
    text = "Book a ride to the airport"
    details = parse_ride_details(text)
    assert details is not None
    # pickup may be missing or default
    assert "drop" in details

if __name__ == "__main__":
    pytest.main([__file__])
