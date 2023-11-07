import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN')) #Токен бота в файле .env

admins = [
    6109859293 #admin
]

DATABASES = {
    'default': {
        'NAME': 'smth_wrong',
        'USER': 'root',
        'PASSWORD': 'Chel_228',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}