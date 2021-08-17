import logging
from aiogram import Bot, Dispatcher, executor, types
from test import get_weather
city_id = 498817

API_TOKEN = '1832273668:AAEO2eKblWxfWa56InpogBm-DEFTVNOw2EM'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nI'm TelegraphBot, i'll send you forecast")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
