from aiogram import types

def about():

    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Назад↩️",callback_data='back')
    markup.row(item1)
    return markup
