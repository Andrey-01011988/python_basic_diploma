from config_data import config

headers_get = {
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": config.HOST_API
}

headers_post = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "9b7c1560cdmsh29d2ef30947066dp163bcfjsn71afb84c95b2",
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

url = "https://" + config.HOST_API
