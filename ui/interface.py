import streamlit as st
import requests

API_BASE_URL = "http://localhost:5000"

st.set_page_config(page_title="Voice Ride Assistant", page_icon="🚗")

def start_voice_input():
    try:
        response = requests.get(f"{API_BASE_URL}/start")
        if response.status_code == 200:
            return response.json().get("transcript", "")
        else:
            st.error(f"Error starting voice input: {response.json().get('error')}")
            return ""
    except Exception as e:
        st.error(f"Exception: {e}")
        return ""

def process_ride(text):
    try:
        response = requests.post(f"{API_BASE_URL}/process_ride", json={"text": text})
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error processing ride: {response.json().get('error')}")
            return None
    except Exception as e:
        st.error(f"Exception: {e}")
        return None

def confirm_booking(confirmation, ride):
    try:
        response = requests.post(f"{API_BASE_URL}/confirm_booking", json={"confirmation": confirmation, "ride": ride})
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error confirming booking: {response.json().get('error')}")
            return None
    except Exception as e:
        st.error(f"Exception: {e}")
        return None

def main():
    st.title("Voice Ride Assistant")

    st.markdown(
        """
        ### Instructions:
        Please click 'Start Voice Input' and clearly say your ride request including pickup and drop locations.
        For example: "Book a ride from Panjagutta to Ameerpet."
        """
    )

    if st.button("Start Voice Input"):
        transcript = start_voice_input()
        if transcript:
            st.session_state['transcript'] = transcript
            st.success(f"Recognized Text: {transcript}")

    transcript = st.session_state.get('transcript', '')

    if transcript:
        if st.button("Process Ride Request"):
            result = process_ride(transcript)
            if result:
                st.session_state['ride_details'] = result.get('ride_details')
                st.session_state['recommendation'] = result.get('recommendation')
                st.session_state['response_text'] = result.get('response_text')
                st.success(st.session_state['response_text'])

    if 'recommendation' in st.session_state:
        st.write("Recommended Ride Details:")
        st.json(st.session_state['recommendation'])

        if st.button("Confirm Booking"):
            confirm_result = confirm_booking("yes", st.session_state['recommendation'])
            if confirm_result:
                st.success(confirm_result.get('message', 'Booking confirmed'))

        if st.button("Cancel Booking"):
            cancel_result = confirm_booking("no", st.session_state['recommendation'])
            if cancel_result:
                st.info(cancel_result.get('message', 'Booking cancelled'))

if __name__ == "__main__":
    main()
