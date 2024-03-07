from typing import Dict, List

from loguru import logger
from telebot.types import Message

from site_API.site_core import url, headers_post
from site_API.site_handlers.site_api_handlers import post_hotels


def get_hotels_info(local_payload: Dict, message: Message) -> List:
    """
    Собирает необходимую информацию об отелях

    :param local_payload: тело запроса
    :param message: сообщение пользователя
    :return:
    """
    hotels_info = []

    response = post_hotels('POST', url=url, headers=headers_post, payload=local_payload,
                           timeout=100)
    logger.info(f'Создан запрос пользователем {message.from_user.id} на поиск отелей {message.text} штук')
    if response.status_code == 200:
        answer: Dict = response.json()
        for value in answer['data']['propertySearch']['properties']:
            hotels_info.append(
                dict(
                    hotel_id=value['id'],
                    distance_from_center=value['destinationInfo']['distanceFromDestination']['value'],
                    price_int=value['price']['lead']['amount']
                )
            )
    else:
        logger.info(f'Код ответа {response.status_code}')

    return hotels_info
