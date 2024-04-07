import asyncio
import logging

from aiogram import  Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv
from app.handlers import router


load_dotenv()

bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


async def start():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Starting..")
        asyncio.run(start())
    except KeyboardInterrupt:
        print("Exit")