"""
Mock fare and time estimator logic for Uber and Rapido rides.
"""

import random

def estimate_fares(ride_details):
    """
    Estimate fare and time for Uber and Rapido based on ride details.
    Args:
        ride_details (dict): Dictionary with keys pickup, drop, time, ride_type.
    Returns:
        dict: Estimated fares and times for Uber and Rapido.
    """
    # Mock base fares and time estimates
    base_fare_uber = random.uniform(5, 10)
    base_fare_rapido = random.uniform(3, 8)
    base_time_uber = random.randint(10, 30)
    base_time_rapido = random.randint(8, 25)

    # Adjust fare based on ride_type preference if specified
    if ride_details.get("ride_type") == "uber":
        base_fare_uber *= 0.9  # discount for preferred Uber
    elif ride_details.get("ride_type") == "rapido":
        base_fare_rapido *= 0.9  # discount for preferred Rapido

    # Return mock estimates
    return {
        "uber": {
            "fare": round(base_fare_uber, 2),
            "time": base_time_uber
        },
        "rapido": {
            "fare": round(base_fare_rapido, 2),
            "time": base_time_rapido
        }
    }
