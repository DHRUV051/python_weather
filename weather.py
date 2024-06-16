"""This Project Used to Find Weather of a Place"""

import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_current_weather(city="New York"):

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"

    weather_data = requests.get(request_url, timeout=10).json()
    
    return weather_data