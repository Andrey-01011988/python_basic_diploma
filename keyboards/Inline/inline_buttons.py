from typing import List

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def cities_buttons(city_info: List) -> InlineKeyboardMarkup:
    """
    Создает инлайн кнопки с данными из списка

    :param city_info:
    :return: markup: кнопки
    """
    keyboard_cities = InlineKeyboardMarkup()
    for value in city_info:
        keyboard_cities.add(InlineKeyboardButton(value['region_name'], callback_data=value['id']))
    return keyboard_cities
