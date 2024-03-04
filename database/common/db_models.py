from datetime import datetime

import peewee

db = peewee.SqliteDatabase('users_history.db')


# Базовая модель
class BaseModel(peewee.Model):
    created_at = peewee.DateField(default=datetime.now())

    class Meta:
        database = db


class Users(BaseModel):
    """
    Модель пользователя

    user_id: первичный ключ модели, будет совпадать с Telegram ID.
    Это значит, что он будет уникальным для всей таблицы

    username: никнейм в Telegram. Может быть не указан

    first_name: имя в Telegram. Может быть не указано

    last_name: фамилия в Telegram. Может быть не указана
    """
    user_id = peewee.IntegerField(primary_key=True)
    username = peewee.CharField(null=True)
    first_name = peewee.CharField(null=True)
    last_name = peewee.CharField(null=True)


class Queries(BaseModel):
    """
    Модель таблицы пользовательских запросов

    query_id: ID запроса. AutoField показывает, что это первичный ключ,
    а значение будет автоматически увеличиваться на единицу. Аналог
    PRIMARY KEY AUTOINCREMENT

    user: внешний ключ, ссылающийся на пользователя.backref создаёт
    обратную ссылку: мы сможем получить задачи пользователя с помощью user.queries

    query_date: дата запроса

    query_text: текст запроса пользователя
    """
    query_id = peewee.AutoField()
    user = peewee.ForeignKeyField(Users, backref="queries")
    query_date = peewee.DateTimeField()
    query_text = peewee.TextField()


class QueryResult(BaseModel):
    """
    Модель таблицы результатов запроса

     result_id: ID результата
     query: внешний ключ, ссылающийся на запрос
     result_text: текст ответа на запрос
     photos: фотографии, если есть
    """
    result_id = peewee.AutoField()
    query = peewee.ForeignKeyField(Queries, backref="result")
    result_text = peewee.TextField()
    photos = peewee.TextField(null=True)
