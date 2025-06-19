"""
Booking simulation and final confirmation module.
Logs booking details to a file.
"""

import json
import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'booking_log.txt')

def confirm_booking(ride):
    """
    Simulate booking confirmation and log the booking.
    Args:
        ride (dict): Ride details including service, fare, time, pickup, drop.
    Returns:
        dict: Confirmation details including booking time.
    """
    booking_time = datetime.datetime.now().isoformat()
    booking_record = {
        "booking_time": booking_time,
        "ride": ride
    }
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, 'a') as f:
            f.write(json.dumps(booking_record) + "\n")
        return booking_record
    except Exception as e:
        raise RuntimeError(f"Failed to log booking: {e}")
