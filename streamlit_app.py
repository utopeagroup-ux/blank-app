import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import json
from pathlib import Path

# Default price data (fallback if JSON file is missing/corrupted)
DEFAULT_PRICE_DATA = {
    # Include a minimal version of the original PRICE_DATA here
    "photography": {"site_visit": 150},
    # ... (simplified for brevity)
}

def load_price_data(file_path: str = "price_data.json") -> dict:
    """Load price data from JSON file, with fallback to default data"""
    try:
        if not Path(file_path).exists():
            raise FileNotFoundError(f"Price data file '{file_path}' not found")
        
        with open(file_path, "r", encoding="utf-8") as f:
            price_data = json.load(f)
        
        # Validate critical fields (customize based on your structure)
        required_keys = ["photography", "videography", "event", "yacht"]
        if not all(key in price_data for key in required_keys):
            raise ValueError("Missing critical keys in price data")
        
        return price_data
    
    except (json.JSONDecodeError, FileNotFoundError, ValueError) as e:
        print(f"Error loading price data: {str(e)}. Using default data.")
        return DEFAULT_PRICE_DATA

# Load price data at app startup
PRICE_DATA = load_price_data()
