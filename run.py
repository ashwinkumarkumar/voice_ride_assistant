"""
Entry point for the voice ride assistant application.
Calls app.main to start the Flask server.
"""

from app.main import app

if __name__ == "__main__":
    app.run(debug=True)
