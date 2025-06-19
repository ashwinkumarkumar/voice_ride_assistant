"""
Module to extract ride details from text using spaCy.
"""

import spacy
import re

# Load the small English model
nlp = spacy.load("en_core_web_sm")

def parse_ride_details(text):
    """
    Parse the input text to extract ride details: pickup, drop, time, ride_type.
    Args:
        text (str): Transcribed user input.
    Returns:
        dict: Extracted details with keys: pickup, drop, time, ride_type.
    """
    doc = nlp(text.lower())
    pickup = None
    drop = None
    time = None
    ride_type = None

    # Extract entities for pickup and drop locations (GPE or LOC)
    locations = [ent.text for ent in doc.ents if ent.label_ in ("GPE", "LOC")]
    if len(locations) >= 2:
        pickup = locations[0]
        drop = locations[1]
    elif len(locations) == 1:
        pickup = locations[0]

    # Extract time expressions using regex and spaCy entities
    time_pattern = re.compile(r'\b(at|around|by)?\s*(\d{1,2}(:\d{2})?\s*(am|pm)?)\b')
    time_match = time_pattern.search(text.lower())
    if time_match:
        time = time_match.group(2)
    else:
        # fallback: look for TIME entities
        times = [ent.text for ent in doc.ents if ent.label_ == "TIME"]
        if times:
            time = times[0]

    # Extract ride type keywords
    ride_types = ["uber", "rapido", "cab", "auto", "bike", "car"]
    for token in doc:
        if token.text in ride_types:
            ride_type = token.text
            break

    # Return extracted details
    return {
        "pickup": pickup,
        "drop": drop,
        "time": time,
        "ride_type": ride_type
    }
