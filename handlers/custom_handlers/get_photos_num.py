from loguru import logger
from telebot.types import Message

from loader import bot
from states.find_hotels import FindHotel


@bot.message_handler(state=FindHotel.photo_number)
def get_photo_num(message: Message) -> None:
    """
    Принимает от пользователя количество фотографий и сохраняет значение

    :param message: кол-во фото
    :return: None
    """
    if message.text.isdigit() and 0 < int(message.text) < 11:
        with bot.retrieve_data(message.from_user.id) as data:
            data['photo_num'] = int(message.text)
            data['query_text'] += f'Количество фотографий: {message.text}\n'
            logger.info('Сохранил количество фото для записи в б/д')
        logger.info('Сохранено количество фотографий')
        if data['command'] == '/bestdeal':
            bot.send_message(message.from_user.id, 'Введите минимальную цену за ночь для поиска отелей')
            logger.info(f'Пользователь {message.from_user.id} вводит минимальную цену')
            bot.set_state(message.from_user.id, FindHotel.price_min)
        elif data['command'] in ('/lowprice', '/highprice'):
            bot.send_message(message.from_user.id, 'Сколько отелей показать? Введите число')
            logger.info(f'Пользователь {message.from_user.id} вводит количество отелей')
            bot.set_state(message.from_user.id, FindHotel.show_hotels)
        else:
            logger.error('Команды пользователя нет в списке')
            bot.send_message(message.from_user.id, 'Команда пользователя не определена')
    else:
        bot.send_message(message.from_user.id, 'Введите целое число от 1 до 10')
