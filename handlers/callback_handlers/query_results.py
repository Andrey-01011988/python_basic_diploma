from loguru import logger
from telebot.types import CallbackQuery, InputMediaPhoto

from database.common.db_models import Queries
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def show_results(call: CallbackQuery) -> None:
    """
    Выводит результаты запроса

    :param call:
    :return:
    """
    media = []
    if call.data:

        bot.answer_callback_query(call.id, 'Результаты запроса представлены ниже')
        bot.delete_message(call.message.chat.id, call.message.message_id)

        cur_query = Queries.get_or_none(Queries.query_id == call.data)
        query_results = cur_query.result
        query_text: str = cur_query.query_text

        bot.send_message(call.from_user.id, query_text)

        switcher_yes = 'Фото отеля: Да'
        switcher_no = 'Фото отеля: Нет'
        if switcher_yes in query_text:
            for result in query_results:
                text = result.result_text
                logger.info('Создается список фотографий для каждого отеля')
                photos = [photo.strip() for photo in result.photos.split(';') if len(photo) > 0]
                for index, link in enumerate(photos):
                    if index == 0:
                        media.append(InputMediaPhoto(media=link, caption=text))
                    else:
                        media.append(InputMediaPhoto(media=link))
                logger.info(f'Для ответа {result.result_id} создан пул фотографий')
                bot.send_media_group(call.from_user.id, media)
                logger.info(f'Отправлен пул медиа результата {result.result_id}')
                media.clear()
                logger.info('Очищен пул фотографий')

        elif switcher_no in query_text:
            for result in query_results:
                text = result.result_text
                bot.send_message(call.from_user.id, text)

        else:
            bot.send_message(call.from_user.id, 'Что-то пошло не так')
            logger.error('Не корректно записались условия вывода фотографий')

    else:
        bot.send_message(call.from_user.id, 'Запросов нет')
        logger.error('Не передался id запроса')
