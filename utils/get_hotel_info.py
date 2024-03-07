from typing import Dict

from loguru import logger

from site_API.site_core import url, headers_post
from site_API.site_handlers.site_api_handlers import post_hotel_info


def get_hotel_info(hotel_query: Dict, hotels_count: int) -> Dict:
    """
    Собирает необходимую информацию об отелях

    :param hotels_count: счетчик отелей
    :param hotel_query: тело запроса
    :return:
    """
    hotel_info = {}

    response = post_hotel_info('POST', url=url, headers=headers_post, payload=hotel_query,
                               timeout=100)
    logger.info(f'Сформирован запрос информации об отеле {hotels_count}')
    if response.status_code == 200:
        answer: Dict = response.json()

        hotel_info = {
            'hotel_name': answer['data']['propertyInfo']['summary']['name'],
            'address': answer['data']['propertyInfo']['summary']['location']['address']['addressLine'],
            'photos': [
                image['image']['url'] if image['__typename'] == 'PropertyImage' else image['image']['url']
                for image in answer['data']['propertyInfo']['propertyGallery']['images']
            ]
        }

    else:
        logger.info(f'Код ответа {response.status_code}')

    return hotel_info
