from aiogram import types


def get_services_keyboard():

    markup = types.InlineKeyboardMarkup()

    back_button = types.InlineKeyboardButton('Назад↩️', callback_data='back_services')
    markup.add(back_button)
    return markup
