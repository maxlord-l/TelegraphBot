import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import weather_key
import datetime
import requests


API_TOKEN = '1832273668:AAEO2eKblWxfWa56InpogBm-DEFTVNOw2EM'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
main_info_search = {'city': "Санкт-Петербург",
                    'time': " "}
city = str('')

'''@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm TelegraphBot, i'll send you forecast\n"
                        "Привет! Я могу присылать тебе погоду в нужном городе\n"
                        "Напиши мне город в котором надо узнать погоду\n"
                        "Список команд: '/start', '/help'\n"
                        "Введите город, в котором вы хотите узнать погоду")'''

@dp.message_handler(commands=['start'])
async def option_of_weather(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['На день', 'На 5 дней']
    keyboard.add(*buttons)
    await message.answer("На какой срок вы хотите узнать прогноз погоды?", reply_markup=keyboard)

'''    inform = message.text
    main_info_search['city'] = inform   # сохраняется в виде общей переменной.

    await message.reply(f"Принято, ваш город для дальнейших прогнозов - {main_info_search['city']}")'''




@dp.message_handler(Text(equals='На день'))
async def get_weather(message: types.Message):

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
            f"http://api.openweathermap.org/data/2.5/weather?q={main_info_search['city']}&appid={weather_key}&units=metric&lang=ru"
        )
        data = res.json()

        city = data['name']
        weather = data["weather"][0]["main"]
        if weather in code_to_icon:
            wd = code_to_icon[weather]
        else:
            wd = "Я испытываю некоторые трудности с определением погоды, по возможности посмотрите сами в окно"
        cur_temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        country = data["sys"]["country"]

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе {city},{country}\nТемпература: {cur_temp}C, {wd}\nОщущается как: {feels_like}C"
              f"\nВлажность: {humidity}% \nДавление: {pressure}мм.рт.ст"
              f"\nВремя рассвета: {sunrise_timestamp} \nВремя заката: {sunset_timestamp}"
              f"\nХорошего дня!")

    except Exception as ex:
        print(ex)
        pass





@dp.message_handler(Text(equals='На 5 дней'))
async def get_forecast_week(message: types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/forecast?q={main_info_search['city']}&appid={weather_key}&units=metric&lang=ru"
        )
        data = r.json()
        city = data['city']['name']
        first_day = data['list'][5]['dt_txt']
        first_day_temp = data['list'][5]['main']['temp']
        first_day_humidity = data['list'][5]['main']['humidity']
        first_day_pressure = data['list'][5]['main']['pressure']
        first_day_wd = data['list'][5]['weather'][0]['description']
        first_day_wd = str(first_day_wd)
        second_day = data['list'][13]['dt_txt']
        second_day_temp = data['list'][13]['main']['temp']
        second_day_humidity = data['list'][13]['main']['humidity']
        second_day_pressure = data['list'][13]['main']['pressure']
        second_day_wd = data['list'][13]['weather'][0]['description']
        third_day = data['list'][21]['dt_txt']
        third_day_temp = data['list'][21]['main']['temp']
        third_day_humidity = data['list'][21]['main']['humidity']
        third_day_pressure = data['list'][21]['main']['pressure']
        third_day_wd = data['list'][21]['weather'][0]['description']
        fourth_day = data['list'][29]['dt_txt']
        fourth_day_temp = data['list'][29]['main']['temp']
        fourth_day_humidity = data['list'][29]['main']['humidity']
        fourth_day_pressure = data['list'][29]['main']['pressure']
        fourth_day_wd = data['list'][29]['weather'][0]['description']
        fifth_day = data['list'][37]['dt_txt']
        fifth_day_temp = data['list'][37]['main']['temp']
        fifth_day_humidity = data['list'][37]['main']['humidity']
        fifth_day_pressure = data['list'][37]['main']['pressure']
        fifth_day_wd = data['list'][37]['weather'][0]['description']
        await message.reply(f"{city} \n"
                            f"{first_day}: \n"
              f"Температура: {first_day_temp}C \n"
              f"{first_day_wd.capitalize()} \n"
              f"Давление: {first_day_pressure} мм.рт.ст. \n"
              f"Влажность: {first_day_humidity}% \n\n"
                            f""
              f"{second_day}: \n"
              f"Температура: {second_day_temp}C \n"
              f"{second_day_wd.capitalize()} \n"
              f"Давление: {second_day_pressure}мм.рт.ст \n"
              f"Влажность: {second_day_humidity}% \n\n"
                            f""
              f"{third_day}: \n"
              f"Температура: {third_day_temp}C \n"
              f"{third_day_wd.capitalize()} \n"
              f"Давление: {third_day_pressure}мм.рт.ст \n"
              f"Влажность: {third_day_humidity}% \n\n"
                            f""
              f"{fourth_day}: \n"
              f"Температура: {fourth_day_temp}C \n"
              f"{fourth_day_wd.capitalize()} \n"
              f"Давление: {fourth_day_pressure}мм.рт.ст \n"
              f"Влажность: {fourth_day_humidity}% \n\n"
                            f""
              f"{fifth_day}: \n" 
              f"Температура: {fifth_day_temp}C \n"
              f"{fifth_day_wd.capitalize()} \n"
              f"Давление: {fifth_day_pressure}мм.рт.ст \n"
              f"Влажность: {fifth_day_humidity}% \n")


    except Exception as e:
        print(e)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
