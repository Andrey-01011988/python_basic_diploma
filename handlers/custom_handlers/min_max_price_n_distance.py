from loguru import logger
from telebot.types import Message

from loader import bot
from states.find_hotels import FindHotel


@bot.message_handler(state=FindHotel.price_min)
def min_price(message: Message) -> None:
    """
    Сохраняет минимальное значение цены

    :param message: мин цена
    :return: None
    """
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id) as data:
            data['price'] = {}
            data['price']['min'] = int(message.text)
            data['query_text'] += f'Минимальная цена: {message.text}\n'
            logger.info('Сохранил Минимальная цена для записи в б/д')
        bot.send_message(message.from_user.id, 'Введите максимальную цену за ночь для поиска отелей')
        logger.info(f'Пользователь {message.from_user.id} вводит максимальную цену')
        bot.set_state(message.from_user.id, FindHotel.price_max)
    else:
        bot.send_message(message.from_user.id, 'Введите целое число')


@bot.message_handler(state=FindHotel.price_max)
def max_price(message: Message) -> None:
    """
    Сохраняет максимальную цену

    :param message: макс цена
    :return: None
    """
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id) as data:
            data['price']['max'] = int(message.text)
            data['query_text'] += f'Максимальная цена: {message.text}\n'
            logger.info('Сохранил Максимальная цена для записи в б/д')
        if data['price']['max'] <= data['price']['min']:
            logger.error('Сработала проверка мин макс цены')
            bot.send_message(message.from_user.id, 'Максимальная цена меньше или равна минимальной, попробуйте еще раз')
            bot.send_message(message.from_user.id, 'Введите минимальную цену за ночь для поиска отелей')
            bot.set_state(message.from_user.id, FindHotel.price_min)
        else:
            bot.send_message(message.from_user.id, 'Введите минимальное расстояние от центра (в милях)')
            logger.info(f'Пользователь {message.from_user.id} вводит минимальную дистанцию')
            bot.set_state(message.from_user.id, FindHotel.distance_min)

    else:
        bot.send_message(message.from_user.id, 'Введите целое число')


@bot.message_handler(state=FindHotel.distance_min)
def min_distance(message: Message) -> None:
    """
    Сохраняет минимальную дистанцию

    :param message: минимальная дистанция
    :return: None
    """
    logger.info('Запустилась обработка ввода минимальной дистанции пользователем')
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id) as data:
            data['distance'] = {}
            data['distance']['min'] = int(message.text)
        bot.send_message(message.from_user.id, 'Введите максимальное расстояние от центра (в милях)')
        logger.info(f'Пользователь {message.from_user.id} вводит максимальную дистанцию')
        bot.set_state(message.from_user.id, FindHotel.distance_max)
    else:
        bot.send_message(message.from_user.id, 'Введите целое число')


@bot.message_handler(state=FindHotel.distance_max)
def max_distance(message: Message) -> None:
    """
    Сохраняет максимальную дистанцию

    :param message: макс дистанция
    :return: None
    """
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id) as data:
            data['distance']['max'] = int(message.text)
        if data['distance']['max'] <= data['distance']['min']:
            logger.error('Сработала проверка мин макс дистанции')
            bot.send_message(message.from_user.id, 'Максимальная цена меньше или равна минимальной, попробуйте еще раз')
            bot.send_message(message.from_user.id, 'Введите минимальное расстояние от центра (в милях)')
            logger.info(f'Пользователь {message.from_user.id} вводит минимальную дистанцию')
            bot.set_state(message.from_user.id, FindHotel.distance_min)
        else:
            bot.send_message(message.from_user.id, 'Сколько отелей показать? Введите число')
            logger.info(f'Пользователь {message.from_user.id} вводит количество отелей')
            bot.set_state(message.from_user.id, FindHotel.show_hotels_bestdeal)
    else:
        bot.send_message(message.from_user.id, 'Введите целое число')
