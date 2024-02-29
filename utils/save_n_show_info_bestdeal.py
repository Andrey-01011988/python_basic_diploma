# import json
from random import randint
from typing import Dict

from loguru import logger
from telebot.types import Message, InputMediaPhoto

from loader import bot
from site_API.site_core import url, headers_post, default_hotel_info
from site_API.site_handlers.site_api_handlers import post_hotels, post_hotel_info
from states.find_hotels import FindHotel


def save_n_show_info_bestdeal(local_payload: Dict, message: Message) -> None:
    """
    Запрашивает информацию у сервера, выдает пользователю после обработки
    (сохраняет в б/д в будущем) для команды /bestdeal

    :param message: сообщение пользователя

    :param local_payload: сформированный запрос
    :return: None
    """
    hotels_info_lst_bestdeal = []  # список необходимой информации об отелях из ответа сервера
    images_to_user = []  # список ссылок на фото отеля для пользователя
    media = []  # список изображений для пользователя с подписью
    hotels_count = 0  # счетчик отелей выводимых пользователю

    response = post_hotels('POST', url=url, headers=headers_post, payload=local_payload,
                           timeout=100)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['hotels_bestdeal'] = []
        data['show_info'] = []

    logger.info(f'Создан запрос пользователем {message.from_user.id} на поиск отелей {message.text} штук')
    if response.status_code == 200:
        answer = response.json()
        # file_address = r'D:\SkillboxPycharm\python_basic_diploma\some_tests\hotels_from_user_bestdeal.json'
        # with open(file_address, 'w', encoding='utf-8') as file_w:
        #     json.dump(answer, file_w, indent=4, ensure_ascii=False)
        # logger.info('Сохранил в файл данные от сервера')

        logger.info('Сортировка по команде /bestdeal')
        for value in answer['data']['propertySearch']['properties']:
            hotels_info_lst_bestdeal.append(
                dict(
                    hotel_id=value['id'],
                    distance_from_center=value['destinationInfo']['distanceFromDestination']['value'],
                    price_int=value['price']['lead']['amount']
                )
            )

        # Спорно!!!
        del answer

        logger.info('Сортировка по расстоянию от центра введенного пользователем')
        for hotel in hotels_info_lst_bestdeal:
            if data['distance']['min'] <= hotel['distance_from_center'] <= data['distance']['max']:
                data['hotels_bestdeal'].append(hotel)

        logger.info('Проверка на длину списка')
        if len(data['hotels_bestdeal']) < data['hotels_number']:
            logger.error('Проверка не пройдена, пользователь возвращен на шаг ввода дистанции')
            bot.send_message(message.from_user.id,
                             'По таким параметрам нет подходящих отелей, попробуйте изменить дистанцию')
            bot.set_state(message.from_user.id, FindHotel.distance_min)
            return

        logger.info('Сортировка по порядку возрастания')
        data['hotels_bestdeal'] = sorted(data['hotels_bestdeal'], key=lambda x: x['distance_from_center'])

        while hotels_count < data['hotels_number']:
            try:
                hotel_id = data['hotels_bestdeal'][hotels_count]['hotel_id']
                hotel_query = default_hotel_info
                hotel_query['propertyId'] = hotel_id
            except Exception as e:
                logger.error(f'Ошибка {e}')
                bot.send_message(message.from_user.id, 'Произошла ошибка')
                break

            logger.info(f'Сформирован запрос информации об отеле {hotels_count}')

            response = post_hotel_info('POST', url=url, headers=headers_post, payload=hotel_query,
                                       timeout=100)

            if response.status_code == 200:
                hotel_data = response.json()
                logger.info('Запрос успешен')

                try:
                    hotel_name = hotel_data['data']['propertyInfo']['summary']['name']
                    address = hotel_data['data']['propertyInfo']['summary']['location']['address']['addressLine']
                    price_int = data['hotels_bestdeal'][hotels_count]['price_int']
                    distance = data['hotels_bestdeal'][hotels_count]['distance_from_center']
                    photos = [
                        image['image']['url']
                        for image in hotel_data['data']['propertyInfo']['propertyGallery']['images']
                    ]
                except Exception as e:
                    logger.error(f'Ошибка {e}')
                    bot.send_message(message.from_user.id, 'Произошла ошибка')
                    break

                logger.info('Формируется список с данными об отелях')
                data['show_info'].append(
                    dict(
                        name=hotel_name,
                        address=address,
                        price_sort=price_int,
                        distance=distance,
                        photos=photos
                    )
                )

            else:
                logger.error(f'Код ошибки {response.status_code}')
                bot.send_message(message.from_user.id, 'Что-то пошло не так')
                break

            hotels_count += 1

        # Формируется ответ пользователю
        if data['need_photos'] == 'no':
            for query_answer in data['show_info']:
                msg = f'Отель: {query_answer["name"]}\n' \
                      f'Адрес: {query_answer["address"]}\n' \
                      f'Цена за ночь: ${str(round(query_answer["price_sort"]))}\n' \
                      f'Расстояние от центра (в милях):{str(query_answer["distance"])}'
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

                bot.send_media_group(message.chat.id, media)
                logger.info('Сообщение отправлено')
                images_to_user.clear()
                media.clear()

    else:
        logger.info(f'Код ответа {response.status_code}')
        bot.send_message(message.from_user.id, 'Что-то пошло не так')