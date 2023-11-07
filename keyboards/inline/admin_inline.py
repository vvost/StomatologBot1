from aiogram import types

def admin_start():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Мои клиенты", callback_data='clients')
    item2 = types.InlineKeyboardButton("Добавить запись", callback_data='add_client')
    markup.row(item1)
    markup.row(item2)
    return markup

def back():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Назад", callback_data='back')
    markup.row(item1)
    return markup


'''def client_start():
    markup=types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Удалить", callback_data='delete')
    item2 = types.InlineKeyboardButton("Изменить", callback_data='edit')
    item3=types.InlineKeyboardButton('Обновить',callback_data='update')

    markup.row(item1)
    markup.row(item2)
    markup.row(item3)
    return markup'''
