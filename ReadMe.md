## Flask Weather App - README

### Overview

This Flask app fetches weather data based on a user-provided date and location. It uses Visual Crossing for weather data and OpenWeather for geocoding (converting location names to coordinates). The app can handle both future forecasts and past weather trends by specifying the desired date.

**Visual Crossing** offers a comprehensive Weather API that provides both historical and forecast weather data.
https://www.visualcrossing.com/weather/weather-data-services

Here's an overview of its free tier capabilities:

*Free Tier Features:*

Daily Record Limit: Access up to 1,000 weather records per day without any cost. 

*VISUAL CROSSING Data Coverage:*

1. Historical Data: Access up to 50 years of past weather data, including temperature, rainfall, snowfall, wind, and other meteorological measurements. 

2. Forecast Data: Obtain 15-day weather forecasts to assist in planning and decision-making. 

3. Current Conditions: Retrieve real-time weather information for various locations. 

4. Global Coverage: Access weather data for locations worldwide, ensuring comprehensive information regardless of your location. 
VISUAL CROSSING

### Features

**Flexible Date Parsing**: Accepts dates like "tomorrow", "next week", or specific formats (e.g., "25th of January 2025").

**Location Geocoding**: Converts city names to latitude and longitude automatically.

**Forecast & Historical Data**: Fetches weather data for any specified date.

**JSON Output**: Returns weather data in structured JSON format.

**Robust Error Handling**: Manages invalid dates, locations, and missing parameters.

### Requirements

1. Python 3.x

2. Flask

3. Requests

4. Dateparser

### Installation

**Clone the repository:**

git clone https://github.com/Miracle-Bassey/ThermalRetrievalApp.git
cd ThermalRetrievalApp


Set API Keys:

Replace the placeholders in the app code with your API keys:

VISUALCROSSING_API_KEY = 'your_visualcrossing_key'
GEOCODING_API_KEY = 'your_geocoding_key'

Running the App

Start the Flask server:

python ThermalRetrievalApp.py

Access the app at:

http://localhost:5000/

Usage

Making Requests

You can request weather data by visiting the following URL in your browser or using curl:

http://localhost:5000/weather?date=tomorrow&location=London

URL Parameters:

date: Specify the date in formats like "tomorrow", "next week", or "15th of February 2025".

location: The city or place name (e.g., "Paris", "Tokyo").

Example Requests:

Tomorrow's weather in New York:

http://localhost:5000/weather?date=tomorrow&location=New%20York

Next Monday's weather in Paris:

http://localhost:5000/weather?date=next%20Monday&location=Paris

Testing with curl:

curl "http://localhost:5000/weather?date=next%20friday&location=Tokyo"

API Response

A successful response returns JSON with weather details:

{
    "cloudcover": 52.9,
    "conditions": "Partially cloudy",
    "datetime": "2025-01-25",
    "datetimeEpoch": 1737759600,
    "description": "",
    "dew": 22.4,
    "feelslike": 38.0,
    "feelslikemax": 0.0,
    "feelslikemin": 0.0,
    "humidity": 74.1,
    "icon": "partly-cloudy-day",
    "moonphase": 0.87,
    "normal": {
        "cloudcover": [
            0.0,
            52.9,
            90.0
        ],
        "feelslike": [
            18.9,
            32.9,
            43.6
        ],
        "humidity": [
            41.6,
            74.1,
            85.3
        ],
        "precip": [
            0.0,
            2.3,
            46.0
        ],
        "snowdepth": [
            null,
            null,
            null
        ],
        "tempmax": [
            30.1,
            32.9,
            35.0
        ],
        "tempmin": [
            18.9,
            24.4,
            31.4
        ],
        "winddir": [
            50.0,
            205.9,
            267.1
        ],
        "windgust": [
            18.4,
            24.1,
            29.5
        ],
        "windspeed": [
            13.0,
            23.4,
            40.7
        ]
    },
    "precip": 2.3,
    "precipcover": 0.0,
    "precipprob": 0.0,
    "preciptype": null,
    "pressure": 1010.8,
    "snow": null,
    "snowdepth": null,
    "solarenergy": null,
    "solarradiation": null,
    "source": "stats",
    "stations": null,
    "sunrise": "07:04:11",
    "sunriseEpoch": 1737785051,
    "sunset": "18:53:35",
    "sunsetEpoch": 1737827615,
    "temp": 28.2,
    "tempmax": 32.9,
    "tempmin": 24.4,
    "uvindex": null,
    "visibility": 6.4,
    "winddir": 205.9,
    "windgust": 24.1,
    "windspeed": 23.4
}

Error Handling

Missing parameters:

{"error": "Missing date or location parameter"}

Invalid location:

{"error": "Invalid location"}

Invalid date:

{"error": "Invalid date"}

Notes

The Visual Crossing free plan allows up to 1,000 records per day.

Ensure your API keys for Visual Crossing and OpenWeather are active and correct.

