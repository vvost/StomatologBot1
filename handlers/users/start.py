from aiogram.types import ContentType, Message
from aiogram import types
from keyboards.inline.start_inline import get_menu_markup
from keyboards.inline.menu_inline import get_about_keyboard
from keyboards.inline.admin_inline import admin_start

from loader import dp





@dp.message_handler(commands=['start'])
async def handle_cosmetology(message: types.Message):
    chat_id = message.chat.id


    # Отправляем фотографию

    image_url = 'https://cloud.mail.ru/public/qv6b/QGvDJA8ZQ'  # Замените это на реальный URL изображения


    # Отправляем описание


    description = '🌼 Здравствуйте! 🌼\n' \
                      'Добро пожаловать в мой чат-бот ! \n' \
                      '👩‍⚕️Меня зовут Макка, и я профессиональный косметолог\n' \
                      'Через этого бота вы можете записаться ко мне на запись. Вместе мы найдем лучшие решения для вашей красоты и здоровья. Не стесняйтесь задавать вопросы и обращаться за помощью.\n' \
                      '🌟 Рады видеть вас здесь! 🌟'
    await dp.bot.send_photo(chat_id, caption=description, reply_markup=get_about_keyboard(), photo=image_url)
    await message.delete()
