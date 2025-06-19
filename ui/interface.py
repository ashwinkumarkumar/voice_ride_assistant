"""
Streamlit interface for the voice ride assistant.
Allows user to interact via voice and see ride recommendations.
"""

import streamlit as st
from app.voice_input import capture_voice_input
from app.nlp_parser import parse_ride_details
from app.fare_simulator import estimate_fares
from app.recommender import recommend_ride
from app.tts_response import speak_text
from app.booking import confirm_booking

def main():
    st.title("Voice Ride Assistant")

    if st.button("Start Voice Ride Request"):
        st.info("Please speak your ride request after the prompt.")
        text = capture_voice_input()
        if not text:
            st.error("Could not capture voice input. Please try again.")
            return
        st.write(f"Captured Text: {text}")

        ride_details = parse_ride_details(text)
        if not ride_details:
            st.error("Could not parse ride details from your input.")
            return
        st.write(f"Parsed Ride Details: {ride_details}")

        fares = estimate_fares(ride_details)
        st.write(f"Estimated Fares: {fares}")

        recommendation = recommend_ride(fares)
        st.write(f"Recommended Ride: {recommendation}")

        response_text = f"Recommended ride is {recommendation['service']} with fare {recommendation['fare']} and time {recommendation['time']} minutes."
        st.success(response_text)
        speak_text(response_text)

        if st.button("Confirm Booking"):
            booking_result = confirm_booking({
                "service": recommendation['service'],
                "fare": recommendation['fare'],
                "time": recommendation['time'],
                "pickup": ride_details.get("pickup"),
                "drop": ride_details.get("drop"),
                "time_requested": ride_details.get("time")
            })
            st.write("Booking Confirmed!")
            st.json(booking_result)
            speak_text("Your ride has been booked. Thank you!")

if __name__ == "__main__":
    main()
