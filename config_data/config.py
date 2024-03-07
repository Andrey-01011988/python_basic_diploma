import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("SITE_API")
HOST_API = os.getenv("HOST_API")

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("lowprice", "Узнать топ самых дешёвых отелей в городе"),
    ("highprice", "Узнать топ самых дорогих отелей в городе"),
    ("bestdeal",
     "Вывод отелей, наиболее подходящих по цене и расположению от центра "),
    ("history", 'Узнать историю поиска отелей (последние 5 запросов)')
)
