import requests
from typing import Dict, List
from requests import Response


def _make_response(method: str, url: str, headers: Dict, params: Dict,
                   timeout: int) -> Response:
    """
    Запрос у сервера данных  по сформированному url
    :param method: метод запроса
    :param url: адрес страницы
    :param headers: пользовательские заголовки
    :param params: запросы
    :param timeout: задержка
    :return: response: ответ от сервера
    """
    response = requests.request(
        method,
        url,
        params=params,
        headers=headers,
        timeout=timeout,
    )

    return response


def get_city(method: str, url: str, headers: Dict, city: str,
             timeout: int, func=_make_response) -> Response:
    """
    Запрашивает у сервера факт о дате по сформированному адресу

    """

    url_city = '{}/locations/v3/search'.format(url)

    local_params = {"q": city, "locale": "ru_RU"}

    response_get_city = func(method, url_city, headers=headers, params=local_params,
                             timeout=timeout)

    return response_get_city


def get_hotels(method: str, url: str, headers: Dict, checkindate: Dict, checkoutdate: Dict,
               rooms: List, price: Dict, timeout: int, func=_make_response) -> Response:
    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {"regionId": "6054439"},
        "checkInDate": {},
        "checkOutDate": {},
        "rooms": [],
        "resultsStartingIndex": 0,
        "resultsSize": 200,
        "sort": "PRICE_LOW_TO_HIGH",
        "filters": {
        }
    }
    payload['checkInDate'].update(checkindate)
    payload['checkOutDate'].update(checkoutdate)
    payload["rooms"].extend(rooms)
    payload['filters'].update(price)

    response_hotels = func(method, url, params=payload, headers=headers, timeout=timeout)

    return response_hotels


checkInDate = {
    "day": 10,
    "month": 10,
    "year": 2022
}

checkOutDate = {
    "day": 15,
    "month": 10,
    "year": 2022
}

rooms_ = [
    {
        "adults": 2,
        "children": [{"age": 5}, {"age": 7}]
    }
]

price_ = {
    "max": 150,
    "min": 100
}
