import requests
from data.config import YANDEX_URL, YANDEX_KEY, YANDEX_VALUE
from utils.yandex_api.dictionary_cities import locality


def connect(text):
    # Координаты Челябинска
    lat, lon = locality(text)
    params = dict(lat=lat, lon=lon, lang='ru_RU')

    response = requests.get(YANDEX_URL, params=params, headers={YANDEX_KEY: YANDEX_VALUE})

    # Check the response
    if response:
        json_response = response.json()
        result = json_response.get('info').get('url')
    else:
        # Print the error message for the invalid response
        result = 'Яндекс Апи не отвечает'

    return result