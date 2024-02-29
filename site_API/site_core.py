from config_data import config

headers_get = {
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": config.HOST_API
}

headers_post = {
    "content-type": "application/json",
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": config.HOST_API
}

url = "https://" + config.HOST_API

default_hotels_payload = {
    "currency": "USD",
    "eapid": 1,
    "locale": "en_US",
    "siteId": 300000001,
    "destination": {"regionId": "2621"},
    "checkInDate": {
        "day": 10,
        "month": 5,
        "year": 2024
    },
    "checkOutDate": {
        "day": 15,
        "month": 5,
        "year": 2024
    },
    "rooms": [
        {
            "adults": 2,
            "children": [{"age": 5}, {"age": 7}]
        }
    ],
    "resultsStartingIndex": 0,
    "resultsSize": 3,
    "sort": "PRICE_LOW_TO_HIGH",
    "filters": {"price": {
        "max": 150,
        "min": 100
    }}
}

default_hotel_info = {
    "currency": "USD",
    "eapid": 1,
    "locale": "en_US",
    "siteId": 300000001,
    "propertyId": "9209612"
}
