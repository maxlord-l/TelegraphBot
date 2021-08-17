import requests
import datetime
from config import weather_key


def get_weather(city, weather_key):
    code_to_icon = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    try:
        res = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric'
        )
        data = res.json()


        city = data['name']
        weather = data["weather"][0]["main"]
        if weather in code_to_icon:
            wd = code_to_icon[weather]
        else:
            wd = "Я испытываю некоторые трудности с определение погоды, по возможности посмотрите сами в окно"
        cur_temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе {city}\nТемпература:{cur_temp}C {wd}\nОщущается как:{feels_like}C"
              f"\nВлажность:{humidity}% \nДавление:{pressure}мм.рт.ст"
              f"\nВремя рассвета:{sunrise_timestamp} \nВремя заката:{sunset_timestamp}"
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