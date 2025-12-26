from aiogram import Router, Bot, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, InputMediaPhoto
from aiogram.types.input_file import FSInputFile
from aiogram.enums.chat_action import ChatAction

from .fsm import GPTRequest
from aiogram.fsm.context import FSMContext
from keyboards import ikb_main_menu, ikb_random, ikb_gpt_menu
import config
from utils import FileManager
from utils.enum_path import Path
from ai_open import chat_gpt
from ai_open.messages import GPTMessage
from keyboards.callback_data import CallbackMenu
from ai_open.enums import GPTRole

fsm_router = Router()


@fsm_router.message(GPTRequest.wait_for_request)
async def wait_for_user_request(message: Message, state: FSMContext, bot: Bot):
    msg_list = GPTMessage('gpt')
    msg_list.update(GPTRole.USER, message.text)
    await bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id,
    )
    response = await chat_gpt.request(msg_list, bot)
    message_id = await state.get_value('message_id')
    await bot.edit_message_media(
        media=InputMediaPhoto(
            media=FSInputFile(Path.IMAGES.value.format(file='gpt')),
            caption=response,
        ),
        chat_id=message.from_user.id,
        message_id=message_id,
        reply_markup=ikb_gpt_menu(),
    )
