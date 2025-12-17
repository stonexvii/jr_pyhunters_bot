from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start_command(message):
    print(message)


@dp.message()
async def all_messages(message: Message, bot: Bot):
    msg_text = f'Пользователь {message.from_user.full_name} написал:\n{message.text}'
    await bot.send_message(
        chat_id=1954334266,
        text=msg_text,
    )


async def start_bot():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())
