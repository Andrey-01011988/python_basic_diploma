# import json
# from pprint import pprint

# import requests
# from typing import List

from loguru import logger
from telebot.types import Message

from loader import bot
from site_API.site_core import default_hotels_payload
from states.find_hotels import FindHotel
from utils.save_n_show_info import save_n_show_info
from utils.save_n_show_info_bestdeal import save_n_show_info_bestdeal


@bot.message_handler(state=FindHotel.show_hotels)
def hotels_number(message: Message) -> None:
    """
    Запоминает введенное пользователем количество отелей и выводит результат запросов пользователю

    :param message: количество отелей
    :return: None
    """

    if message.text.isdigit():
        logger.info('Сообщение содержит цифру')
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['hotels_number'] = int(message.text)
            logger.info('Сохранил количество отелей')
        # with open(r'D:\SkillboxPycharm\python_basic_diploma\some_tests\data.json', 'w', encoding='utf-8') as file_w:
        #     json.dump(data, file_w, sort_keys=True, indent=4, ensure_ascii=False)
        logger.info('Сохранил информацию от пользователя в файл data')
        bot.send_message(message.from_user.id, 'Жду ответа от сервера')
    else:
        bot.send_message(message.from_user.id, 'Введите целое число')

    if data['command'] in ('/lowprice', '/highprice'):
        local_payload = default_hotels_payload
        local_payload['destination']['regionId'] = data['destination_id']
        local_payload['checkInDate'] = data['check_in']
        local_payload['checkOutDate'] = data['check_out']
        local_payload['rooms'] = data['rooms']
        local_payload['resultsSize'] = data['hotels_number']
        local_payload['sort'] = data['sort']
        local_payload['filters'].clear()

        logger.info('Сформировано тело запроса lowprice highprice')

        save_n_show_info(local_payload=local_payload, message=message)

    elif data['command'] == '/bestdeal':
        local_payload = default_hotels_payload
        local_payload['destination']['regionId'] = data['destination_id']
        local_payload['checkInDate'] = data['check_in']
        local_payload['checkOutDate'] = data['check_out']
        local_payload['rooms'] = data['rooms']
        local_payload['resultsSize'] = 50
        local_payload['sort'] = data['sort']
        local_payload['filters']['price'] = data['price']

        logger.info('Сформировано тело запроса bestdeal')

        save_n_show_info_bestdeal(local_payload=local_payload, message=message)

    else:
        bot.send_message(message.from_user.id, 'Не та команда')
        return
