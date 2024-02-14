from datetime import date

from telebot.types import CallbackQuery
from telegram_bot_calendar import DetailedTelegramCalendar

ALL_STEPS = {'y': 'год', 'm': 'месяц', 'd': 'день'}


def create_calendar(call: CallbackQuery, min_date=None, is_process: bool = None, locale='ru'):
    """
    Генерирует календарь

    :param call: нажатие на кнопку(отклик) пользователя
    :param min_date: дата с которой формируется календарь
    :param is_process: переключатель для создания календаря
    :param locale: локализация
    :return:
    """
    if min_date is None:
        min_date = date.today()

    if is_process:
        result, keyboard, step = DetailedTelegramCalendar(min_date=min_date, locale=locale).process(
            call_data=call.data)
        return result, keyboard, ALL_STEPS[step]
    else:
        calendar, step = DetailedTelegramCalendar(current_date=min_date,
                                                  min_date=min_date,
                                                  locale=locale).build()
        return calendar, ALL_STEPS[step]