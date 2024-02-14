from loguru import logger
from telebot.types import CallbackQuery

from loader import bot
from states.find_hotels import FindHotel
from utils.calendar import create_calendar


@bot.callback_query_handler(func=None, state=FindHotel.check_in_date)
def check_in_date(call: CallbackQuery) -> None:
    """
    Запрашивает у пользователя дату заезда и сохраняет ее

    :param call: вызов

    :return: None
    """

    result, keyboard, step = create_calendar(call, is_process=True)

    if not result and keyboard:
        bot.edit_message_text(f'Укажите {step} заезда',
                              call.from_user.id,
                              call.message.message_id,
                              reply_markup=keyboard)

    elif result:
        logger.info(f'Сохраняется дата заезда {call.from_user.id}')
        answer = {}
        year, month, day = str(result).split('-')
        answer['year'] = year
        answer['month'] = month
        answer['day'] = day
        with bot.retrieve_data(call.from_user.id) as data:
            data['check_in'] = answer
            answer.clear()

        bot.send_message(call.from_user.id, f'Дата заезда: {str(result)}')
        bot.set_state(call.message.chat.id, FindHotel.check_out_date)
        calendar, step = create_calendar(call)
        bot.answer_callback_query(call.id)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.from_user.id, f"Укажите {step} выезда", reply_markup=calendar)


@bot.callback_query_handler(func=None, state=FindHotel.check_out_date)
def check_in_date(call: CallbackQuery) -> None:
    """
    Запрашивает у пользователя дату выезда и сохраняет ёё

    :param call: вызов
    :return: None
    """

    result, keyboard, step = create_calendar(call, is_process=True)
    if not result and keyboard:
        bot.edit_message_text(f'Укажите {step} выезда',
                              call.from_user.id,
                              call.message.message_id,
                              reply_markup=keyboard)
    elif result:
        logger.info(f'Сохраняется дата выезда {call.from_user.id}')
        answer = {}
        year, month, day = str(result).split('-')
        answer['year'] = year
        answer['month'] = month
        answer['day'] = day
        with bot.retrieve_data(call.from_user.id) as data:
            data['check_out'] = answer
            answer.clear()

        bot.send_message(call.from_user.id, f'Дата выезда: {str(result)}')
        bot.answer_callback_query(call.id)
        bot.delete_message(call.message.chat.id, call.message.message_id)
