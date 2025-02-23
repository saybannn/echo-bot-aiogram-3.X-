from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Hello! This is a simple echo bot.\n"
                         "Type ant text and bot will repeat it!")    


@dp.message()
async def echo_message(message: Message):
    await message.answer(message.text)    


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot has been stopped.")
