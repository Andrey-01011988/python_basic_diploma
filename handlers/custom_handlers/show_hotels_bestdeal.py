from datetime import datetime
from random import randint

from loguru import logger
from peewee import IntegrityError
from telebot.types import Message, InputMediaPhoto

from database.common.db_models import db, Queries, Users, QueryResult
from database.core import crud
from loader import bot
from site_API.site_core import default_hotels_payload, default_hotel_info
from states.find_hotels import FindHotel
from utils.get_hotel_info import get_hotel_info
from utils.get_hotels_info import get_hotels_info


db_write = crud.create()  # Создание и запись в таблицу данных


@bot.message_handler(state=FindHotel.show_hotels_bestdeal)
def hotels_info_bestdeal(message: Message) -> None:
    """
    Запоминает введенное пользователем количество отелей,
    по собранной от пользователя информации направляет запрос серверу
    и выдает пользователю сформированный ответ, для команд /bestdeal

    :param message: количество отелей
    :return: None
    """

    hotels_count = 0  # счетчик отелей выводимых пользователю
    cur_query_id = 0  # Проверка на извлечение id запроса
    images_to_user = []  # список ссылок на фото отеля для пользователя
    media = []  # список изображений для пользователя с подписью

    if message.text.isdigit():
        logger.info('Сообщение содержит цифру')
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['hotels_number'] = int(message.text)
            logger.info('Сохранил количество отелей')
            data['hotels_bestdeal'] = []  # список информации об отелях после сортировки
            data['show_info'] = []  # список информации об отелях для записи в б/д и показа пользователю
            data['photos_db'] = ''  # строка для записи ссылок на фотографии в б/д
            data['query_text'] += f'Количество отелей: {message.text}\n'
            logger.info('Сохранил количество отелей для записи в б/д')

        bot.send_message(message.from_user.id, 'Жду ответа от сервера')
    else:
        bot.send_message(message.from_user.id, 'Введите целое число')
        return

    local_payload = default_hotels_payload
    local_payload['destination']['regionId'] = data['destination_id']
    local_payload['checkInDate'] = data['check_in']
    local_payload['checkOutDate'] = data['check_out']
    local_payload['rooms'] = data['rooms']
    local_payload['resultsSize'] = 50
    local_payload['sort'] = data['sort']
    local_payload['filters']['price'] = data['price']

    logger.info('Сформировано тело запроса bestdeal')

    hotels_info = get_hotels_info(local_payload, message)

    if len(hotels_info) > 0:
        data['query_text'] += f'Минимальная дистанция до центра: {data["distance"]["min"]}\n'
        data['query_text'] += f'Максимальная дистанция до центра: {data["distance"]["max"]}\n'
        data['query_text'] += f'Запрос составлен: {datetime.now().replace(microsecond=0)}\n'

        logger.info('Сортировка по расстоянию от центра введенного пользователем')
        for hotel in hotels_info:
            if data['distance']['min'] <= hotel['distance_from_center'] <= data['distance']['max']:
                data['hotels_bestdeal'].append(hotel)

        logger.info('Проверка на длину списка')
        if len(data['hotels_bestdeal']) < data['hotels_number']:
            logger.error('Проверка не пройдена, пользователь возвращен на шаг ввода дистанции')
            data['hotels_bestdeal'].clear()
            logger.info('Очищен список')
            bot.send_message(message.from_user.id,
                             'По таким параметрам нет подходящих отелей, попробуйте изменить дистанцию')
            bot.send_message(message.from_user.id, 'Введите минимальную дистанцию от центра (в милях)')
            bot.set_state(message.from_user.id, FindHotel.distance_min)
            return
        else:
            logger.info('Проверка на список пройдена')

            logger.info('Сортировка по порядку возрастания дистанции')
            data['hotels_bestdeal'] = sorted(data['hotels_bestdeal'], key=lambda x: x['distance_from_center'])

        while hotels_count < data['hotels_number']:

            hotel_id = data['hotels_bestdeal'][hotels_count]['hotel_id']
            hotel_query = default_hotel_info
            hotel_query['propertyId'] = hotel_id

            logger.info(f'Сформирован запрос информации об отеле {hotels_count}')

            hotel_info = get_hotel_info(hotel_query, hotels_count)

            if len(hotel_info) > 0:

                logger.info('Формируется список с данными об отелях')
                data['show_info'].append(
                    dict(
                        name=hotel_info['hotel_name'],
                        address=hotel_info['address'],
                        price_sort=data['hotels_bestdeal'][hotels_count]['price_int'],
                        distance=data['hotels_bestdeal'][hotels_count]['distance_from_center'],
                        photos=hotel_info['photos']
                    )
                )
                hotels_count += 1
            else:
                bot.send_message(message.from_user.id, 'Произошла ошибка, выберите в меню другую функцию (/help)')
                logger.error('Ошибка: пустой ответ')
                return

        req_info = [
            {
                'user': message.from_user.id,
                'query_date': datetime.now().replace(microsecond=0),
                'query_text': data['query_text']
            }
        ]
        db_write(db, Queries, req_info)
        logger.info('Сохранение в б/д информации о запросе успешно!')

        try:
            cur_user = Users.get(Users.user_id == message.from_user.id)
            cur_query_lst = cur_user.queries.order_by(-Queries.query_date, -Queries.query_id).limit(1)
            cur_query_id = cur_query_lst[0].query_id
            logger.info('Извлечение ID запроса успешно')
        except IntegrityError as e:
            logger.error(f'Произошла ошибка {e}')

        # Формируется ответ пользователю
        if data['need_photos'] == 'no':
            for query_answer in data['show_info']:
                msg = f'Отель: {query_answer["name"]}\n' \
                      f'Адрес: {query_answer["address"]}\n' \
                      f'Цена за ночь: ${str(round(query_answer["price_sort"]))}\n' \
                      f'Расстояние от центра (в милях):{str(query_answer["distance"])}'

                try:
                    query_res = [
                        {
                            'query': cur_query_id,
                            'result_text': msg
                        }
                    ]
                    db_write(db, QueryResult, query_res)
                    logger.info('Сохранение в б/д информации о результате запроса успешно!')
                except IntegrityError as e:
                    logger.error(f'Ошибка {e}')

                bot.send_message(message.from_user.id, msg)
                logger.info('Сообщение отправлено')

        elif data['need_photos'] == 'yes':
            for query_answer in data['show_info']:
                msg = f'Отель: {query_answer["name"]}\n' \
                      f'Адрес: {query_answer["address"]}\n' \
                      f'Цена за ночь: ${str(round(query_answer["price_sort"]))}\n' \
                      f'Расстояние от центра (в милях):{str(query_answer["distance"])}'
                for image_link in range(data['photo_num']):
                    images_to_user.append(query_answer['photos'][randint(0, len(query_answer['photos']) - 1)])
                for index, link in enumerate(images_to_user):
                    if index == 0:
                        media.append(InputMediaPhoto(media=link, caption=msg))
                    else:
                        media.append(InputMediaPhoto(media=link))
                    data['photos_db'] += link + ';'

                try:
                    query_res = [
                        {
                            'query': cur_query_id,
                            'result_text': msg,
                            'photos': data['photos_db']
                        }
                    ]
                    db_write(db, QueryResult, query_res)
                    logger.info('Сохранение в б/д информации о результате запроса успешно!')
                except IntegrityError as e:
                    logger.error(f'Ошибка {e}')

                data['photos_db'] = ''

                bot.send_media_group(message.chat.id, media)
                logger.info('Сообщение отправлено')
                images_to_user.clear()
                media.clear()

        bot.delete_state(message.from_user.id)
        bot.send_message(message.from_user.id, 'Если хотите продолжить, введите /help для выбора необходимой опции')

    else:
        bot.send_message(message.from_user.id, 'Произошла ошибка')
        logger.error('Ошибка: пустой ответ')
        return
