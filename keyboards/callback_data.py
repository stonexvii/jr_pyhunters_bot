from aiogram.filters.callback_data import CallbackData


class CallbackMenu(CallbackData, prefix='CM'):
    button: str
