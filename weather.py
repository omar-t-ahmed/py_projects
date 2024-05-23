import requests
import json
import sys
import logging

API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

logging.basicConfig(level=logging.INFO)

def get_weather(city_name, units='imperial'):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': units
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"Other error occurred: {err}")
    return None

def display_weather(data, units):
    if data is None or data['cod'] != 200:
        print("City not found or unable to fetch data.")
        return
    
    city = data['name']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    weather_desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    visibility = data.get('visibility', 'N/A')
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']

    temp_unit = "°F" if units == 'imperial' else "°C"
    speed_unit = "m/s" if units == 'metric' else "mph"

    print(f"City: {city}")
    print(f"Temperature: {temp}{temp_unit}")
    print(f"Feels Like: {feels_like}{temp_unit}")
    print(f"Weather: {weather_desc}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} {speed_unit}")
    print(f"Visibility: {visibility} meters")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python weather_app.py <city_name> [units]")
        return
    
    city_name = sys.argv[1]
    units = sys.argv[2] if len(sys.argv) == 3 else 'imperial'
    
    if units not in ['imperial', 'metric']:
        print("Invalid units. Use 'imperial' or 'metric'.")
        return
    
    weather_data = get_weather(city_name, units)
    display_weather(weather_data, units)

if __name__ == '__main__':
    main()