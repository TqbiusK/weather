from typing import Dict, Any

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def kelvin_to_fahrenheit(kelvin: float) -> float:
    """
    Convert temperature from Kelvin to Fahrenheit.

    Parameters:
        kelvin (float): Temperature in Kelvin.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (kelvin - 273.15) * 9/5 + 32

def mps_to_mph(mps: float) -> float:
    """
    Convert speed from meters per second to miles per hour.

    Parameters:
        mps (float): Speed in meters per second.

    Returns:
        float: Speed in miles per hour.
    """
    return mps * 2.23694  # Conversion factor from meters per second to miles per hour

def get_weather_data(city_state: str) -> tuple[None, str] | tuple[dict[str, str | Any], None]:
    """
    Get weather data for a given city and state.

    Parameters:
        city_state (str): City and state in the format "City, State".

    Returns:
        tuple[dict, str]: A tuple containing a dictionary with weather information
                         and a string indicating any errors encountered.
    """
    geo = Nominatim(user_agent="my_geocoder")

    try:
        location = geo.geocode(city_state)
        if location is None:
            return None, "Location not found. Please enter a valid city and state."
    except Exception as e:
        return None, f"Error finding location: {str(e)}"

    # Get timezone
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime('%I:%M %p')

    api_key = '74358e1d5982a2c1d2d5a7460b492310'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_state}&appid={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
    except requests.RequestException as e:
        return None, f"Error fetching weather data: {str(e)}"

    return {
        'location': location,
        'current_time': current_time,
        'weather_data': weather_data
    }, None
