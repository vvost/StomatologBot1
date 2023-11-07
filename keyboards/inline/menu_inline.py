from aiogram import types

# Функция для получения инлайн клавиатуры "О нас"
def get_about_keyboard():

    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton('О нас👩🏻‍⚕️🦷', callback_data='about')
    item1 = types.InlineKeyboardButton('Услуги📋', callback_data='services1')
    item2 = types.InlineKeyboardButton('Контакты📞', callback_data='contacts')
    item3 = types.InlineKeyboardButton('Запись📋', callback_data='appointment')
    markup.add(item,item1,item2, item3)
    return markup




