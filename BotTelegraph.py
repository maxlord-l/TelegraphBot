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
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        print(current_datetime)
        print("Погода:", data['weather'][0]['description'])
        print("Температура:", data['main']['temp'])
        print("Минимальная:", data['main']['temp_min'])
        print("Максимальная:", data['main']['temp_max'])
    except Exception as e:
        print("Exception (weather):", e)
        pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
