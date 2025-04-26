import requests
import json

def get_weather():
    api_url = "https://aviationweather.gov/api/data/windtemp?region=hawaii"

    response = requests.get(api_url)

    print(response.text)



