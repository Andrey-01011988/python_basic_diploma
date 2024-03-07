from telebot.handler_backends import StatesGroup, State


class FindHotel(StatesGroup):
    command = State()  # команда, которую выбрал пользователь
    select_city = State()  # пользователь выбирает город
    check_in_date = State()  # вводит дату заезда
    check_out_date = State()  # вводит дату выезда
    adult_guests = State()  # вводит количество взрослых гостей
    children_number = State()  # вводит количество детей (если необходимо)
    children_age = State()  # вводит возраст детей (если необходимо)
    need_photos = State()  # определяет нуж ны ли фото
    photo_number = State()  # вводит количество фотографий отеля
    hotels_number = State()  # Получает количество отелей от пользователя
    show_hotels_high_low = State()  # по информации пользователя выводит результаты запросов lowprice/highprice
    show_hotels_bestdeal = State()  # по информации пользователя выводит результаты запросов bestdeal
    price_min = State()  # минимальная цена для поиска
    price_max = State()  # максимальная цена для поиска
    distance_min = State()  # минимальное расстояние от центра города
    distance_max = State()  # максимальное расстояние от центра города
