import requests
from data.config import YANDEX_URL, YANDEX_KEY, YANDEX_VALUE
from utils.yandex_api.dictionary_cities import locality
from utils.yandex_api.response import responce


def connect(text):
    # Координаты Челябинска
    lat, lon = locality(text)
    if lat == 0:
        return "Введите пожалуйста название населенного пункта правильно\n" \
               "Или возможно я ещё незнаю данного населенного пункта"
    params = dict(lat=lat, lon=lon, lang='ru_RU')

    res = requests.get(YANDEX_URL, params=params, headers={YANDEX_KEY: YANDEX_VALUE})

    # Check the response
    if res:
        result = responce(res)
    else:
        # Print the error message for the invalid response
        result = 'Яндекс.Погода не отвечает напишите позднее'

    return result