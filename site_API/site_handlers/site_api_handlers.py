import requests
from typing import Dict
from requests import Response


def _make_response(method: str, url: str, headers: Dict, params: Dict,
                   timeout: int) -> Response:
    """
    Запрос у сервера данных  по сформированному url годится только для get в данном случае
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
    Запрашивает у сервера город по сформированному адресу

    """

    url_city = '{}/locations/v3/search'.format(url)

    local_params = {"q": city, "locale": "ru_RU"}

    response_get_city = func(method, url_city, headers=headers, params=local_params,
                             timeout=timeout)

    return response_get_city


def post_hotels(method: str, url: str, headers: Dict, payload: Dict, timeout: int) -> Response:
    """
    Запрашивает у сервера отели по сформированному запросу

    :param method: метод запроса
    :param url: адрес запроса
    :param headers: заголовки
    :param payload: тело запроса
    :param timeout: время ожидания

    :return: Response
    """

    hotels_url = '{}/properties/v2/list'.format(url)

    response_hotels = requests.request(method, hotels_url, json=payload, headers=headers, timeout=timeout)

    return response_hotels


def post_hotel_info(method: str, url: str, headers: Dict, payload: Dict, timeout: int) -> Response:
    """
    Запрашивает у сервера информацию по отелю

    :param timeout:
    :param method: метод запроса
    :param url: адрес запроса
    :param headers: заголовки
    :param payload: тело запроса
    :return: Response
    """

    hotel_info_url = '{}/properties/v2/detail'.format(url)

    response_hotel_info = requests.request(method, hotel_info_url, json=payload, headers=headers, timeout=timeout)

    return response_hotel_info
