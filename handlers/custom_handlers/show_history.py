from loguru import logger
from telebot.types import Message

from database.common.db_models import Users, Queries
from database.core import crud
from keyboards.Inline.inline_buttons import results_button
from loader import bot


read_db = crud.retrieve()


@bot.message_handler(commands=['history'])
def show_queries(message: Message) -> None:
    """
    Показывает пользователю историю запросов (последние 10)

    :param message:
    :return:
    """
    cur_user = Users.get_or_none(Users.user_id == message.from_user.id)
    if cur_user:
        logger.info(f'Пользователь {cur_user} сделал запрос истории')
        cur_user_queries = cur_user.queries.order_by(-Queries.query_date).limit(5)
        for query in cur_user_queries:
            query_id = query.query_id
            text = query.query_text
            if text:
                bot.send_message(message.from_user.id, text, reply_markup=results_button(query_id))
                logger.info(f'Отправлен текст запроса №{query_id}')

            else:
                bot.send_message('Запросов пока нет, создайте свой запрос выбрав команду из меню /help')
    else:
        bot.send_message(message.from_user.id,
                         'Пройдите авторизацию (введите /start) и создайте свой первый запрос')
