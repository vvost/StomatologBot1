from aiogram import types
from loader import dp

from keyboards.inline.menu_inline import get_about_keyboard
from keyboards.inline.contacts_inline import get_contacts

@dp.callback_query_handler(lambda c: c.data == 'contacts')
async def handle_contacts(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id


    img='https://cloud.mail.ru/public/g4jv/g6w2oH9qe'


    description = 'Наш адресс : Метро Третьяковская / Полянка  \n Наш номер:+8(964)028-33-37'

    await dp.bot.send_photo(chat_id,caption= description, reply_markup=get_contacts(),photo=img)
    await callback.message.delete()

@dp.callback_query_handler(lambda c: c.data == 'back_services')
async def handle_back_services(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id

    image_url = 'https://cloud.mail.ru/public/qv6b/QGvDJA8ZQ'  # Замените это на реальный URL изображения

    # Отправляем описание

    description = '🌼 Здравствуйте! 🌼\n' \
                  'Добро пожаловать в мой чат-бот ! \n' \
                  '👩‍⚕️Меня зовут Макка, и я профессиональный косметолог\n' \
                  'Через этого бота вы можете записаться ко мне на запись. Вместе мы найдем лучшие решения для вашей красоты и здоровья. Не стесняйтесь задавать вопросы и обращаться за помощью.\n' \
                  '🌟 Рады видеть вас здесь! 🌟'
    await dp.bot.send_photo(chat_id, caption=description, reply_markup=get_about_keyboard(), photo=image_url)
    await callback_query.message.delete()
