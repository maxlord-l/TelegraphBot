import logging
from aiogram import Bot, Dispatcher, executor, types
from config import weather_key
import datetime
import requests
city_id = 498817

API_TOKEN = '1832273668:AAEO2eKblWxfWa56InpogBm-DEFTVNOw2EM'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nI'm TelegraphBot, i'll send you forecast")

@dp.message_handler()
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
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_key}&units=metric'
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
        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе {city}\nТемпература:{cur_temp}C {wd}\nОщущается как:{feels_like}C"
              f"\nВлажность:{humidity}% \nДавление:{pressure}мм.рт.ст"
              f"\nВремя рассвета:{sunrise_timestamp} \nВремя заката:{sunset_timestamp}"
              f"\nХорошего дня!"
              )

    except Exception as ex:
        print(ex)
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
