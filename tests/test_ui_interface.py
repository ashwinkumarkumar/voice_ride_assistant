import pytest
from streamlit.testing import StreamlitRunner
from ui.interface import main

def test_ui_interface_runs():
    # This test will just run the Streamlit app main function to check for errors
    try:
        main()
    except Exception as e:
        pytest.fail(f"Streamlit interface failed to run: {e}")

if __name__ == "__main__":
    pytest.main([__file__])
