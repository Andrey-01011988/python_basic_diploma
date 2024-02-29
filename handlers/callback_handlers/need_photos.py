from loguru import logger
from telebot.types import CallbackQuery

from loader import bot
from states.find_hotels import FindHotel


@bot.callback_query_handler(func=None, state=FindHotel.need_photos)
def get_photo(call: CallbackQuery) -> None:
    """
    Меняет состояние пользователя в зависимости от нажатой кнопки

    :param call:
    :return:
    """
    logger.info('Нужны ли фото?')
    if call.data == 'p_yes':
        logger.info(f'Пользователь {call.from_user.id} нажал Да')
        with bot.retrieve_data(call.from_user.id) as data:
            data['need_photos'] = 'yes'

        bot.send_message(call.from_user.id, 'Введите количество фото (от 1 до 10)')
        bot.set_state(call.from_user.id, FindHotel.photo_number)

    elif call.data == 'p_no':
        logger.info(f'Пользователь {call.from_user.id} нажал Нет')
        with bot.retrieve_data(call.from_user.id) as data:
            data['need_photos'] = 'no'
        bot.send_message(call.from_user.id, 'Сколько отелей показать? Введите число')
        bot.set_state(call.from_user.id, FindHotel.show_hotels)

    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
