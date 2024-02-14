from telebot.handler_backends import StatesGroup, State


class FindHotel(StatesGroup):
    command = State()  # команда, которую выбрал пользователь
    select_city = State()  # пользователь выбирает город
    check_in_date = State()  # вводит дату заезда
    check_out_date = State()  # вводит дату выезда
    photo_number = State()  # вводит количество фотографий отеля
    hotels_num = State()  # вводит количество отелей в ответе
    price_min = State()  # минимальная цена для поиска
    price_max = State()  # максимальная цена для поиска
    distance = State()  # расстояние от центра города
