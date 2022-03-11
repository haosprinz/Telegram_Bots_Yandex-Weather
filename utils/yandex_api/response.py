# info
# url - Страница населенного пункта на сайте Яндекс.Погода

# fact
# temp - Температура (°C).
# feels_like - Ощущаемая Температура (°C).
# icon как вставить <img src="https://yastatic.net/weather/i/icons/funky/dark/ovc_-sn.svg">
# wind_speed - Скорость ветра (в м/с).
# wind_gust - Скорость порывов ветра (в м/с).
# pressure_mm - Давление (в мм рт. ст.).
# humidity - Влажность воздуха (в процентах).
# is_thunder - Признак грозы. Возможные значения:
#               true — гроза.
#               false — нет грозы.

# Код расшифровки погодного описания
condition = {
    'clear': 'ясно',
    'partly-cloudy': 'малооблачно',
    'cloudy': 'облачно с прояснениями',
    'overcast': 'пасмурно',
    'drizzle': 'морось',
    'light-rain': 'небольшой дождь',
    'rain': 'дождь',
    'moderate-rain': 'умеренно сильный дождь',
    'heavy-rain': 'сильный дождь',
    'continuous-heavy-rain': 'длительный сильный дождь',
    'showers': 'ливень',
    'wet-snow': 'дождь со снегом',
    'light-snow': 'небольшой снег',
    'snow': 'снег',
    'snow-showers': 'снегопад',
    'hail': 'град',
    'thunderstorm': 'гроза',
    'thunderstorm-with-rain': 'дождь с грозой',
    'thunderstorm-with-hail': 'гроза с градом'
}

# Направление ветра
wind_dir = {
    'nw': 'северо-западное',
    'n': 'северное',
    'ne': 'северо-восточное',
    'e': 'восточное',
    'se': 'юго-восточное',
    's': 'южное',
    'sw': 'юго-западное',
    'w': 'западное',
    'с': 'штиль'
}

# Тип осадков. Возможные значения:
prec_type = {
    0: 'без осадков',
    1: 'дождь',
    2: 'дождь со снегом',
    3: 'снег',
    4: 'град',
}

# Сила осадков
prec_strength = {
    0: 'без осадков',
    0.25: 'слабый дождь/слабый снег',
    0.5: 'дождь/снег',
    0.75: 'сильный дождь/сильный снег',
    1: 'сильный ливень/очень сильный снег',
}

# Облачность
cloudness = {
    0: 'ясно',
    0.25: 'малооблачно',
    0.5: 'облачно с прояснениями',
    0.75: 'облачно с прояснениями',
    1: 'пасмурно',
}


def responce(res):
    json_response = res.json()
    result = f"По данным сервиса Яндекс.Погода:\n" \
             f"Сейчас погода {json_response.get('fact').get('temp')}°C\n" \
             f"Ощущается как {json_response.get('fact').get('feels_like')}°C\n" \
             f"Атмосферное давление: {json_response.get('fact').get('pressure_mm')} мм рт. ст.\n" \
             f"{cloudness[json_response.get('fact').get('cloudness')]}, " \
             f"{condition[json_response.get('fact').get('condition')]}\n" \
             f"Влажность воздуха: {json_response.get('fact').get('humidity')}%\n" \
             f"Направление ветра: {wind_dir[json_response.get('fact').get('wind_dir')]}\n" \
             f"Ветер: {json_response.get('fact').get('wind_speed')}м/с\n" \
             f"С порывами: {json_response.get('fact').get('wind_gust')}м/с\n"

    result += json_response.get('info').get('url')

    return result
