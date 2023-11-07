from aiogram import types
from loader import dp

from keyboards.inline.uslugi_inline import get_services_keyboard
from keyboards.inline.menu_inline import get_about_keyboard


@dp.callback_query_handler(lambda c: c.data == 'services1')
async def handle_services(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id

    image1 = 'https://cloud.mail.ru/public/Ruiy/pHR1mxAuw'

    description = '#Эпиляция (Лазерная)\n' \
                  'Все тело (также ведётся прием мужчин).\n' \
                  'Диодный аппарат премиум класса доведёт ваше тело до идеала, уже после первой процедуры вы будете удивлены результату.\n' \
                  'Обратите особое внимание на цену, которая сохраняется на полный курс💵\n' \
                  'Прием ведет врач дерматолог-косметолог 🥼💉\n' \
                  'Москва:\n' \
                  '🔘м. Полянка (4-6 минут)\n' \
                  '🟠м. Третьяковская (5 минут)\n' \
                  '🟢м. Новокузнецкая (5-7минут)'

    await dp.bot.send_photo(chat_id,caption= description, reply_markup=get_services_keyboard(),photo=image1)
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
