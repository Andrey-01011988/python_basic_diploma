from telebot.types import Message

from database.common.db_models import Users, db
from database.core import crud

from loguru import logger


update_nfo = crud.update()


@logger.catch()
def check_user(message: Message) -> bool:
    """
    Проверяет есть ли пользователь в базе данных и изменяет
    информацию о пользователе если он её поменял

    :param message: сообщение пользователя
    :return:
    """
    user_id = message.from_user.id
    data = {}
    current_user = Users.get_or_none(Users.user_id == user_id)

    if current_user:

        if str(current_user.username) != str(message.from_user.username):
            data.update({'username': message.from_user.username})

        if str(current_user.first_name) != str(message.from_user.first_name):
            data.update({'first_name': message.from_user.first_name})

        if str(current_user.last_name) != str(message.from_user.last_name):
            data.update({'last_name': message.from_user.last_name})

        if len(data) > 0:
            update_nfo(db, Users, data)
            logger.info(f'Данные пользователя изменились {data.items()}')

        return True
    else:
        return False
