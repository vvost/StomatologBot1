from aiogram import types
from loader import dp

from keyboards.inline.about_inline import about
from keyboards.inline.menu_inline import get_about_keyboard


@dp.callback_query_handler(lambda c: c.data == 'about')
async def handle_about(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id

    # Получение инлайн-клавиатуры "О-нас"
    photo='https://cloud.mail.ru/public/qv6b/QGvDJA8ZQ'

    description = '🏨Я врач-косметолог с 3ех летним опытом. Занимаюсь лазерной депиляцией всего тела. ' \
                      'Сегодня, с накопленным опытом и страстью к работе, я предлагаю вам мои услуги в современной косметологии.\n \n' \
                      '☎️Наши телефоны: +8(964)028-33-37\n \n' \
                      '🗺Мы находимся по адресу: Метро Третьяковская / Полянка\n \n' \
                      '❇️Доверьтесь нам, и мы поможем вам достичь желаемых результатов, сохранить здоровье и уверенность в себе. Мы гордимся нашей работой и с нетерпением ждем, чтобы увидеть вас'
    await dp.bot.send_photo(chat_id,caption=description, reply_markup=about(),photo=photo)
    await callback.message.delete()



@dp.callback_query_handler(lambda c: c.data == 'back')
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



