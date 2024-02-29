from datetime import datetime
# from pprint import pprint
from typing import List

import requests
from loguru import logger
from telebot.types import Message

from keyboards.Inline.inline_buttons import cities_buttons
from site_API.site_core import headers_get, url
from site_API.site_handlers.site_api_handlers import get_city
from states.find_hotels import FindHotel
from loader import bot


def check_command(command: str) -> str:
    """
      Проверка команды и назначение параметра сортировки

      : param command : str команда, выбранная (введенная) пользователем
      : return : str команда сортировки
    """
    if command == '/bestdeal':
        return 'DISTANCE'
    elif command == '/lowprice':
        return 'PRICE_LOW_TO_HIGH'
    elif command == '/highprice':
        return 'PRICE_RELEVANT '


def get_cities_list(response_sr: List) -> List:
    """
    Из списка данных выбирает необходимые для обработки данные

    :param response_sr: список данных

    :return: city_info: словарь с данными о городах
    """
    city_info = []
    for string in response_sr:
        if string['type'] in ('CITY', 'NEIGHBORHOOD'):
            city_info.append(
                dict(
                    id=string['gaiaId'],
                    region_name=string['regionNames']['fullName']
                )
            )

    return city_info


@bot.message_handler(commands=['lowprice', 'highprice', 'bestdeal'])
def low_high_best_handler(message: Message) -> None:
    """
    Обработчик команд, срабатывает на три команды /lowprice, /highprice, /bestdeal
    и запоминает необходимые данные. Спрашивает пользователя - какой искать город.
    : param message : Message
    : return : None
    """
    bot.set_state(message.from_user.id, FindHotel.command)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        logger.info('Запоминаем выбранную команду: ' + message.text + f" User_id: {message.chat.id}")
        data['command'] = message.text
        data['sort'] = check_command(message.text)
        data['date_time'] = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        data['chat_id'] = message.chat.id
    bot.set_state(message.from_user.id, FindHotel.select_city, message.chat.id)
    bot.send_message(message.from_user.id, 'Введите город, в котором хотите найти отели')


@bot.message_handler(state=FindHotel.select_city)
def select_city(message: Message) -> None:
    """
    Сохраняет введенный пользователем город и выводит варианты локаций
    инлайн клавиатурой

    :param message: название города

    :return: None
    """

    response = get_city('GET', url=url, headers=headers_get, city=message.text, timeout=10)
    logger.info(f'Создан запрос пользователем {message.from_user.id} на поиск городов {message.text}')
    if response.status_code == requests.codes.ok:
        answer = response.json()

        cities = (get_cities_list(answer['sr']))
        if len(cities) == 0:
            bot. send_message(message.from_user.id, 'По вашему запросу ни чего не найдено, введите другой запрос')
        else:
            with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data['cities'] = cities
            bot.send_message(message.from_user.id, 'Уточните расположение',
                             reply_markup=cities_buttons(cities))
