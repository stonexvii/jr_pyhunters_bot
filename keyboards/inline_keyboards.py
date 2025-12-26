from collections import namedtuple

from aiogram.utils.keyboard import InlineKeyboardBuilder

from .callback_data import CallbackMenu

Button = namedtuple('Button', ['text', 'callback'])


def ikb_main_menu():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        Button('Рандомный факт', 'random'),
        Button('Спросить GPT', 'gpt'),
        Button('Разговор со звездой', 'talk'),
        Button('КВИЗ!', 'quiz'),
    ]
    for button in buttons:
        keyboard.button(
            text=button.text,
            callback_data=CallbackMenu(button=button.callback),
        )
    keyboard.adjust(2, 2)
    return keyboard.as_markup()


def ikb_random():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        Button('Хочу еще!', 'random'),
        Button('Закончить!', 'start'),
    ]
    for button in buttons:
        keyboard.button(
            text=button.text,
            callback_data=CallbackMenu(button=button.callback),
        )
    return keyboard.as_markup()


def ikb_gpt_menu():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        Button('Еще запрос', 'gpt'),
        Button('Закончить!', 'start'),
    ]
    for button in buttons:
        keyboard.button(
            text=button.text,
            callback_data=CallbackMenu(button=button.callback),
        )
    return keyboard.as_markup()


def ikb_cancel_gpt():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text='Отмена',
        callback_data=CallbackMenu(button='start'),
    )
    return keyboard.as_markup()
