"""
Common helper functions used across the project.
"""

def validate_ride_type(ride_type):
    """
    Validate the ride type string.
    Args:
        ride_type (str): Ride type input.
    Returns:
        bool: True if valid ride type, False otherwise.
    """
    valid_types = {"uber", "rapido", "cab", "auto", "bike", "car"}
    return ride_type.lower() in valid_types if ride_type else False

def format_ride_type(ride_type):
    """
    Format the ride type string to standard form.
    Args:
        ride_type (str): Raw ride type input.
    Returns:
        str: Formatted ride type or None if invalid.
    """
    if not ride_type:
        return None
    ride_type = ride_type.lower()
    if validate_ride_type(ride_type):
        return ride_type.capitalize()
    return None
