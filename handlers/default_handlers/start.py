from loguru import logger
from telebot.types import Message

from loader import bot


logger.add("log_file.log", backtrace=True, diagnose=True, rotation='10 MB', retention=5)


@bot.message_handler(commands=["start"])
def bot_start(message: Message) -> None:
    bot.reply_to(message, f"Здравствуйте, {message.from_user.full_name}, чтобы узнать все мои функции введите /help")
