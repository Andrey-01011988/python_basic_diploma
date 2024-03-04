from typing import List, Dict, TypeVar

from peewee import ModelSelect

from loguru import logger

from database.common.db_models import BaseModel, db


T = TypeVar('T')


# Операция записи
@logger.catch()
def _store_data(db: db, model: T, *data: List[Dict]) -> None:
    # Защита транзакций средствами ORM:
    # Используем неделимость операций
    with db.atomic():
        # Заменил insert_many, так как из-за особенностей массовой вставки
        # каждая строка должна содержать одни и те же поля
        model.insert(*data).execute()


# Операция чтения
@logger.catch()
def _retrieve_all_data(db: db, model: T, *columns: BaseModel) -> ModelSelect:
    with db.atomic():
        response = model.select(*columns)

    return response


# Операция изменения (update) данных
@logger.catch()
def _update_data(db: db, model: T, *data: Dict) -> None:
    with db.atomic():
        model.update(*data).execute()


# Фасад
class CRUDInterface:
    @staticmethod
    def create():
        return _store_data

    @staticmethod
    def retrieve():
        return _retrieve_all_data

    @staticmethod
    def update():
        return _update_data
