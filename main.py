# Для запуска бота
from loader import bot
import handlers  # noqa
from telebot.custom_filters import StateFilter
from utils.set_bot_commands import set_default_commands


if __name__ == "__main__":
    # Добавление фильтра состояний
    bot.add_custom_filter(StateFilter(bot))
    # Отправка на ТГ сервер команд бота
    set_default_commands(bot)
    # Запуск бота с бесконечным циклом получения обновлений
    bot.infinity_polling()
