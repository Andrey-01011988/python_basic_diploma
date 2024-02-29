from loguru import logger
from telebot.types import CallbackQuery

from keyboards.Inline.inline_buttons import yes_no_photo_button
from loader import bot
from states.find_hotels import FindHotel


@bot.callback_query_handler(func=lambda call: call.data.startswith('cb'))
def yes_no_children(call: CallbackQuery) -> None:
    """
    Принимает от пользователя ответ и в зависимости от ответа меняет состояние

    :param call: ответ пользователя
    :return: None
    """

    if call.data == 'cb_yes':
        bot.set_state(call.from_user.id, FindHotel.children_number)
        bot.send_message(call.from_user.id, 'Сколько детей с вами едет? Введите количество')
        logger.info('Пользователь ответил Да')
    elif call.data == 'cb_no':
        bot.set_state(call.from_user.id, FindHotel.need_photos)
        bot.send_message(call.from_user.id, 'Нужны ли фотографии отеля?', reply_markup=yes_no_photo_button())
        logger.info('Пользователь ответил Нет')

    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
