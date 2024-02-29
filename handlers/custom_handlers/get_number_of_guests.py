from loguru import logger
from telebot.types import Message

from keyboards.Inline.inline_buttons import yes_no_children_button, yes_no_photo_button
from loader import bot
from states.find_hotels import FindHotel


@bot.message_handler(state=FindHotel.adult_guests)
def get_adults(message: Message) -> None:
    """
    Записывает введенное пользователем число взрослых гостей,
    запрашивает есть ли дети

    :param message:
    :return:
    """
    logger.info(f'Получил от пользователя {message.from_user.id} число взрослых')
    if message.text.isdigit():
        guests = {'adults': int(message.text)}
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['rooms'] = list()
            data['rooms'].append(guests)
            logger.info('Сохранил в словарь')
        logger.info('Запрос у пользователя детей')
        bot.send_message(message.from_user.id, 'С вами едут дети?', reply_markup=yes_no_children_button())
    else:
        bot.send_message(message.from_user.id, 'Введите целое число, пожалуйста')


@bot.message_handler(state=FindHotel.children_number)
def get_children_number(message: Message) -> None:
    """
    Принимает и сохраняет количество детей

    :param message: количество детей
    :return: None
    """
    logger.info(f'Получил от пользователя {message.from_user.id} число детей')
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['children_number'] = int(message.text)
        logger.info('Сохранил число')
        bot.set_state(message.from_user.id, FindHotel.children_age)
        bot.send_message(message.from_user.id,
                         'Введите возраст детей целыми числами через запятую (если необходимо)')
    else:
        bot.send_message('Введите целое число')


@bot.message_handler(state=FindHotel.children_age)
def get_children_age(message: Message) -> None:
    """
    Запрашивает возраст детей через запятую и сохраняет

    :param message: возраст детей через запятую

    :return:
    """
    logger.info(f'Получил от пользователя {message.from_user.id} возраст детей')
    age = message.text.split(', ')
    for num in age:
        if not num.isdigit():
            bot.send_message(message.from_user.id,
                             'Введите возраст детей целыми числами через запятую с пробелом (если необходимо)')
            logger.error(f'Сработала проверка {num}')
            break
    logger.info('Проверка пройдена')
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        if len(age) != data['children_number']:
            bot.send_message(message.from_user.id,
                             'Количество детей и введенный возраст не соответствуют друг другу, попробуйте ещё раз')
            bot.set_state(message.from_user.id, FindHotel.children_number)
            logger.error('Количество и возраст не совпали')
            return
        else:
            data['rooms'][0]['children'] = list()
            for number in age:
                data['rooms'][0]['children'].append(
                    dict(
                        age=int(number)
                    )
                )
            logger.info('Сохранил данные')
    bot.send_message(message.from_user.id, 'Нужны ли фотографии отеля?', reply_markup=yes_no_photo_button())
    bot.set_state(message.from_user.id, FindHotel.need_photos)