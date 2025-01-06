import requests
from datetime import datetime, timedelta
import dateparser
from flask import Flask, request, jsonify

app = Flask(__name__)

# API Keys
VISUALCROSSING_API_KEY = 'Z829VQ63BZEBVLQUV4VV76SVS'          # https://www.visualcrossing.com/weather/weather-data-services

GEOCODING_API_KEY = '69142fa91901f62ebfc51c82d82e21b5'        #https://home.openweathermap.org/api_keys

# API Endpoints
VISUALCROSSING_FORECAST_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
GEOCODING_URL = 'https://api.openweathermap.org/geo/1.0/direct'

# Get today's date
today = datetime.now().date()


# Convert location name to coordinates
def get_coordinates(location):
    response = requests.get(
        GEOCODING_URL,
        params={
            'q': location,
            'limit': 1,
            'appid': GEOCODING_API_KEY
        }
    )
    data = response.json()
    if data:
        return data[0]['lat'], data[0]['lon']
    else:
        raise ValueError("Invalid location")


# Forecast and Historical function (Visual Crossing only)
def get_weather_data(date, location):
    lat, lon = get_coordinates(location)
    response = requests.get(
        f"{VISUALCROSSING_FORECAST_URL}{lat},{lon}/{date}/",
        params={'key': VISUALCROSSING_API_KEY, 'unitGroup': 'metric'}
    )
    data = response.json()
    return data.get('days', [{}])[0]


# Date parsing function
def parse_date(date_str):
    return dateparser.parse(date_str).date()


# Flask route to handle weather requests
@app.route('/weather', methods=['GET'])
def weather():
    date_str = request.args.get('date')
    location = request.args.get('location')
    if not date_str or not location:
        return jsonify({'error': 'Missing date or location parameter'}), 400

    try:
        date = parse_date(date_str)
        weather_data = get_weather_data(date, location)
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)