from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def keyboard_main_menu():
    keyboard = ReplyKeyboardBuilder()
    buttons = [
        '/random',
        '/gpt',
        '/talk',
        '/quiz',
    ]
    for button in buttons:
        keyboard.button(
            text=button,
        )
    return keyboard.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def ikb_random():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        'Хочу еще факт!',
        'Закончить',
    ]
    for button in buttons:
        keyboard.button(
            text=button,
            callback_data='1',
        )
    return keyboard.as_markup()
