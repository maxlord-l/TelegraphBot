import requests
import datetime
from config import weather_key
from pprint import pprint


def get_weather(city, weather_key):
    try:
        res = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric'
        )
        data = res.json()
        #pprint(data)

        city = data['name']
        cur_temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        weather = data["weather"][0]["main"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(f"Погода в городе {city}\nТемпература:{cur_temp} \nОщущается как:{feels_like}"
              f"\nВлажность:{humidity} \nДавление:{pressure} \nКраткая информация:{weather}"
              f"\nВремя рассвета:{sunrise_timestamp} \nВремя заката:{sunset_timestamp},"
              f"\nХорошего дня!"
              )

    except Exception as ex:
        print(ex)
        pass


def main():
    city = input("Введите город>> ")
    get_weather(city, weather_key)


if __name__ == '__main__':
    main()