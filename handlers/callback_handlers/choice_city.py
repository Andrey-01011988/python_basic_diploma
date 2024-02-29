from loader import bot
from telebot.types import CallbackQuery
from loguru import logger
from states.find_hotels import FindHotel
from utils.calendar import create_calendar


@bot.callback_query_handler(func=lambda call: call.data.startswith('q'))
def save_n_continue(call: CallbackQuery) -> None:
    """
    Сохраняет id города и меняет состояние пользователя

    :param call: id города
    :return:None
    """
    logger.info(f'Пользователь выбрал город')
    if call.data:
        id_num = str(call.data)[1:]
        with bot.retrieve_data(call.message.chat.id) as data:
            data['destination_id'] = id_num
        for value in data['cities']:
            if value['id'] == data['destination_id']:
                bot.send_message(call.from_user.id, f'Вы выбрали {value["region_name"]}')
    else:
        logger.info('Что-то пошло не так')

    calendar, step = create_calendar(call)
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.from_user.id, f"Укажите {step} заезда", reply_markup=calendar)
    bot.set_state(call.message.chat.id, FindHotel.check_in_date)