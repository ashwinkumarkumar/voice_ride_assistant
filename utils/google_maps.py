"""
Helper functions for location APIs (mocked).
"""

def validate_location(location):
    """
    Mock validation of a location string.
    Args:
        location (str): Location name or address.
    Returns:
        bool: True if location is valid, False otherwise.
    """
    if not location or not isinstance(location, str):
        return False
    # Simple mock: location must be at least 3 characters
    return len(location.strip()) >= 3

def format_location(location):
    """
    Mock formatting of location string.
    Args:
        location (str): Raw location input.
    Returns:
        str: Formatted location string.
    """
    if not location:
        return ""
    return location.strip().title()
