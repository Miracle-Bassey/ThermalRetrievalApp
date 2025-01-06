import requests
from datetime import datetime
import dateparser
from flask import request, jsonify
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('config.env')

# Access the API keys from the environment
VISUALCROSSING_API_KEY = os.getenv('VISUALCROSSING_API_KEY')
GEOCODING_API_KEY = os.getenv('GEOCODING_API_KEY')

# API Endpoints
VISUALCROSSING_FORECAST_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
GEOCODING_URL = 'https://api.openweathermap.org/geo/1.0/direct'

#print(VISUALCROSSING_API_KEY)

# Get today's date
today = datetime.now().date()


# Convert location name to coordinates
def get_coordinates(location):
    """Convert a location name to latitude and longitude using the geocoding API."""
    response = requests.get(
        GEOCODING_URL,
        params={
            'q': location,
            'limit': 1,
            'appid': GEOCODING_API_KEY
        }
    )
    if response.status_code != 200:
        raise ValueError(f"Geocoding API error: {response.status_code} - {response.text}")

    data = response.json()
    if data:
        return data[0]['lat'], data[0]['lon']
    else:
        raise ValueError(f"Location '{location}' not found.")


# Forecast and Historical function (Visual Crossing only)
def get_weather_data(date, location):
    """Fetch weather data for the specified date and location."""
    lat, lon = get_coordinates(location)
    response = requests.get(
        f"{VISUALCROSSING_FORECAST_URL}{lat},{lon}/{date}/",
        params={'key': VISUALCROSSING_API_KEY, 'unitGroup': 'metric'}
    )
    if response.status_code != 200:
        raise ValueError(f"Weather API error: {response.status_code} - {response.text}")

    data = response.json()  # Parse the response body as JSON

    return data.get('days', [{}])[0]  # Return the first day's weather data (as a dictionary)


# Date parsing function
def parse_date(date_str):
    """Parse the date string into a datetime object."""
    parsed_date = dateparser.parse(date_str)
    if parsed_date is None:
        raise ValueError(f"Invalid date format: '{date_str}'")
    return parsed_date.date()


def weather(date_str, location):
    """Standalone function to get weather data for a given date and location."""
    if not date_str or not location:
        return {'error': 'Missing date or location parameter'}

    try:
        date = parse_date(date_str)
        weather_data = get_weather_data(date, location)
        return weather_data  # Return as a dictionary
    except ValueError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': f"Internal server error: {str(e)}"}
