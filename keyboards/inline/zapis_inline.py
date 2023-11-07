from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

def get_keyboards():

    markup = ReplyKeyboardMarkup(
        keyboard=[

                    [KeyboardButton("Лицо"),],
                    [KeyboardButton("Усики"),],
                    [KeyboardButton("Подбородок"),],
                    [KeyboardButton("Бакенбарды"),],
                    [KeyboardButton("Шея"),],
                    [KeyboardButton("Грудь"),],
                    [KeyboardButton("Линия живота"),],
                    [KeyboardButton("Область живота"),],
                    [KeyboardButton("Спина(полностью)"),],
                    [KeyboardButton("Ягодицы"),],
                    [KeyboardButton("Бикини(классическое)"),],
                    [KeyboardButton("Бикини(глубокое)"),],
                    [KeyboardButton("Подмышки"),],
                    [KeyboardButton("Руки(полностью)"),],
                    [KeyboardButton("Руки(до локтя)"),],
                    [KeyboardButton("Ноги(полностью)"),],
                    [KeyboardButton("Бёдра"),],
                    [KeyboardButton("Голени"),],


            ],


        resize_keyboard=True
    )
    return markup


def get_time():
    markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("10:00-11:00"),],
            [KeyboardButton("11:00-12:00"),],
            [KeyboardButton("12:00-13:00"),],
            [KeyboardButton("14:00-15:00"),],
            [KeyboardButton("15:00-16:00"),],
            [KeyboardButton("16:00-17:00"),],
            [KeyboardButton("17:00-18:00"),],
            [KeyboardButton("18:00-19:00"),],
            [KeyboardButton("19:00-20:00"), ],

        ],
        resize_keyboard=True
    )
    return markup

def get_services_keyboard():

    markup = types.InlineKeyboardMarkup()

    back_button = types.InlineKeyboardButton('Назад↩️', callback_data='back_services')

    markup.add(back_button)
    return markup
