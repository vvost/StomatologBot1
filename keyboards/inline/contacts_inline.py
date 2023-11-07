from aiogram import types

def get_contacts():

    markup = types.InlineKeyboardMarkup()
    inst=types.InlineKeyboardButton('🟣Instagram',callback_data='inst',url='https://www.instagram.com/dr.makka_gagieva/')
    tg=types.InlineKeyboardButton('🔵Telegram',callback_data='tg',url='https://t.me/MakkaGagieva')
    back_button = types.InlineKeyboardButton('Назад↩️', callback_data='back_services')
    markup.row(inst,tg)

    markup.add(back_button)
    return markup
