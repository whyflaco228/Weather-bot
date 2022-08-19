import requests
import datetime
from config import TG_BOT_TOKEN, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет, напиши мне название города и я пришлю сводку погоды!')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        city = data['name']
        current_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']

        await message.reply(f'Температура в городе {city}: {current_weather}\n'
                            f'Влажность: {humidity}\n'
                            f'Давление:{pressure}\n'
                            f'Скорость ветра: {wind_speed}')
    except Exception as ex:
        await message.reply('Проверьте название города!')


if __name__ == '__main__':
    executor.start_polling(dp)
