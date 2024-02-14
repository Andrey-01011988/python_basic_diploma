from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message) -> None:
    """
    bot_help
    Выводит все доступные пользователю команды бота

    :param message:
    :return:
    """
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))