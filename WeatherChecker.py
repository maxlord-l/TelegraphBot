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
        pprint(data)
        city = data['city']['name']
        first_day = data['list'][0]['dt_txt']
        first_day_temp = data['list'][0]['main']['temp']
        first_day_humidity = data['list'][0]['main']['humidity']
        first_day_pressure = data['list'][0]['main']['pressure']
        first_day_wd = data['list'][0]['weather'][0]['description']
        first_day_wd = str(first_day_wd)
        second_day = data['list'][8]['dt_txt']
        second_day_temp = data['list'][8]['main']['temp']
        second_day_humidity = data['list'][8]['main']['humidity']
        second_day_pressure = data['list'][8]['main']['pressure']
        second_day_wd = data['list'][8]['weather'][0]['description']
        third_day = data['list'][16]['dt_txt']
        third_day_temp = data['list'][16]['main']['temp']
        third_day_humidity = data['list'][16]['main']['humidity']
        third_day_pressure = data['list'][16]['main']['pressure']
        third_day_wd = data['list'][16]['weather'][0]['description']
        fourth_day = data['list'][24]['dt_txt']
        fourth_day_temp = data['list'][24]['main']['temp']
        fourth_day_humidity = data['list'][24]['main']['humidity']
        fourth_day_pressure = data['list'][24]['main']['pressure']
        fourth_day_wd = data['list'][24]['weather'][0]['description']
        fifth_day = data['list'][32]['dt_txt']
        fifth_day_temp = data['list'][32]['main']['temp']
        fifth_day_humidity = data['list'][32]['main']['humidity']
        fifth_day_pressure = data['list'][32]['main']['pressure']
        fifth_day_wd = data['list'][32]['weather'][0]['description']
        print(f"{first_day}, {city} \n"
              f"Температура: {first_day_temp}C \n"
              f"{first_day_wd.capitalize()} \n"
              f"Давление: {first_day_pressure} мм.рт.ст. \n"
              f"Влажность: {first_day_humidity}% \n"
              f"{second_day}, {city}"
              f"Температура: {second_day_temp}C \n"
              f"{second_day_wd.capitalize()} \n"
              f"Давление: {second_day_pressure}мм.рт.ст \n"
              f"Влажность: {second_day_humidity}% \n"
              f"{third_day}, {city} \n"
              f"Температура: {third_day_temp}C \n"
              f"{third_day_wd.capitalize()} \n"
              f"Давление: {third_day_pressure}мм.рт.ст \n"
              f"Влажность: {third_day_humidity}% \n"
              f"{fourth_day}, {city} \n"
              f"Температура: {fourth_day_temp}C \n"
              f"{fourth_day_wd.capitalize()} \n"
              f"Давление: {fourth_day_pressure}мм.рт.ст \n"
              f"Влажность: {fourth_day_humidity}% \n"
              f"{fifth_day}, {city} \n"
              f"Температура: {fifth_day_temp}C \n"
              f"{fifth_day_wd.capitalize()} \n"
              f"Давление: {fifth_day_pressure}мм.рт.ст \n"
              f"Влажность: {fifth_day_humidity}% \n")


    except Exception as e:
        print(e)
get_forecast('Moscow', weather_key)