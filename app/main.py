"""
Flask app routes for the voice ride assistant.
Provides endpoints to start voice input, process ride requests, and confirm bookings.
"""

from flask import Flask, request, jsonify
from app.voice_input import capture_voice_input
from app.nlp_parser import parse_ride_details
from app.fare_simulator import estimate_fares
from app.recommender import recommend_ride
from app.booking import confirm_booking
from app.tts_response import speak_text

app = Flask(__name__)

@app.route('/start', methods=['GET'])
def start():
    """
    Start the voice ride assistant interaction.
    """
    try:
        text = capture_voice_input()
        if not text:
            return jsonify({'error': 'Could not capture voice input'}), 400
        return jsonify({'transcript': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/process_ride', methods=['POST'])
def process_ride():
    """
    Process the ride request from voice input text.
    Extract ride details, estimate fares, recommend ride.
    """
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text in request'}), 400
    text = data['text']
    try:
        ride_details = parse_ride_details(text)
        if not ride_details:
            return jsonify({'error': 'Could not parse ride details'}), 400
        fares = estimate_fares(ride_details)
        recommendation = recommend_ride(fares)
        response_text = f"Recommended ride is {recommendation['service']} with estimated fare {recommendation['fare']} and time {recommendation['time']} minutes."
        speak_text(response_text)
        return jsonify({
            'ride_details': ride_details,
            'fares': fares,
            'recommendation': recommendation,
            'response_text': response_text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/confirm_booking', methods=['POST'])
def confirm():
    """
    Confirm the booking based on user confirmation.
    """
    data = request.get_json()
    if not data or 'confirmation' not in data or 'ride' not in data:
        return jsonify({'error': 'Missing confirmation or ride details'}), 400
    confirmation = data['confirmation']
    ride = data['ride']
    if confirmation.lower() not in ['yes', 'y', 'confirm']:
        return jsonify({'message': 'Booking cancelled by user.'})
    try:
        booking_result = confirm_booking(ride)
        speak_text("Your ride has been booked. Thank you!")
        return jsonify({'message': 'Booking confirmed', 'details': booking_result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
