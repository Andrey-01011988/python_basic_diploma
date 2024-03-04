# import json
from datetime import datetime
from random import randint
from typing import Dict

from peewee import IntegrityError
from loguru import logger
from telebot.types import Message, InputMediaPhoto

from database.common.db_models import db, Queries, Users, QueryResult
from database.core import crud
from loader import bot
from site_API.site_core import url, headers_post, default_hotel_info
from site_API.site_handlers.site_api_handlers import post_hotels, post_hotel_info

db_write = crud.create()  # Создание и запись в таблицу данных
db_read = crud.retrieve()  # Чтение из б/д


def save_n_show_info(local_payload: Dict, message: Message) -> None:
    """
    Запрашивает информацию у сервера, выдает пользователю после обработки
    (сохраняет в б/д в будущем)

    :param message:  сообщение пользователя

    :param local_payload: сформированный запрос
    :return: None
    """
    hotel_info_lst = []
    images_to_user = []
    media = []
    hotels_count = 0
    cur_query_id = 0

    response = post_hotels('POST', url=url, headers=headers_post, payload=local_payload,
                           timeout=100)
    logger.info(f'Создан запрос пользователем {message.from_user.id} на поиск отелей {message.text} штук')
    if response.status_code == 200:
        answer: Dict = response.json()

        # file_address = r'D:\SkillboxPycharm\python_basic_diploma\some_tests\hotels_from_user.json'
        # with open(file_address, 'w', encoding='utf-8') as file_w:
        #     json.dump(answer, file_w, indent=4, ensure_ascii=False)
        # logger.info('Сохранил в файл данные от сервера')

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            # Можно добавить список информации об отеле и другие списки
            data['photos_db'] = ''

        data['query_text'] += f'Запрос составлен: {datetime.now().replace(microsecond=0)}\n'

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

        while hotels_count < data['hotels_number']:
            try:
                hotel_id = answer['data']['propertySearch']['properties'][hotels_count]['id']
                hotel_query = default_hotel_info
                hotel_query['propertyId'] = hotel_id
            except Exception as e:
                logger.error(f'Ошибка {e}')
                bot.send_message(message.from_user.id, 'Произошла ошибка')
                continue

            logger.info(f'Сформирован запрос информации об отеле {hotels_count}')

            response = post_hotel_info('POST', url=url, headers=headers_post, payload=hotel_query,
                                       timeout=100)

            if response.status_code == 200:
                hotel_data = response.json()
                logger.info('Запрос успешен')
                try:
                    hotel_name = hotel_data['data']['propertyInfo']['summary']['name']
                    address = hotel_data['data']['propertyInfo']['summary']['location']['address']['addressLine']
                    price_int = \
                        answer['data']['propertySearch']['properties'][hotels_count]['price']['lead']['amount']
                    distance = \
                        answer['data']['propertySearch']['properties'][hotels_count]['destinationInfo'][
                            'distanceFromDestination']['value']
                    photos = [
                        image['image']['url'] if image['__typename'] == 'PropertyImage' else image['image']['url']
                        for image in hotel_data['data']['propertyInfo']['propertyGallery']['images']
                    ]
                except Exception as e:
                    logger.error(f'Ошибка {e}')
                    bot.send_message(message.from_user.id, 'Произошла ошибка')
                    break

                logger.info('Формируется список с данными об отелях')
                hotel_info_lst.append(
                    dict(
                        name=hotel_name,
                        address=address,
                        price_sort=price_int,
                        distance=distance,
                        photos=photos
                    )
                )

            else:
                bot.send_message(message.from_user.id, 'Что-то пошло не так')
                break

            hotels_count += 1

        # Список сортируется в зависимости от введенной команды
        if data['command'] == '/highprice':
            logger.info('Сортировка по команде /highprice')
            hotel_info_lst = sorted(hotel_info_lst, key=lambda x: x['price_sort'], reverse=True)

        elif data['command'] == '/lowprice':
            logger.info('Сортировка по команде /lowprice')
            hotel_info_lst = sorted(hotel_info_lst, key=lambda x: x['price_sort'])

        # Формируется ответ пользователю
        if data['need_photos'] == 'no':
            for query_answer in hotel_info_lst:
                msg = f'Отель: {query_answer["name"]}\n' \
                      f'Адрес: {query_answer["address"]}\n' \
                      f'Цена за ночь: ${str(round(query_answer["price_sort"]))}\n' \
                      f'Расстояние от центра (в милях):{str(query_answer["distance"])}'

                try:
                    if cur_query_id == 0:
                        logger.info('Не записался ID запроса')
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
            for answer in hotel_info_lst:

                msg = f'Отель: {answer["name"]}\n' \
                      f'Адрес: {answer["address"]}\n' \
                      f'Цена за ночь: ${str(round(answer["price_sort"]))}\n' \
                      f'Расстояние от центра (в милях):{str(answer["distance"])}'
                for image_link in range(data['photo_num']):
                    images_to_user.append(answer['photos'][randint(0, len(answer['photos']) - 1)])

                for index, link in enumerate(images_to_user):
                    if index == 0:
                        media.append(InputMediaPhoto(media=link, caption=msg))
                    else:
                        media.append(InputMediaPhoto(media=link))
                    data['photos_db'] += link + ';'

                if cur_query_id < 0:
                    logger.info('Не записался ID запроса')
                query_res = [
                    {
                        'query': cur_query_id,
                        'result_text': msg,
                        'photos': data['photos_db']
                    }
                ]
                db_write(db, QueryResult, query_res)
                logger.info('Сохранение в б/д информации о результате запроса успешно!')
                data['photos_db'] = ''
                logger.info('Очищена строка ссылок на фотографии')

                bot.send_media_group(message.chat.id, media)
                logger.info('Сообщение отправлено')
                images_to_user.clear()
                media.clear()

    else:
        logger.info(f'Код ответа {response.status_code}')
        bot.send_message(message.from_user.id, 'Что-то пошло не так')
