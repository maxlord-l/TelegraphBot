import requests
from datetime import datetime
from config import weather_key
from pprint import pprint


def get_forecast(city,weather_key):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={weather_key}&units=metric&lang=ru'
        )
        data = r.json()
        print(data)

    except Exception as e:
        print(e)
get_forecast('Санкт-Петербург', weather_key)