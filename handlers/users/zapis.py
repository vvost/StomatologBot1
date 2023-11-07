import pymysql
import re
from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
from data.config import DATABASES
from keyboards.inline.zapis_inline import get_services_keyboard, get_keyboards, get_time
from keyboards.inline.menu_inline import get_about_keyboard


# Инициализация соединения с базой данных
conn = pymysql.connect(
    host=DATABASES['default']['HOST'],
    port=int(DATABASES['default']['PORT']),
    user=DATABASES['default']['USER'],
    password=DATABASES['default']['PASSWORD'],
    database=DATABASES['default']['NAME'],
    charset='utf8mb4'
)

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()


# Определение состояний для FSM
class FormStates(StatesGroup):
    FIRST_NAME = State()
    LAST_NAME = State()
    CONTACT_INFO = State()
    SERVICE = State()
    APPOINTMENT_DATE = State()
    APPOINTMENT_TIME = State()  # Изменено на APPOINTMENT_TIME


@dp.callback_query_handler(lambda c: c.data == 'appointment', state='*')
async def start_appointment(query: types.CallbackQuery, state: FSMContext):
    chat_id = query.message.chat.id

    await FormStates.FIRST_NAME.set()

    await query.message.answer("Начинаем запись приема, введите свое имя:")



@dp.message_handler(state=FormStates.FIRST_NAME)
async def start_appointment_process(message: types.Message, state: FSMContext):
    chat_id = message.chat.id

    first_name = message.text
    if not first_name.isalpha():

        await message.reply("Пожалуйста, введите ваше имя текстом. Используйте только буквы.")

        return
    await state.update_data(first_name=first_name)

    await message.reply("Введите свою фамилию:")

    await FormStates.LAST_NAME.set()


@dp.message_handler(state=FormStates.LAST_NAME)
async def process_last_name(message: types.Message, state: FSMContext):
    chat_id = message.chat.id

    last_name = message.text
    if not last_name.isalpha():

        await message.reply("Пожалуйста, введите вашу фамилию текстом. Используйте только буквы.")

        return
    await state.update_data(last_name=last_name)


    await message.reply("Введите ваш контактный номер:")

    await FormStates.CONTACT_INFO.set()


@dp.message_handler(state=FormStates.CONTACT_INFO)
async def process_contact_info(message: types.Message, state: FSMContext):
    contact_info = message.text
    chat_id = message.chat.id

    description = '✳️У вас появятся кнопки возле поля ввода текста. \n' \
                  'Пожалуйста нажмите на одну из кнопок которая соответствует вашим требованиям.\n' \
                  '*Кнопки можно листать вниз'


    if not contact_info.isdigit():

        await message.reply("Пожалуйста, введите контактный номер, используя только цифры.")

        return

    await state.update_data(contact_info=contact_info)
    await message.reply("Введите желаемую услугу:")

    await message.reply(description, reply_markup=get_keyboards())
    await FormStates.SERVICE.set()


@dp.message_handler(state=FormStates.SERVICE)
async def process_service(message: types.Message, state: FSMContext):
    chat_id = message.chat.id

    service = message.text
    await state.update_data(service=service)

    await message.reply("Введите желаемую дату записи в формате ГГГГ-ММ-ДД:\n"
                            "Обязательно пишите через черточку\n"
                            "Пример - 2023-10-28")


    await FormStates.APPOINTMENT_DATE.set()


@dp.message_handler(state=FormStates.APPOINTMENT_DATE)
async def process_appointment_date(message: types.Message, state: FSMContext):
    chat_id = message.chat.id

    appointment_date = message.text
    # Здесь можно выполнить проверку даты, чтобы убедиться, что она корректна

    try:
        appointment_date = datetime.strptime(appointment_date, '%Y-%m-%d').date()
    except ValueError:
        await message.reply("Неверный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")
        return

    await state.update_data(appointment_date=appointment_date)

    await message.reply("Введите желаемое время записи \n"
                            "Пожалуйста нажмите на одну из кнопок желаемого времени\n."
                            "*Кнопки расположены на клавиатуре", reply_markup=get_time())

    await FormStates.APPOINTMENT_TIME.set()  # Изменено на APPOINTMENT_TIME


@dp.message_handler(state=FormStates.APPOINTMENT_TIME)  # Изменено на APPOINTMENT_TIME
async def process_appointment_time(message: types.Message, state: FSMContext):
    chat_id = message.chat.id

    appointment_time = message.text
    # Проверяем, соответствует ли введенное время формату "ЧЧ:ММ-ЧЧ:ММ"
    if not re.match(r'\d{1,2}:\d{2}-\d{1,2}:\d{2}', appointment_time):

        await message.reply("Неверный формат времени. Пожалуйста, введите время в формате 'ЧЧ:ММ-ЧЧ:ММ'.")

        return

    start_time_str, end_time_str = appointment_time.split('-')
    start_time = datetime.strptime(start_time_str, '%H:%M').time()
    end_time = datetime.strptime(end_time_str, '%H:%M').time()

    await state.update_data(appointment_time=appointment_time, start_time=start_time, end_time=end_time)

    # Получаем данные из FSM
    data = await state.get_data()
    first_name = data["first_name"]
    last_name = data["last_name"]
    contact_info = data["contact_info"]
    service = data["service"]
    appointment_date = data["appointment_date"]
    start_time = data["start_time"]
    end_time = data["end_time"]

    # Проверяем доступность времени и даты
    if is_time_available(start_time, end_time, appointment_date):
        # Записываем данные в базу данных MySQL
        add_application(first_name, last_name, contact_info, service, appointment_date, start_time, end_time)

        await bot.send_message(message.chat.id, f"<b>Вас записали на прием:</b>\n"
                                                    f"<b>Имя:</b> {first_name}\n"
                                                    f"<b>Фамилия:</b> {last_name}\n"
                                                    f"<b>Контактный номер:</b> {contact_info}\n"
                                                    f"<b>Услуга:</b> {service}\n"
                                                    f"<b>Дата записи:</b> {appointment_date}\n"
                                                    f"<b>Время записи:</b> {start_time}-{end_time}", parse_mode='HTML',
                                   reply_markup=get_services_keyboard())


    else:

            await bot.send_message(message.chat.id,
                                   "Извините, выбранное вами время и дата не доступны. Пожалуйста, пройдите Регистрацию еще раз и выберите другое время или дату.",
                                   reply_markup=get_services_keyboard())

        # Сбрасываем состояние FSM
    await state.finish()


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



def is_time_available(start_time, end_time, appointment_date):
    # Проверяем доступность времени и даты в базе данных
    query = """
            SELECT COUNT(*) 
            FROM stomatolog_application 
            WHERE appointment_date = %s 
            AND (TIME(start_time) < %s AND TIME(end_time) > %s)
        """
    cursor.execute(query, (appointment_date, end_time, start_time))
    count = cursor.fetchone()[0]

    return count == 0


smth_chanel = "https://t.me/+knSA8Q9RJks1OTdi"

def add_application(first_name, last_name, contact_info, service, appointment_date, start_time, end_time):
    # Добавляем запись в базу данных MySQL
    query = "INSERT INTO stomatolog_application (first_name, last_name, contact_info, service, appointment_date, start_time, end_time) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (first_name, last_name, contact_info, service, appointment_date, start_time, end_time)
    cursor.execute(query, values)
    conn.commit()
