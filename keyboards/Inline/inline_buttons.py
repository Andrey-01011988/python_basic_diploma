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
        id_prefix = 'q' + value['id']
        keyboard_cities.add(InlineKeyboardButton(value['region_name'], callback_data=id_prefix))
    return keyboard_cities


def yes_no_children_button() -> InlineKeyboardMarkup:
    """
    Создает инлайн кнопки Да/Нет для детей (размещаются под сообщением)

    :return: InlineKeyboardMarkup
    """
    markup = InlineKeyboardMarkup()
    markup.row_width = 2  # количество кнопок под строкой
    markup.add(InlineKeyboardButton('Да', callback_data='cb_yes'),
               InlineKeyboardButton('Нет', callback_data='cb_no'))
    return markup


def yes_no_photo_button() -> InlineKeyboardMarkup:
    """
    Создает инлайн кнопки Да/Нет для фото (размещаются под сообщением)

    :return: InlineKeyboardMarkup
    """
    markup = InlineKeyboardMarkup()
    markup.row_width = 2  # количество кнопок под строкой
    markup.add(InlineKeyboardButton('Да', callback_data='p_yes'),
               InlineKeyboardButton('Нет', callback_data='p_no'))
    return markup
