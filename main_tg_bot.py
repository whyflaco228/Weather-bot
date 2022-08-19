import requests
import datetime
from config import TG_BOT_TOKEN, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(TG_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handlers(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет, напиши мне название города и я пришлю сводку погоды!')


if __name__ == '__main__':
    executor.start_polling(dp)
