from loader import bot
from telebot.types import CallbackQuery
from loguru import logger
from states.find_hotels import FindHotel
from utils.calendar import create_calendar
from handlers.custom_handlers.get_city_handler import cities


@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def save_n_continue(call: CallbackQuery) -> None:
    """
    Сохраняет id города и (в будущем) меняет состояние пользователя

    :param call: id города
    :return:None
    """
    logger.info(f'Пользователь выбрал город')
    print('call.message.chat.id', call.message.chat.id)  # Совпадает с id пользователя
    if call.data:
        with bot.retrieve_data(call.message.chat.id) as data:
            data['destination_id'] = call.data
        city_name = None
        for city in cities:
            if city['id'] == data['destination_id']:
                city_name = city["region_name"]

        bot.send_message(call.from_user.id, f'Вы выбрали {city_name}')
        calendar, step = create_calendar(call)
        bot.answer_callback_query(call.id)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.from_user.id, f"Укажите {step} заезда", reply_markup=calendar)
        bot.set_state(call.message.chat.id, FindHotel.check_in_date)
