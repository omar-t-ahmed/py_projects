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

def display_weather(data):
    if data['cod'] != 200:
        print("City not found.")
        return
    
    city = data['name']
    temp = data['main']['temp']
    weather_desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    
    print(f"City: {city}")
    print(f"Temperature: {temp}°C")
    print(f"Weather: {weather_desc}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather_app.py <city_name>")
        return
    
    city_name = sys.argv[1]
    weather_data = get_weather(city_name)
    display_weather(weather_data)

if __name__ == '__main__':
    main()