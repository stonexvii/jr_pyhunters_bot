from aiogram import Router, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, InputMediaPhoto
from aiogram.types.input_file import FSInputFile
from aiogram.enums.chat_action import ChatAction

from keyboards import keyboard_main_menu, ikb_random
import config
from utils import FileManager
from utils.enum_path import Path
from ai_open import chat_gpt
from ai_open.messages import GPTMessage

main_router = Router()


@main_router.message(Command('start', 'gpt', 'talk', 'quiz'))
async def command_handler(message: Message, command: CommandObject):
    keyboard = None
    if command.command == 'start':
        keyboard = keyboard_main_menu()
    await message.answer_photo(
        photo=FSInputFile(Path.IMAGES.value.format(file=command.command)),
        caption=FileManager.read_txt(Path.MESSAGES, command.command),
        reply_markup=keyboard,
    )


@main_router.message(Command('random'))
async def random_handler(message: Message, command: CommandObject, bot: Bot):
    await message.answer_photo(
        photo=FSInputFile(Path.IMAGES.value.format(file=command.command)),
        caption=FileManager.read_txt(Path.MESSAGES, command.command),
    )
    await bot.send_chat_action(
        chat_id=message.from_user.id,
        action=ChatAction.TYPING,
    )
    response = await chat_gpt.request(GPTMessage('random'), bot)
    await bot.edit_message_media(
        media=InputMediaPhoto(
            media=FSInputFile(Path.IMAGES.value.format(file=command.command)),
            caption=response,
        ),
        chat_id=message.from_user.id,
        message_id=message.message_id + 1,
        reply_markup=ikb_random(),
    )


@main_router.message()
async def all_messages(message: Message, bot: Bot):
    msg_text = f'Пользователь {message.from_user.full_name} написал:\n{message.text}'
    await bot.send_message(
        chat_id=config.ADMIN_ID,
        text=msg_text,
    )
